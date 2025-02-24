# nodbapi.py
from fastapi import FastAPI
from pydantic import BaseModel

from nodb import AnimalManager



app = FastAPI()
manager = AnimalManager()
manager.create_default_animals()


# Request models
class DogRequest(BaseModel):
    name: str
    breed: str


class CatRequest(BaseModel):
    name: str
    color: str


# Routes
@app.get("/")
def read_root():
    return {"message": "Welcome to the Animal API!"}


@app.get("/dog")
def get_dog():
    """Get the first Dog JSON."""
    return manager.get_dog_json()


@app.get("/cat")
def get_cat():
    """Get the first Cat JSON."""
    return manager.get_cat_json()


@app.post("/dog")
def create_dog(dog: DogRequest):
    """Create a custom Dog."""
    return manager.create_custom_dog(dog.name, dog.breed)


@app.post("/cat")
def create_cat(cat: CatRequest):
    """Create a custom Cat."""
    return manager.create_custom_cat(cat.name, cat.color)