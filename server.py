from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
import random

# Criar uma instância do FastAPI
app = FastAPI()

# Modelo Pydantic para representar a estrutura dos dados dos animais
class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str

# Lista para armazenar os animais
animais_db : List[Animal] = []

# Rota para cadastrar um novo animal
@app.post("/animais")
def cadastrar_animal(animal: Animal):
    # Gerar um ID randomicamente
    animal.id = str(uuid4())

    # Adicionar o animal à lista
    animais_db.append(animal)

    return animal

# Rota para obter todos os animais cadastrados
@app.get("/animais")
def obter_animais():
    return animais_db

# Rota para obter um animal específico por ID
@app.get("/animais/{animal_id}")
def obter_animal(animal_id: str):
    for animal in animais_db:
        if animal["id"] == animal_id:
            return animal
    raise HTTPException(status_code=404, detail="Animal not found")

# Rota para deletar um animal por ID
@app.delete("/animais/{animal_id}")
def deletar_animal(animal_id: str):
    for i, animal in enumerate(animais_db):
        if animal["id"] == animal_id:
            del animais_db[i]
            return {"message": "Animal deleted successfully"}
    raise HTTPException(status_code=404, detail="Animal not found")
