from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import repository

app = FastAPI(title="Tienda API")


class ProductoIn(BaseModel):
    nombre: str
    precio: float
    stock: int


@app.get("/productos")
def get_productos():
    return repository.listar_productos()


@app.get("/productos/{pid}")
def get_producto(pid: int):
    p = repository.obtener_producto(pid)
    if not p:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return p


@app.post("/productos", status_code=201)
def post_producto(body: ProductoIn):
    return repository.crear_producto(body.nombre, body.precio, body.stock)


@app.delete("/productos/{pid}")
def delete_producto(pid: int):
    if not repository.eliminar_producto(pid):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"ok": True}


@app.get("/health")
def health():
    return {"status": "ok"}