from fastapi import FastAPI, HTTPException
from typing import List
from .models import Envio
from .services import cargar_envios, get_envios_db
from .watcher import start_watcher
import threading
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="API de Envíos",
    description="Examen P1 Domenica Arcos",
    version="0.0.1"
)

# Carga inicial si ya hay archivo
cargar_envios()

# Inicia watcher en hilo separado
threading.Thread(target=start_watcher, daemon=True).start()

@app.get("/envios", response_model=List[Envio])
def get_envios():
    logging.info("[INFO] GET /envios solicitado")
    return get_envios_db()  # devuelve la lista actual

@app.get("/envios/{id_envio}", response_model=Envio)
def get_envio(id_envio: str):
    logging.info(f"[INFO] GET /envios/{id_envio} solicitado")
    for envio in get_envios_db():
        if envio.id == id_envio:
            return envio
    raise HTTPException(status_code=404, detail="Envío no encontrado")

@app.post("/envios", response_model=Envio)
def crear_envio(envio: Envio):
    logging.info(f"[INFO] POST /envios solicitado para id={envio.id}")
    db = get_envios_db()
    if any(e.id == envio.id for e in db):
        raise HTTPException(status_code=400, detail="El envío ya existe")
    db.append(envio)
    return envio
