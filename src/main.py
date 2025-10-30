from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from .models import Envio
from .services import cargar_envios
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="API de Envíos",
    description="Examen P1 Domenica Arcos",
    version="0.0.1"
)

envios_db: List[Envio] = cargar_envios()

@app.get("/envois", response_model=List[Envio])
def get_envios():
    logging.info("[INFO] GET /envios solicitado")
    return envios_db

@app.get("/envios/{id_envio}", response_model=Envio)
def get_envio(id_envio: str):
    logging.info(f"[INFO] GET /envios/{id_envio} solicitado")
    for envio in envios_db:
        if envio.id == id_envio:
            return envio
    raise HTTPException(status_code=404, detail="Envío no encontrado")

@app.post("/envios", response_model=Envio)
def crear_envio(envio: Envio):
    logging.info(f"[INFO] POST /envios solicitado para id={envio.id}")
    if any(e.id == envio.id for e in envios_db):
        raise HTTPException(status_code=400, detail="El envío ya existe")
    envios_db.append(envio)
    return envio
