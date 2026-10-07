from enum import Enum
from pprint import pprint

from pydantic import BaseModel, Field, ValidationError


class Limbaj(str, Enum):
    PYTHON     = "Python"
    JAVASCRIPT = "JavaScript"
    GO         = "Go"
    RUST       = "Rust"


class Dificultate(str, Enum):
    USOR  = "usor"
    MEDIU = "mediu"
    GREU  = "greu"


class TaskIn(BaseModel):
    titlu:       str = Field(min_length=3)
    limbaj:      Limbaj
    dificultate: Dificultate
    recompensa:  float = Field(gt=0)


def valideaza(date_brute: dict):
    try:
        task = TaskIn.model_validate(date_brute)
        return {"valid": True, "task": task}
    except ValidationError as e:
        pprint(e.errors())
        erori = [f"{'.'.join(str(p) for p in er['loc'])}: {er['msg']}" for er in e.errors()]
        return {"valid": False, "erori": erori}
