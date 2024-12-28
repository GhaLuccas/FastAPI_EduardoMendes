from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_OK_e_helloword():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Action

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'hello word'}  # Assert


def test_read_html_deve_retornar_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert ' <h1> Olá Mundo </h1>' in response.text
