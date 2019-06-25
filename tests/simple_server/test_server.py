import pytest

from simple_server import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_hello(client):
    response = client.get("/")
    assert b"Hello World!" == response.data


def test_shout(client):
    response = client.get("/shout?message=hello%20friend")
    assert b"HELLO FRIEND" == response.data
