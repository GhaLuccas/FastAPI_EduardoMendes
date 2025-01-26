from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import Todo, User
from fast_zero.schemas import TodoPublic, TodoSchema
from fast_zero.security import get_current_user

todo_routerss = APIRouter(prefix='/todo', tags=['todos'])

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@todo_routerss.post('/', response_model=TodoPublic)
def create_todo(todo: TodoSchema, session: Session, user: CurrentUser):

    db_todo = Todo(
        title=todo.title,
        description=todo.desciption,
        state=todo.state,
        user_id=user.id,
    )

    return todo
