from app.model.todo import TodoModel
from fastapi import APIRouter
from app.service.crud_service import TodoService

router = APIRouter(prefix="/v1/todo")

@router.get("/", response_model=list[TodoModel])
async def get_all_todos():
    return TodoService.get_all_todos()

@router.post("/")
async def create_new_todo(todo: TodoModel):
    return TodoService.create_new_todo(todo)

