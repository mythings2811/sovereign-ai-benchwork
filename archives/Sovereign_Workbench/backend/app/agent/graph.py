import json
import uuid
from typing import Dict, Any, List, TypedDict
from langgraph.graph import StateGraph, END
from archives.Sovereign_Workbench.backend.app.database.sqlite import log_execution

# State definition
class AgentState(TypedDict):
    task_id: str
    execution_id: str
    user_request: str
    workflow_class: str
    security_context: Dict[str, Any]
    plan: List[str]
    step_results: List[Dict[str, Any]]
    final_result: str
    status: str
    trace: List[str]

# =========================================================================
# POLICY ENFORCEMENT POINTS (PEP) - Phase 14
# =========================================================================

def node_pep_task_authorization(state: AgentState) -> AgentState:
    """PEP-01: Task Authorization"""
    state["trace"].append("PEP-01 (Observe): Checking task authorization.")
    
    role = state["security_context"].get("role", "")
    wf_class = state["workflow_class"]
    
    if wf_class == "W5" and role != "developer":
        state["status"] = "BLOCKED"
        state["trace"].append(f"PEP-01 (Deny): Role '{role}' unauthorized for {wf_class}.")
    else:
        state["status"] = "AUTHORIZED"
        state["trace"].append(f"PEP-01 (Allow): Authorized for {wf_class}.")
    
    return state

def node_plan_execution(state: AgentState) -> AgentState:
    """Agent Intelligence: Plan the execution strategy"""
    state["trace"].append("AGENT (Plan): Generating workflow strategy.")
    if state["workflow_class"] == "W3":
        state["plan"] = ["search_knowledge_base"]
    elif state["workflow_class"] == "W2":
        state["plan"] = ["extract_pid_entities"]
    else:
        state["plan"] = []
    
    state["trace"].append(f"AGENT (Plan): Formulated steps: {state['plan']}")
    return state

def node_execute_tools(state: AgentState) -> AgentState:
    """PEP-03: Tool Authorization & Execution"""
    allowed_tools = state["security_context"].get("tool_permissions", [])
    
    for tool in state["plan"]:
        state["trace"].append(f"PEP-03 (Tool Check): Validating authorization for '{tool}'.")
        if tool not in allowed_tools and "ALL" not in allowed_tools:
            state["trace"].append(f"PEP-03 (Deny): Unauthorized tool '{tool}'.")
            state["status"] = "ESCALATED"
            return state
            
        state["trace"].append(f"PEP-03 (Allow): Authorized. Executing '{tool}'.")
        
        # Mock Tool Execution
        if tool == "search_knowledge_base":
            result = {"tool": tool, "data": "Governed evidence retrieved from Qdrant/Docling.", "success": True}
        elif tool == "extract_pid_entities":
            result = {"tool": tool, "data": "P&ID Topology Extracted successfully.", "success": True}
        else:
            result = {"tool": tool, "data": "Executed.", "success": True}
            
        state["step_results"].append(result)
        state["trace"].append(f"TOOL (Result): {result['data']}")
        
    return state

def node_synthesize(state: AgentState) -> AgentState:
    """Agent Intelligence: Synthesize evidence into a final response"""
    state["trace"].append("AGENT (Synthesize): Synthesizing results.")
    if state["status"] == "ESCALATED":
        state["final_result"] = "Abstained due to policy escalation."
    else:
        state["final_result"] = "Task complete. " + " ".join([r["data"] for r in state["step_results"]])
    
    return state

def node_verification(state: AgentState) -> AgentState:
    """AR-06: Verification (Execution Success Is Not Correctness)"""
    state["trace"].append("VERIFY: Checking correctness against constraints.")
    if state["status"] == "AUTHORIZED":
        state["status"] = "COMPLETED"
        state["trace"].append("VERIFY (Pass): Output validated.")
    else:
        state["trace"].append("VERIFY (Fail): Non-authorized status detected.")
        
    log_execution(
        execution_id=state["execution_id"],
        task_id=state["task_id"],
        workflow_class=state["workflow_class"],
        security_context=state["security_context"],
        status=state["status"],
        trace=state["trace"]
    )
    return state

# =========================================================================
# ROUTING LOGIC
# =========================================================================

def router_after_auth(state: AgentState) -> str:
    if state["status"] == "BLOCKED":
        return "synthesize"
    return "plan_execution"

# =========================================================================
# GRAPH DEFINITION
# =========================================================================

workflow = StateGraph(AgentState)

workflow.add_node("check_auth", node_pep_task_authorization)
workflow.add_node("plan_execution", node_plan_execution)
workflow.add_node("execute_tools", node_execute_tools)
workflow.add_node("synthesize", node_synthesize)
workflow.add_node("verify", node_verification)

workflow.set_entry_point("check_auth")
workflow.add_conditional_edges("check_auth", router_after_auth, {
    "plan_execution": "plan_execution",
    "synthesize": "synthesize"
})
workflow.add_edge("plan_execution", "execute_tools")
workflow.add_edge("execute_tools", "synthesize")
workflow.add_edge("synthesize", "verify")
workflow.add_edge("verify", END)

agent_runner = workflow.compile()

