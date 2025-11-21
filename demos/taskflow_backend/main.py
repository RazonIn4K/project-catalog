from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import random

app = FastAPI(title="TaskFlow Pro API", version="1.0.0")

# Mock Database
tasks_db = [
    {"id": 1, "title": "Fix Login Bug", "description": "Users getting 403 on dashboard.", "status": "In Progress", "priority": "High"},
    {"id": 2, "title": "Update Homepage Hero", "description": "New copy provided by marketing.", "status": "Todo", "priority": "Medium"},
    {"id": 3, "title": "Database Migration", "description": "Move from Postgres 12 to 14.", "status": "Done", "priority": "High"},
]

class Task(BaseModel):
    title: str
    description: str
    status: str = "Todo"
    priority: str = "Medium"

class AIRequest(BaseModel):
    project_id: int

@app.get("/tasks", response_model=List[dict])
def get_tasks():
    return tasks_db

@app.post("/tasks")
def create_task(task: Task):
    new_id = len(tasks_db) + 1
    new_task = task.dict()
    new_task["id"] = new_id
    tasks_db.append(new_task)
    return new_task

@app.post("/ai/summarize_project")
def summarize_project(req: AIRequest):
    """
    Mock AI Endpoint: Simulates calling OpenAI to summarize project status.
    """
    # In a real app, we'd query the DB for this project's tasks and send to GPT-4.
    # Here we just mock the response based on our mock DB.
    
    total = len(tasks_db)
    done = len([t for t in tasks_db if t["status"] == "Done"])
    high_priority = len([t for t in tasks_db if t["priority"] == "High"])
    
    summary = (
        f"Project Status: {done}/{total} tasks completed. "
        f"There are {high_priority} high-priority items remaining. "
        "Overall progress is on track, but the 'Fix Login Bug' task is critical and blocking release."
    )
    
    return {
        "project_id": req.project_id,
        "summary": summary,
        "risk_level": "Medium",
        "suggested_action": "Prioritize the Login Bug fix immediately."
    }

@app.post("/ai/suggest_subtasks")
def suggest_subtasks(task_description: str):
    """
    Mock AI Endpoint: Breaks down a task into subtasks.
    """
    # Mock logic
    return {
        "original_task": task_description,
        "subtasks": [
            "Investigate logs for error patterns",
            "Reproduce issue in staging",
            "Apply fix",
            "Write regression test"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
