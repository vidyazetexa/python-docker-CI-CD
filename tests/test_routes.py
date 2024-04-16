# tests/test_routes.py
import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Im testing a  Docker, done?!' in response.data
