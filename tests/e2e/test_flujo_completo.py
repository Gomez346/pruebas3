import pytest

pytestmark = pytest.mark.e2e


def test_flujo_completo_crud(client):
    """
    Simula un usuario real:
    1) lista productos
    2) crea uno nuevo
    3) lo consulta
    4) lo borra
    5) verifica que ya no está
    """
    # 1) listar
    r = client.get("/productos")
    assert r.status_code == 200
    inicial = len(r.json())

    # 2) crear
    r = client.post("/productos", json={"nombre": "Auriculares", "precio": 60.0, "stock": 20})
    assert r.status_code == 201
    nuevo_id = r.json()["id"]

    # 3) consultar
    r = client.get(f"/productos/{nuevo_id}")
    assert r.status_code == 200
    assert r.json()["nombre"] == "Auriculares"

    # 4) borrar
    r = client.delete(f"/productos/{nuevo_id}")
    assert r.status_code == 200

    # 5) verificar eliminación
    r = client.get(f"/productos/{nuevo_id}")
    assert r.status_code == 404

    # cantidad final == inicial
    r = client.get("/productos")
    assert len(r.json()) == inicial