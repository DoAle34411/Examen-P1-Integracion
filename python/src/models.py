from pydantic import BaseModel

class Envio(BaseModel):
    id: str
    cliente: str
    direccion: str
    estado: str
