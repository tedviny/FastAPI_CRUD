from ast import Return
from typing import List
from fastapi import FastAPI, HTTPException
from models import Enseignant, Eleve, Cours
from typing import List


app = FastAPI()


@app.get("/")
def hello():
    return{"message": "Bienvenu sur notre API"}


db_enseignant: List[Enseignant]
db_enseignant = [Enseignant(id=1, nom="Doe", prenom="John", age=23, cours=[Cours.informatique, Cours.anglais]),
                 Enseignant(id=2, nom="Doe", prenom="Bob", age=25,
                            cours=[Cours.francais, Cours.anglais])
                 ]


@app.get("/api/v1/enseignants")
def get_enseignants():
    """Affiche tous les enseignants de la liste"""
    return db_enseignant


@app.post("/api/v1/enseignant")
def add_enseignant(enseignant: Enseignant):
    """ Ajout d'un nouvel enseignant dans la liste"""
    db_enseignant.append(enseignant)
    return {"message": f"Enseignant avec id : {enseignant.id} du nom de : {enseignant.nom} a bien été ajouté"}


@app.delete("/api/v1/enseignant/{id:int}")
def remove_enseignant(id: int):
    """Supprimer un enseignant"""
    for index, i in enumerate(db_enseignant):
        if i.id == id:
            db_enseignant.pop(index)
            return {"message": f"Un enseignant avec id: {id} a bien été supprimé"}
    raise HTTPException(status_code=404, detail=f"Enseignant non trouvé")


@app.put("/api/v1/enseignant/{id:int}")
def update_enseignant(enseignant: Enseignant):
    """Modifier un enseignant"""
    if enseignant.id is not None:
        new_enseignant = Enseignant(id=enseignant.id, nom=enseignant.nom,
                                    prenom=enseignant.prenom, age=enseignant.age, cours=enseignant.cours)
        for index, i in enumerate(db_enseignant):
            if i.id == enseignant.id:
                db_enseignant[index] = new_enseignant
    return {"message": f"Enseignant {enseignant.nom} {enseignant.prenom} a bien été modifié"}
