from __future__ import annotations

from datetime import date
from hashlib import sha256

from .contracts import Document, DocumentRevision, Evidence, KnowledgeState, Source


class KnowledgeManager:
    """Canonical source/document/revision/evidence store; indexes are projections."""

    def __init__(self) -> None:
        self.sources: dict[str, Source] = {}
        self.documents: dict[str, Document] = {}
        self.revisions: dict[str, DocumentRevision] = {}
        self.evidence: dict[str, Evidence] = {}

    def register_source(self, source: Source) -> Source:
        self.sources[source.source_id] = source
        return source

    def register_document(self, document: Document) -> Document:
        if document.source_id not in self.sources:
            raise ValueError("Document source must be registered before the document.")
        self.documents[document.document_id] = document
        return document

    def add_revision(self, revision: DocumentRevision) -> DocumentRevision:
        if revision.document_id not in self.documents:
            raise ValueError("Revision document must be registered before the revision.")
        self.revisions[revision.revision_id] = revision
        return revision

    def add_evidence(self, evidence: Evidence, document_id: str | None = None) -> Evidence:
        if document_id and document_id not in self.documents:
            raise ValueError("Evidence document must be registered before evidence.")
        self.evidence[evidence.evidence_id] = evidence
        return evidence

    def retrieve(self, query: str, scopes: set[str], limit: int = 5) -> list[Evidence]:
        terms = {term.lower() for term in query.split() if len(term) > 2}
        matches: list[tuple[int, Evidence]] = []
        for evidence in self.evidence.values():
            if evidence.classification not in scopes and "ALL" not in scopes:
                continue
            if evidence.state in {KnowledgeState.REJECTED, KnowledgeState.SUPERSEDED, KnowledgeState.UNVERIFIABLE}:
                continue
            score = sum(term in evidence.content.lower() for term in terms)
            if score:
                matches.append((score, evidence))
        matches.sort(key=lambda item: item[0], reverse=True)
        return [evidence for _, evidence in matches[:limit]]

    def fingerprint(self) -> str:
        material = "|".join(sorted(f"{item.evidence_id}:{item.content}:{item.revision}" for item in self.evidence.values()))
        return sha256(material.encode("utf-8")).hexdigest()

    def revoke(self, evidence_id: str) -> None:
        evidence = self.evidence[evidence_id]
        evidence.state = KnowledgeState.REJECTED
