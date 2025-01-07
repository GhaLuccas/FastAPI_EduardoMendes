from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routers.auth import auth_router
from fast_zero.routers.users import users_router
from fast_zero.schemas import Message

app = FastAPI()

# Incluindo os routers
app.include_router(users_router)
app.include_router(auth_router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
