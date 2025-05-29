import pytest
import sys
import os
from fastapi.testclient import TestClient

print("PATH IS: ", os.path.abspath(os.path.join(os.path.dirname(__file__))))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)