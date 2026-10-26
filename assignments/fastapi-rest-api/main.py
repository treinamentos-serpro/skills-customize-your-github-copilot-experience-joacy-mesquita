from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Tasks API")


class TaskInput(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


# Use this in-memory list while developing the API.
tasks = [
    {"id": 1, "title": "Read about REST", "completed": False},
    {"id": 2, "title": "Build a FastAPI route", "completed": True},
]
next_task_id = 3


@app.get("/")
def read_root():
    pass


@app.get("/tasks")
def list_tasks():
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_input: TaskInput):
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    pass
