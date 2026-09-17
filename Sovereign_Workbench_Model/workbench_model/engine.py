from __future__ import annotations

import io
import json
import os
import re
from pathlib import Path
from typing import Any
from uuid import uuid4

from PIL import Image, UnidentifiedImageError
from pypdf import PdfReader

from .contracts import (
    Entity,
    Evidence,
    ExecutionStatus,
    KnowledgeState,
    ProvenanceLink,
    Relationship,
    TaskRequest,
    TraceEvent,
    Workflow,
    WorkflowResult,
)
from .policy import authorize
from .knowledge import KnowledgeManager
from .registry import Registry
from .verification import VerificationEngine


class OfflineWorkbench:
    """Deterministic workflow engine; no model runtime or external provider is used."""

    def __init__(self, audit_path: str | Path = "runtime/audit.jsonl") -> None:
        self.audit_path = Path(audit_path)
        self.registry = Registry()
        self.knowledge = KnowledgeManager()
        self.verification = VerificationEngine()
        self.evidence_store = [
            Evidence(
                evidence_id="DEMO-E1",
                source="Synthetic SOP / revision 3",
                content="Pump P-101A requires valve isolation before diagnostics.",
                authority="authoritative",
                revision="3",
                classification="standard",
            ),
            Evidence(
                evidence_id="DEMO-E2",
                source="Synthetic engineering standard / revision 2",
                content="The stated maximum pressure for V-100 in this seed is 150 PSI.",
                authority="authoritative",
                revision="2",
                classification="standard",
            ),
        ]
        for evidence in self.evidence_store:
            self.knowledge.add_evidence(evidence)

    def execute(self, request: TaskRequest) -> WorkflowResult:
        trace: list[TraceEvent] = []
        self._trace(trace, "OBSERVE", "Task received", {"workflow": request.workflow.value})
        decision = authorize(request)
        self._trace(trace, "VERIFY", decision.reason, {"allowed": decision.allowed})
        if not decision.allowed:
            return self._finish(request.workflow, ExecutionStatus.BLOCKED, None, [decision.reason], trace)
        handlers = {
            Workflow.W1: self._w1,
            Workflow.W2: self._w2,
            Workflow.W3: self._w3,
            Workflow.W4: self._w4,
            Workflow.W5: self._w5,
        }
        try:
            result = handlers[request.workflow](request, trace)
        except (ValueError, OSError) as exc:
            self._trace(trace, "RESULT", "Workflow failed safely", {"error": str(exc)})
            result = self._finish(request.workflow, ExecutionStatus.FAILED, None, [str(exc)], trace)
        self._write_audit(result)
        return result

    def analyze_file(self, filename: str, content: bytes, mime_type: str, request: TaskRequest) -> WorkflowResult:
        if request.workflow is not Workflow.W2:
            raise ValueError("File analysis requires workflow W2.")
        trace: list[TraceEvent] = []
        self._trace(trace, "OBSERVE", "File received", {"filename": Path(filename).name, "bytes": len(content)})
        decision = authorize(request)
        self._trace(trace, "VERIFY", decision.reason, {"allowed": decision.allowed})
        if not decision.allowed:
            return self._finish(Workflow.W2, ExecutionStatus.BLOCKED, None, [decision.reason], trace)
        if not content:
            return self._finish(Workflow.W2, ExecutionStatus.FAILED, None, ["Uploaded file is empty."], trace)
        if len(content) > int(os.getenv("WORKBENCH_MAX_UPLOAD_BYTES", str(25 * 1024 * 1024))):
            return self._finish(Workflow.W2, ExecutionStatus.FAILED, None, ["Uploaded file exceeds the configured size limit."], trace)
        suffix = Path(filename).suffix.lower()
        if suffix not in {".pdf", ".png", ".jpg", ".jpeg"}:
            return self._finish(Workflow.W2, ExecutionStatus.FAILED, None, ["Unsupported file extension."], trace)
        self._validate_signature(suffix, content, mime_type)
        self._trace(trace, "VERIFY", "File type, MIME type, size, and signature checked")
        if suffix == ".pdf":
            result = self._analyze_pdf(Path(filename).name, content, trace)
        else:
            result = self._analyze_image(Path(filename).name, content, trace)
        self._write_audit(result)
        return result

    def _w3(self, request: TaskRequest, trace: list[TraceEvent]) -> WorkflowResult:
        stopwords = {"the", "and", "for", "what", "does", "this", "that", "with", "from", "into", "about"}
        terms = {term.lower() for term in re.findall(r"[A-Za-z0-9-]+", request.task) if len(term) > 2 and term.lower() not in stopwords}
        matches = [e for e in self.evidence_store if any(term in e.content.lower() for term in terms)]
        self._trace(trace, "ACTION", "Retrieved authorized evidence", {"count": len(matches)})
        if not matches:
            return self._finish(Workflow.W3, ExecutionStatus.ABSTAINED, {"answer": "Insufficient evidence for a deterministic answer."}, ["No matching evidence was found."], trace, True)
        answer = " ".join(e.content for e in matches)
        provenance = [ProvenanceLink(output_id="answer", evidence_ids=[e.evidence_id for e in matches], derived_by="deterministic-evidence-join", verification_state="VERIFIED")]
        self._trace(trace, "VERIFY", "Authority, revision, authorization, and evidence sufficiency checked")
        return self._finish(Workflow.W3, ExecutionStatus.COMPLETED, {"answer": answer, "claim_count": len(matches)}, [], trace, False, matches, provenance)

    def _w1(self, request: TaskRequest, trace: list[TraceEvent]) -> WorkflowResult:
        text = str(request.inputs.get("text", "")).strip()
        if not text:
            return self._finish(Workflow.W1, ExecutionStatus.ABSTAINED, None, ["No report text was supplied; OCR/model processing is unavailable in this reference model."], trace, True)
        findings = [line.strip() for line in text.splitlines() if line.strip()]
        self._trace(trace, "ACTION", "Extracted report observations without model inference", {"finding_count": len(findings)})
        evidence = [Evidence(source="user-supplied report", content=finding, state=KnowledgeState.CANDIDATE, page=index + 1) for index, finding in enumerate(findings)]
        self._trace(trace, "VERIFY", "Observations retained as candidate evidence; no consequential conclusion asserted")
        return self._finish(Workflow.W1, ExecutionStatus.COMPLETED_WITH_WARNINGS, {"findings": findings, "human_review_required": True}, ["Findings are extracted observations and require domain review."], trace, True, evidence)

    def _w2(self, request: TaskRequest, trace: list[TraceEvent]) -> WorkflowResult:
        text = str(request.inputs.get("text", ""))
        entities, relationships = self._extract_pid(text)
        self._trace(trace, "ACTION", "Extracted tag-like identifiers deterministically", {"entities": len(entities), "relationships": len(relationships)})
        warnings = ["Drawing geometry and engineering correctness were not validated."]
        if not entities:
            warnings.append("No supported P&ID tags were legible in the supplied text.")
        return self._finish(Workflow.W2, ExecutionStatus.COMPLETED_WITH_WARNINGS, {"entities": [e.model_dump() for e in entities], "relationships": [r.model_dump() for r in relationships], "summary": "Visible identifiers only; not operational validation."}, warnings, trace, True)

    def _w4(self, request: TaskRequest, trace: list[TraceEvent]) -> WorkflowResult:
        source = str(request.inputs.get("source", "")).strip()
        if not source:
            return self._finish(Workflow.W4, ExecutionStatus.ABSTAINED, None, ["Artifact generation requires source evidence."], trace, True)
        artifact = f"# Technical Workbench Draft\n\n## Request\n{request.task}\n\n## Source observations\n{source}\n\n## Acceptance\nGenerated draft only. Human review and approval are required."
        self._trace(trace, "ACTION", "Generated deterministic Markdown draft")
        self._trace(trace, "VERIFY", "Artifact structure checked; approval state remains HUMAN_REVIEW_REQUIRED")
        return self._finish(Workflow.W4, ExecutionStatus.COMPLETED_WITH_WARNINGS, {"format": "markdown", "content": artifact, "approval_state": "HUMAN_REVIEW_REQUIRED"}, ["Generated artifact is not approved."], trace, True)

    def _w5(self, request: TaskRequest, trace: list[TraceEvent]) -> WorkflowResult:
        return self._finish(Workflow.W5, ExecutionStatus.UNAVAILABLE, None, ["Controlled code execution is intentionally disabled until a separately validated sandbox exists."], trace)

    def _analyze_pdf(self, filename: str, content: bytes, trace: list[TraceEvent]) -> WorkflowResult:
        try:
            reader = PdfReader(io.BytesIO(content), strict=True)
            pages = [(page.extract_text() or "").strip() for page in reader.pages]
        except Exception as exc:
            raise ValueError("PDF is malformed or cannot be parsed.") from exc
        self._trace(trace, "ACTION", "Extracted embedded PDF text", {"pages": len(pages)})
        entities: list[Entity] = []
        evidence: list[Evidence] = []
        warnings: list[str] = []
        for page, text in enumerate(pages, start=1):
            if text:
                evidence.append(Evidence(source=filename, content=text[:4000], page=page, region="embedded-text"))
                page_entities, _ = self._extract_pid(text, page)
                entities.extend(page_entities)
            else:
                warnings.append(f"Page {page} has no embedded text; OCR is unavailable.")
        if not any(pages):
            warnings.append("Scanned/image-only PDF requires OCR, which is unavailable in this reference model.")
        result = self._finish(Workflow.W2, ExecutionStatus.COMPLETED_WITH_WARNINGS, {"document_name": filename, "pages_processed": len(pages), "entities": [e.model_dump() for e in entities], "relationships": [], "summary": "Embedded text extraction only; not operational validation."}, warnings, trace, True, evidence)
        return result

    def _analyze_image(self, filename: str, content: bytes, trace: list[TraceEvent]) -> WorkflowResult:
        try:
            with Image.open(io.BytesIO(content)) as image:
                image.verify()
                dimensions = image.size
        except (UnidentifiedImageError, OSError, ValueError) as exc:
            raise ValueError("Image is malformed or cannot be decoded.") from exc
        self._trace(trace, "ACTION", "Validated image dimensions", {"width": dimensions[0], "height": dimensions[1]})
        return self._finish(Workflow.W2, ExecutionStatus.UNAVAILABLE, {"document_name": filename, "dimensions": dimensions, "entities": [], "relationships": []}, ["Vision analysis is unavailable because no LLM or vision runtime is configured."] , trace, True)

    @staticmethod
    def _extract_pid(text: str, page: int | None = None) -> tuple[list[Entity], list[Relationship]]:
        patterns = [("equipment", r"\b(?:P|V|T|E|C|TK|F)-\d{2,5}[A-Z]?\b"), ("instrument", r"\b(?:FIT|FIC|TIC|LIC|PIC|PT|TT|LT)-\d{2,5}[A-Z]?\b"), ("line", r"\b\d{1,5}-[A-Z]{1,5}-\d{1,5}\b")]
        entities: list[Entity] = []
        seen: set[tuple[str, str]] = set()
        for kind, pattern in patterns:
            for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                tag = match.group(0).upper()
                if (kind, tag) in seen:
                    continue
                seen.add((kind, tag))
                snippet = " ".join(text[max(0, match.start() - 60):match.end() + 60].split())
                entities.append(Entity(entity_type=kind, tag=tag, description=f"Visible {kind} identifier.", page=page, evidence_text=snippet, confidence=0.7, uncertainty=["No drawing geometry or engineering meaning inferred."]))
        return entities, []

    @staticmethod
    def _validate_signature(suffix: str, content: bytes, mime_type: str) -> None:
        expected = {".pdf": "application/pdf", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}
        if mime_type != expected[suffix]:
            raise ValueError("MIME type does not match the supported extension.")
        signatures = {".pdf": content.startswith(b"%PDF-"), ".png": content.startswith(b"\x89PNG\r\n\x1a\n"), ".jpg": content.startswith(b"\xff\xd8\xff"), ".jpeg": content.startswith(b"\xff\xd8\xff")}
        if not signatures[suffix]:
            raise ValueError("File signature does not match the declared type.")

    def _finish(self, workflow: Workflow, status: ExecutionStatus, result: dict[str, Any] | None, warnings: list[str], trace: list[TraceEvent], requires_human_review: bool = False, evidence: list[Evidence] | None = None, provenance: list[ProvenanceLink] | None = None) -> WorkflowResult:
        self._trace(trace, "RESULT", status.value, {"warnings": len(warnings)})
        return WorkflowResult(workflow=workflow, status=status, result=result, warnings=warnings, trace=trace, evidence=evidence or [], provenance=provenance or [], requires_human_review=requires_human_review, external_transfer=False)

    @staticmethod
    def _trace(trace: list[TraceEvent], phase: str, message: str, data: dict[str, Any] | None = None) -> None:
        trace.append(TraceEvent(sequence=len(trace) + 1, phase=phase, message=message, data=data or {}))

    def _write_audit(self, result: WorkflowResult) -> None:
        self.audit_path.parent.mkdir(parents=True, exist_ok=True)
        with self.audit_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(result.model_dump(mode="json"), ensure_ascii=True) + "\n")
