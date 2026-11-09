import pytest

from app import repository

pytestmark = pytest.mark.unit


def test_listar_productos_devuelve_lista():
    productos = repository.listar_productos()
    assert isinstance(productos, list)
    assert len(productos) == 3


def test_obtener_producto_existente():
    p = repository.obtener_producto(1)
    assert p is not None
    assert p["nombre"] == "Laptop"


def test_obtener_producto_inexistente():
    assert repository.obtener_producto(999) is None


def test_crear_producto_asigna_id_autoincremental():
    nuevo = repository.crear_producto("Monitor", 300.0, 10)
    assert nuevo["id"] == 4
    assert nuevo["nombre"] == "Monitor"
    assert len(repository.listar_productos()) == 4


def test_eliminar_producto_existente():
    assert repository.eliminar_producto(2) is True
    assert repository.obtener_producto(2) is None


def test_eliminar_producto_inexistente():
    assert repository.eliminar_producto(999) is False