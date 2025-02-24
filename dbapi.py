# nodbapi.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import BASE, ENGINE, SessionLocal, AnimalManager

# Create tables
BASE.metadata.create_all(bind=ENGINE)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic mymodels
class DogRequest(BaseModel):
    name: str
    breed: str

class CatRequest(BaseModel):
    name: str
    color: str

# Routes
@app.post("/dog")
def create_dog(dog: DogRequest, db: Session = Depends(get_db)):
    manager = AnimalManager(db)
    return manager.create_dog(dog.name, dog.breed)

@app.post("/cat")
def create_cat(cat: CatRequest, db: Session = Depends(get_db)):
    manager = AnimalManager(db)
    return manager.create_cat(cat.name, cat.color)

@app.get("/dogs")
def get_dogs(db: Session = Depends(get_db)):
    manager = AnimalManager(db)
    return manager.get_dogs()

@app.get("/cats")
def get_cats(db: Session = Depends(get_db)):
    manager = AnimalManager(db)
    return manager.get_cats()
