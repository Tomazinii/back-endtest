from sqlalchemy import Column, Integer, String, ForeignKey,Enum
from src.infra.config import Base
import enum

class AnimalTypes(enum.Enum):
    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False,unique=True)
    specie = Column(Enum(AnimalTypes),nullable=False)
    age = Column(Integer)
    user_id = Column(Integer,ForeignKey("users.id"))

    def __repr__(self) -> str:
        return self.name