from sqlalchemy import create_engine

from fast_zero.models import User, table_registry


def test_create_user_model():
    create_engine('sqlite:///database.db')

    table_registry.metadata.create_all

    user = User(username='model-user', email='user@gmail.com', password='senha')

    assert user.password == 'senha'
