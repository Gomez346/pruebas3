import json
import shutil
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import repository
from app.main import app

DB_ORIGINAL = Path(__file__).parent / "db_seed.json"
DB_REAL = repository.DB_PATH


@pytest.fixture(autouse=True)
def reset_db():
    """Restaura db.json a su estado inicial ANTES de cada test."""
    shutil.copy(DB_ORIGINAL, DB_REAL)
    yield
    shutil.copy(DB_ORIGINAL, DB_REAL)


@pytest.fixture
def client():
    return TestClient(app)