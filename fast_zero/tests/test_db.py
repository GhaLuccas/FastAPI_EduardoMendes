from sqlalchemy import select

from fast_zero.models import User


def test_create_user_model(session):
    user = User(username='model-user', email='user@gmail.com', password='senha')
    session.add(user)
    session.commit()
    session.refresh(user)
    result = session.scalar(select(User).where(User.email == 'user@gmail.com'))

    assert result.password == 'senha'
