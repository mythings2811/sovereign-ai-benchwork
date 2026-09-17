import os
import sqlite3
import json
from typing import Dict, Any

DB_PATH = os.path.join(os.path.dirname(__file__), 'workbench.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Stores the task execution traces as defined in Phase 14
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS executions (
            execution_id TEXT PRIMARY KEY,
            task_id TEXT,
            workflow_class TEXT,
            security_context TEXT,
            status TEXT,
            trace TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_execution(execution_id: str, task_id: str, workflow_class: str, security_context: Dict[str, Any], status: str, trace: list):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO executions (execution_id, task_id, workflow_class, security_context, status, trace)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        execution_id,
        task_id,
        workflow_class,
        json.dumps(security_context),
        status,
        json.dumps(trace)
    ))
    conn.commit()
    conn.close()

def get_execution(execution_id: str) -> Dict[str, Any]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM executions WHERE execution_id = ?', (execution_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "execution_id": row[0],
            "task_id": row[1],
            "workflow_class": row[2],
            "security_context": json.loads(row[3]),
            "status": row[4],
            "trace": json.loads(row[5]),
            "created_at": row[6]
        }
    return None

init_db()

