import pytest

pytestmark = pytest.mark.integration


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_get_productos(client):
    r = client.get("/productos")
    assert r.status_code == 200
    assert len(r.json()) == 3


def test_get_producto_ok(client):
    r = client.get("/productos/1")
    assert r.status_code == 200
    assert r.json()["nombre"] == "Laptop"


def test_get_producto_404(client):
    r = client.get("/productos/999")
    assert r.status_code == 404


def test_post_producto(client):
    r = client.post("/productos", json={"nombre": "Webcam", "precio": 80.0, "stock": 15})
    assert r.status_code == 201
    data = r.json()
    assert data["id"] == 4
    assert data["nombre"] == "Webcam"


def test_delete_producto(client):
    r = client.delete("/productos/3")
    assert r.status_code == 200
    assert r.json() == {"ok": True}

    r2 = client.get("/productos/3")
    assert r2.status_code == 404