from pydantic import BaseModel
from enum import Enum
from typing import List


class Cours(str, Enum):
    mathematiques="mathematiques"
    informatique="informatique"
    francais="francais"
    anglais="anglais"


class Enseignant(BaseModel):
    id: int
    nom: str
    prenom: str
    age: int
    cours: List[Cours]

class Eleve(BaseModel):
    id: int
    nom: str
    prenom: str
    age: int
    classe: str