echo "[INFO] Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[INFO] Iniciando API en http://localhost:8000..."
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
