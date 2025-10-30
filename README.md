# 📘 People Connect API - LMS  
```bash
Aplicación **FastAPI** para el examen P1.  
Incluye una estructura organizada conforme el documento asignado.  
```

## 🚀 Tecnologías usadas
```bash
- [FastAPI](https://fastapi.tiangolo.com/) – Framework principal  
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI  
- [Pydantic](https://docs.pydantic.dev/) – Modelado de datos  
```

## 📂 Estructura del proyecto
```bash
fastapi_project/
│── src/
│   │── main.py 
│   │── models.py 
│   └── services.py/ 
│
│── .gitignore
│── envios.csv
│── postman_collection.json
│── README.md
│── requirements.txt
│── script.sh
```

## ⚙️ Instalación y ejecución

### 1. Crear entorno virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar servidor
```bash
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
```

### 4. Documentación
```bash
Swagger UI → http://127.0.0.1:8000/docs
ReDoc → http://127.0.0.1:8000/redoc
```

## 📌 Estado
Versión inicial `0.0.1` – proyecto base con FastAPI y documentación automática.  
