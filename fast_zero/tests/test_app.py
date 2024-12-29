from http import HTTPStatus


def test_read_root_deve_retornar_OK_e_helloword(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hello word'}


def test_read_html_deve_retornar_html(client):
    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert ' <h1> Olá Mundo </h1>' in response.text


def test_create_user_deve_criar_user(client):
    test_user = {
        'username': 'string',
        'email': 'user@example.com',
        'password': 'string',
    }

    response = client.post('/users/', json=test_user)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'string',
        'email': 'user@example.com',
    }
