import json
import pytest

from app import repository

pytestmark = pytest.mark.integration


def test_leer_db_json_desde_repository():
    """Verifica que la BD real (app/db.json) se puede leer correctamente."""
    with open(repository.DB_PATH, encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert "productos" in data
    assert len(data["productos"]) >= 1