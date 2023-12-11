from pydantic import BaseModel
from typing import Optional


class Serie(BaseModel):
    id: Optional[int] = None
    titulo:str
    ano:int
    genero:Optional[str]
    qtd_temporada: int
    class Config:
        orm_mode = True