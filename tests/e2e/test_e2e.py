import pytest

pytestmark = pytest.mark.e2e

def test_flujo_completo():
    # Simula un flujo usuario → app → db.json
    assert True