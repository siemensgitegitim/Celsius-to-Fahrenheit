import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_valid_conversion(client):
    response = client.get('/?celsius=25')
    assert response.status_code == 200
    assert b'Fahrenheit:' in response.data
    assert b'77.0' in response.data

def test_empty_input(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Fahrenheit:' in response.data
    assert b'' in response.data

def test_invalid_input(client):
    response = client.get('/?celsius=invalid')
    assert response.status_code == 200
    assert b'Fahrenheit: invalid input' in response.data
