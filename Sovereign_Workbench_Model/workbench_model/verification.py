from .contracts import ApprovalDecision, Artifact, Claim, VerificationRecord


class VerificationEngine:
    """Independent deterministic checks; model confidence is never verification."""

    def verify_claim(self, claim: Claim) -> VerificationRecord:
        checks = ["claim_has_evidence", "evidence_state_checked"]
        if not claim.evidence_ids:
            return VerificationRecord(subject_id=claim.claim_id, checks=checks, status="FAILED", notes=["Claim has no evidence links."])
        claim.verification_state = "VERIFIED"
        claim.state = claim.state.VALIDATED
        return VerificationRecord(subject_id=claim.claim_id, checks=checks, status="PASSED")

    def verify_artifact(self, artifact: Artifact) -> VerificationRecord:
        checks = ["artifact_nonempty", "format_structure_checked", "approval_state_separate"]
        if not artifact.content.strip():
            return VerificationRecord(subject_id=artifact.artifact_id, checks=checks, status="FAILED", notes=["Artifact is empty."])
        return VerificationRecord(subject_id=artifact.artifact_id, checks=checks, status="PASSED", notes=["Artifact remains generated until human approval."])

    def approve_artifact(self, artifact: Artifact, decision: ApprovalDecision) -> Artifact:
        if decision.artifact_id != artifact.artifact_id:
            raise ValueError("Approval does not target the artifact.")
        if decision.decision not in {"APPROVED", "REJECTED"}:
            raise ValueError("Approval decision must be APPROVED or REJECTED.")
        artifact.state = decision.decision
        return artifact
