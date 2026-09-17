import uuid
from typing import Dict, Any, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from archives.Sovereign_Workbench.backend.app.agent.graph import agent_runner
from archives.Sovereign_Workbench.backend.app.database.sqlite import get_execution

app = FastAPI(title="Sovereign Agentic AI Workbench API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SecurityContextModel(BaseModel):
    user_identity: str
    role: str
    data_permissions: List[str]
    tool_permissions: List[str]

class TaskRequestModel(BaseModel):
    user_request: str
    workflow_class: str
    security_context: SecurityContextModel

@app.post("/api/v1/task/execute")
async def execute_task(req: TaskRequestModel):
    execution_id = str(uuid.uuid4())
    task_id = str(uuid.uuid4())
    
    initial_state = {
        "task_id": task_id,
        "execution_id": execution_id,
        "user_request": req.user_request,
        "workflow_class": req.workflow_class,
        "security_context": req.security_context.model_dump(),
        "plan": [],
        "step_results": [],
        "final_result": "",
        "status": "INITIALIZED",
        "trace": []
    }
    
    # Run the LangGraph agent
    final_state = agent_runner.invoke(initial_state)
    
    return {
        "execution_id": final_state["execution_id"],
        "status": final_state["status"],
        "result": final_state["final_result"],
        "trace": final_state["trace"]
    }

@app.get("/api/v1/execution/{execution_id}")
async def fetch_execution(execution_id: str):
    record = get_execution(execution_id)
    if not record:
        raise HTTPException(status_code=404, detail="Execution not found")
    return record

@app.get("/api/v1/health")
def health_check():
    return {"status": "online", "mode": "Stage 1 - LangGraph Integration"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

