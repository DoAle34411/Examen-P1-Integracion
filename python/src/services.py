import csv
import logging
import time
from pathlib import Path
from typing import List
from .models import Envio

logging.basicConfig(level=logging.INFO)

# Carpeta actual del script
BASE_DIR = Path(__file__).resolve().parent

# Ruta dinámica hacia outputs de Camel
OUTPUTS_DIR = BASE_DIR.parent.parent / "camel" / "camel-labs" / "lab01" / "camel-lab" / "output"
CURRENT_CSV = OUTPUTS_DIR / "envios.csv"

# Base de datos en memoria
_envios_db: List[Envio] = []

def cargar_envios() -> List[Envio]:
    """Carga envíos desde el CSV actual, actualizando _envios_db"""
    global _envios_db
    envios = []

    if not CURRENT_CSV.exists():
        logging.warning(f"[WARN] Archivo {CURRENT_CSV} no encontrado.")
        return _envios_db

    for attempt in range(5):
        try:
            with open(CURRENT_CSV, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    envio = Envio(
                        id=row['id_envio'],
                        cliente=row['cliente'],
                        direccion=row['direccion'],
                        estado=row['estado']
                    )
                    envios.append(envio)

            _envios_db = envios  # actualizar la base de datos en memoria
            logging.info(f"[INFO] Archivo cargado con {len(envios)} registros.")
            logging.info("[INFO] Datos transformados a formato JSON.")
            return _envios_db
        except PermissionError:
            logging.warning(f"[WARN] Archivo en uso, reintentando 0.5s ({attempt+1}/5)...")
            time.sleep(0.5)

    logging.error("[ERROR] No se pudo abrir el archivo envios.csv después de varios intentos.")
    return _envios_db

def get_envios_db() -> List[Envio]:
    """Devuelve la base de datos actual en memoria"""
    return _envios_db
