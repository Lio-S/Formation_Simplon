# import basics  pip install mysqlclient
import os
import pandas as pd
import numpy as np
from os.path import join

from sqlalchemy import create_engine
from sqlalchemy import delete

from sqlalchemy.orm import sessionmaker
from sympy import Order, Product
from models.model import Customers, Orders, Products, Base
# , Nom, Prix

from sqlalchemy_utils import database_exists, create_database, drop_database

import config

# Importation des informations de connexion
DATABASE_HOST = config.DATABASE_HOST
DATABASE_NAME = config.DATABASE_NAME
DATABASE_USERNAME = config.DATABASE_USERNAME
DATABASE_PASSWORD = config.DATABASE_PASSWORD

# Création du moteur de base de données
# engine = create_engine("mysql+pymysql://root:root@localhost/my_database_tmp")
engine = create_engine(f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}")

# # Définir le nom de la base de données
# def bk():
#     return print("\n",79*'=','\n')

# file_path = join(join("data","data.csv"))

# if os.path.exists(file_path):
#     data = pd.read_csv(file_path)
#     # Ouvrir le fichier CSV
#     data = pd.read_csv(file_path)
# else:
#     bk()
#     print(file_path)
#     bk()
#     print("The file 'data.csv' does not exist in the directory 'data'")
#     print("pwd", os.getcwd())
#     bk()

if database_exists(engine.url):
    drop_database(engine.url)    

create_database(engine.url)
print("is database existing?: ", database_exists(engine.url))

# Création des tables
Base.metadata.create_all(engine)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()


df = pd.DataFrame([["1", "Produit_1", "100"],["2", "Produit_2", "100"]],columns = ["id_","no_","pri_"])
# print(df)
for i,r in df.iterrows() :
    new_product = Products(identifiant=r["id_"], nom=r["no_"], prix=r["pri_"])
    session.add(new_product)

# Validation des modifications pour les tables Genre et Pays
session.commit()

# Lecture des données dans la DB Products
result = session.query(Products).all()
for Produit in result :
    print(Produit.nom,Produit.identifiant,Produit.prix)
# df = pd.DataFrame(result, columns=df.columns)

# Création des tables customers et order :
df = pd.DataFrame([["1", "user_1", "u1@u.fr"],["2", "user_2", "u2@u.fr"]],columns = ["id_","no_","email_"])

for i,r in df.iterrows() :
    new_product = Customers(identifiant=r["id_"], nom=r["no_"], email=r["email_"])
    session.add(new_product)

df = pd.DataFrame([["1", "1", "1"],["2", "2", "2"]],columns = ["id_","Custom_id","Product_id"])

for i,r in df.iterrows() :
    new_product = Orders(identifiant=r["id_"], customers_id=r["Custom_id"], product_id=r["Product_id"])
    session.add(new_product)

# Lecture des données dans la DB Customers
result = session.query(Customers).all()
for Utilisateurs in result :
    print(Utilisateurs.nom,Utilisateurs.identifiant,Utilisateurs.email)

# Lecture des données dans la DB Orders
result = session.query(Orders).all()
# for Ord in result :
#     print(Ord.customers_id,Ord.identifiant,Ord.product_id)

session.commit()

result = session.query(
    Products.nom,
    Products.prix,
    Customers.nom,
    Customers.email
).join(Orders, Orders.product_id == Products.identifiant).join(Customers, Customers.identifiant == Orders.customers_id).all()


# MAJ données produit
product = session.query(Products).filter_by(identifiant=2).first()
product.prix = 500

session.commit()

# result = session.query(Products).all()
# for Produit in result :
#     print(Produit.nom,Produit.identifiant,Produit.prix)

#Suppression de la commande avec Id 2 :
result = delete(Orders).where(Orders.identifiant == 2)
# <> result = DELETE FROM Orders WHERE Orders.identifiant = :2
session.execute(result)
session.commit()

result = session.query(Orders).all()

for Ord in result :
    print(Ord.product_id,Ord.identifiant,Ord.customers_id)
    
session.close()