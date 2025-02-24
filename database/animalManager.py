# animalManager.py
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database URL
DATABASE_URL = "sqlite:///./animals.db"

# Create engine and session
ENGINE = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

# Base class for mymodels
BASE = declarative_base()

class Dog(BASE):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=False)

class Cat(BASE):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)


class AnimalManager:
    def __init__(self, db: Session):
        self.db = db

    def create_dog(self, name: str, breed: str):
        dog = Dog(name=name, breed=breed)
        self.db.add(dog)
        self.db.commit()
        self.db.refresh(dog)
        return dog

    def create_cat(self, name: str, color: str):
        cat = Cat(name=name, color=color)
        self.db.add(cat)
        self.db.commit()
        self.db.refresh(cat)
        return cat

    def get_dogs(self):
        return self.db.query(Dog).all()

    def get_cats(self):
        return self.db.query(Cat).all()