# import basics  pip install mysqlclient
import os
import pandas as pd
import numpy as np
from os.path import join

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from models.model import Products, Base
# , Nom, Prix

from sqlalchemy_utils import database_exists, create_database, drop_database

import config

# Importation des informations de connexion
DATABASE_HOST = config.DATABASE_HOST
DATABASE_NAME = config.DATABASE_NAME
DATABASE_USERNAME = config.DATABASE_USERNAME
DATABASE_PASSWORD = config.DATABASE_PASSWORD

# Création du moteur de base de données
engine = create_engine(f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}")

# Définir le nom de la base de données
def bk():
    return print("\n",79*'=','\n')

file_path = join(join("data","data.csv"))

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    # Ouvrir le fichier CSV
    data = pd.read_csv(file_path)
else:
    bk()
    print(file_path)
    bk()
    print("The file 'data.csv' does not exist in the directory 'data'")
    print("pwd", os.getcwd())
    bk()

# Création de la connexion à la base de données
# engine = create_engine("mysql+pymysql://root:root@localhost/my_database_tmp")
if database_exists(engine.url):
    drop_database(engine.url)    

create_database(engine.url)
print("is database existing?: ", database_exists(engine.url))


# Création des tables
Base.metadata.create_all(engine)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# # Remplissage des tables Genre et Pays
# identifiant_ = data['identifiant'].unique()
# Nom_ = data['Nom'].unique()
# Prix_ = data['Prix'].unique()

# for identifiant in identifiant_:
#     identifiant_obj = Identifiant(nom=identifiant)
#     session.add(identifiant_obj)

# for nom in Nom_:
#     nom_obj = Nom(nom=nom)
#     session.add(nom_obj)

# for prix in Prix_:
#     pays_obj = Prix(nom=prix)
#     session.add(pays_obj)

# Validation des modifications pour les tables Genre et Pays
session.commit()

ar = np.array = (["1", "Produit_1", "100"],["2", "Produit_2", "100"])
df = pd.DataFrame(ar)

identifiant = ar[0:]
nom = ar[1:]
prix = ar[2:]