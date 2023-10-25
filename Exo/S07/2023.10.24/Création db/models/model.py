# Importez les modules SQLAlchemy et définissez votre modèle de base
import email
from numpy import integer
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Définissez vos classes de modèle
class Products(Base):
    __tablename__ = "products"

    identifiant = Column(Integer, primary_key=True)
    nom = Column(String(255))
    prix = Column(Float())

class Customers(Base):
    __tablename__ = "customers"

    identifiant = Column(Integer, primary_key=True)
    nom = Column(String(255))
    email = Column(String(255))

class Orders(Base):
    __tablename__ = "orders"

    identifiant = Column(Integer, primary_key=True)
    customers_id = Column(Integer(),ForeignKey("customers.identifiant"))
    customers = relationship(Customers)
    product_id = Column(Integer(),ForeignKey("products.identifiant"))
    product = relationship(Products)
