from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
import uuid
import os
from openai import OpenAI

app = FastAPI(title="TaskFlow Pro API", version="1.0.0")

# --- Models ---


class TaskStatus(str, Enum):
    TODO = "Todo"
    IN_PROGRESS = "In Progress"
    DONE = "Done"


class TaskPriority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    owner_id: str


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class SubtaskRequest(BaseModel):
    task_description: str


class SubtaskResponse(BaseModel):
    original_task: str
    subtasks: List[str]


# --- Mock Data ---

tasks_db = [
    {
        "id": "1",
        "title": "Fix Login Bug",
        "description": "Users getting 403 on dashboard.",
        "status": TaskStatus.IN_PROGRESS,
        "priority": TaskPriority.HIGH,
        "owner_id": "user_123",
    },
    {
        "id": "2",
        "title": "Update Homepage Hero",
        "description": "New copy provided by marketing.",
        "status": TaskStatus.TODO,
        "priority": TaskPriority.MEDIUM,
        "owner_id": "user_123",
    },
    {
        "id": "3",
        "title": "Database Migration",
        "description": "Move from Postgres 12 to 14.",
        "status": TaskStatus.DONE,
        "priority": TaskPriority.HIGH,
        "owner_id": "user_123",
    },
]

# --- Endpoints ---


@app.post("/auth/login", response_model=LoginResponse)
def login(creds: LoginRequest):
    """
    Mock Login: Returns a fake JWT for any non-empty credentials.
    """
    if not creds.username or not creds.password:
        raise HTTPException(status_code=400, detail="Username and password required")

    # In a real app, we'd verify hash and sign JWT
    return {
        "access_token": f"mock_jwt_token_for_{creds.username}",
        "token_type": "bearer",
    }


@app.get("/tasks", response_model=List[Task])
def get_tasks(owner_id: Optional[str] = None):
    """
    List tasks, optionally filtered by owner_id.
    """
    if owner_id:
        return [t for t in tasks_db if t["owner_id"] == owner_id]
    return tasks_db


@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    """
    Create a new task.
    """
    new_task = task.dict()
    new_task["id"] = str(uuid.uuid4())
    tasks_db.append(new_task)
    return new_task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    """
    Get a specific task by ID.
    """
    for t in tasks_db:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks/{task_id}/ai-breakdown", response_model=SubtaskResponse)
def generate_subtasks(task_id: str):
    """
    AI Endpoint: Generates subtasks for a given task ID.
    Uses OpenAI if available, otherwise falls back to mock data.
    """
    task = next((t for t in tasks_db if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    api_key = os.environ.get("OPENAI_API_KEY")

    if api_key:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a project manager. Break down the following task into 3-5 actionable subtasks.",
                    },
                    {
                        "role": "user",
                        "content": f"Task: {task['title']}\nDescription: {task['description']}",
                    },
                ],
            )
            content = response.choices[0].message.content
            # Simple parsing (assuming list format or just returning lines)
            subtasks = [
                line.strip("- ").strip() for line in content.split("\n") if line.strip()
            ]

            return {
                "original_task": task["title"],
                "subtasks": subtasks[:5],  # Limit to 5
            }
        except Exception as e:
            print(f"OpenAI Error: {e}. Falling back to mock.")
            # Fall through to mock

    # Mock AI Logic (Fallback)
    return {
        "original_task": task["title"],
        "subtasks": [
            f"Research requirements for {task['title']}",
            f"Draft initial implementation for {task['title']}",
            "Review code with team",
            "Deploy to staging",
        ],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
