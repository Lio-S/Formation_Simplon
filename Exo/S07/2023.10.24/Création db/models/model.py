# Importez les modules SQLAlchemy et définissez votre modèle de base
from numpy import integer
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Définissez vos classes de modèle
class Products(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True)
    identifiant = Column(Integer())
    id = Column(Integer, primary_key=True)
    nom = Column(String(255))
    id = Column(Integer, primary_key=True)
    prix = Column(Float())
