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
EXAMEN-P1-INTEGRACION/
├── python/
│   ├── src/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── envios.csv
│   │   ├── postman_collection.json
│   │   ├── requirements.txt
├── camel/
├── README.md
├── .gitignore
└── script.sh
```

## ⚙️ Instalación y ejecución Python

### 1. Crear entorno virtual (opcional)
```bash
cd python
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

## ⚙️ Ejecución APACHE CAMEL

Importante: se asume que se cuenta con maven instalado, version 3.9.11.

### 1. Crear entorno virtual (opcional)
```bash
cd camel\camel-labs\lab01\camel-lab
mvn clean package
java -jar target/camel-lab-1.0-SNAPSHOT-shaded.jar
```

## ⚙️ Ejecución PROYECTO COMPLETO

Importante: se asume que se han realizado los pasos previos yla carpeta output dentro de CAMEL se encuentra vacia.
La carpeta input debe contener el archivo llamado envios.csv con el formato determinado.

### 1. Ejecutar entorno python 
```bash
cd python
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
```
### 2. Ejecutar entorno Apache Camel 
```bash
cd python
java -jar target/camel-lab-1.0-SNAPSHOT-shaded.jar
```

### 3. Validar en UISwagger
Abrir en el navegador 
```bash
127.0.0.1:8000/docs
```


## 📌 Estado
Versión inicial `0.0.1` – proyecto base con FastAPI y documentación automática.  
