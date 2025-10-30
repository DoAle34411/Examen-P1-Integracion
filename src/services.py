import csv
import logging
from pathlib import Path
from typing import List
from .models import Envio

logging.basicConfig(level=logging.INFO)

CSV_FILE = Path(__file__).parent.parent / "envios.csv"

def cargar_envios() -> List[Envio]:
    envios = []
    if not CSV_FILE.exists():
        logging.warning(f"[WARN] Archivo {CSV_FILE} no encontrado.")
        return envios

    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            envio = Envio(
                id=row['id_envio'],
                cliente=row['cliente'],
                direccion=row['direccion'],
                estado=row['estado']
            )
            envios.append(envio)
    logging.info(f"[INFO] Archivo cargado con {len(envios)} registros.")
    logging.info("[INFO] Datos transformados a formato JSON.")
    return envios
