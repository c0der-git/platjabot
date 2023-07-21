from typing import List
from pydantic import BaseModel

class Measurement(BaseModel):
    timestamp: str
    bandera: str
    motiuBandera: str
    meteorologia: str
    transparenciaAigua: str
    estatMar: str
    observacions: str
    marDeFons: bool
    temperatura: int
    meduses: str

class Beach(BaseModel):
    _id: str
    codiPlatja: str
    platjaNom: str
    coordenades: str
    banderaBlava: str
    municipi: str
    costa: str
    measurements: List[Measurement]