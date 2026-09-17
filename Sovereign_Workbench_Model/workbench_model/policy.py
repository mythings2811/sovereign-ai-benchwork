from .contracts import SecurityContext, TaskRequest, Workflow


class PolicyDecision:
    def __init__(self, allowed: bool, reason: str):
        self.allowed = allowed
        self.reason = reason


def authorize(request: TaskRequest) -> PolicyDecision:
    if request.workflow is Workflow.W5:
        return PolicyDecision(False, "W5 code execution is disabled in the offline reference model.")
    required = f"execute_{request.workflow.value.lower()}"
    if required not in request.security.permissions and "admin" not in request.security.permissions:
        return PolicyDecision(False, f"Permission '{required}' is required.")
    return PolicyDecision(True, "Authorized by external policy.")


def authorize_upload(context: SecurityContext) -> PolicyDecision:
    if "execute_w2" not in context.permissions and "admin" not in context.permissions:
        return PolicyDecision(False, "Permission 'execute_w2' is required.")
    return PolicyDecision(True, "Authorized by external policy.")
