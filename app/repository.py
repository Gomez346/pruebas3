import json
from pathlib import Path

# Ruta absoluta -> funciona en local Y en GitHub Actions
DB_PATH = Path(__file__).parent / "db.json"


def _leer() -> dict:
    with open(DB_PATH, encoding="utf-8") as f:
        return json.load(f)


def _escribir(data: dict) -> None:
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def listar_productos() -> list[dict]:
    return _leer()["productos"]


def obtener_producto(pid: int) -> dict | None:
    for p in listar_productos():
        if p["id"] == pid:
            return p
    return None


def crear_producto(nombre: str, precio: float, stock: int) -> dict:
    data = _leer()
    nuevo_id = max((p["id"] for p in data["productos"]), default=0) + 1
    nuevo = {"id": nuevo_id, "nombre": nombre, "precio": precio, "stock": stock}
    data["productos"].append(nuevo)
    _escribir(data)
    return nuevo


def eliminar_producto(pid: int) -> bool:
    data = _leer()
    original = len(data["productos"])
    data["productos"] = [p for p in data["productos"] if p["id"] != pid]
    if len(data["productos"]) == original:
        return False
    _escribir(data)
    return True