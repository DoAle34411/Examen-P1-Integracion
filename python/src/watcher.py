from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
from pathlib import Path
import time
from .services import cargar_envios, OUTPUTS_DIR

logging.basicConfig(level=logging.INFO)

class CSVHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith("envios.csv"):
            logging.info(f"[INFO] Nuevo archivo detectado: {event.src_path}")
            cargar_envios()  # actualiza _envios_db

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith("envios.csv"):
            logging.info(f"[INFO] Archivo modificado: {event.src_path}")
            cargar_envios()  # actualiza _envios_db

def start_watcher():
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, str(OUTPUTS_DIR), recursive=False)
    observer.start()
    logging.info(f"[INFO] Observando carpeta: {OUTPUTS_DIR}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
