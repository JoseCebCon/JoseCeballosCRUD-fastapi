from pydantic import BaseModel

class Libro(BaseModel):
    id: int
    nombre: str
    autor: str
    isbn: str