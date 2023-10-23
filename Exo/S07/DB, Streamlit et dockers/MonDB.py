from pymongo import MongoClient
import streamlit as st
import mysql.connector

st.title('Connexion à une Base de Données NoSQL (MongoDB)')

# Connexion Base MongoDB :
# client = MongoClient("mongodb://localhost:3306/")
client = MongoClient()
db = client["mon_conteneur_myDBMongo"]
collection = db["utilisateurs"]

name = st.text_input("Entrez votre nom","name")
email = st.text_input("Entrez votre email","email")

button = st.button("Enregistrer")

if button:
    st.write("Enregistrement effectué")
    post = {
            "name": name,
            "email": email,
        }
    collection.insert_one(post)

button = st.button("Supprimer")

if button:
    st.write("Suppression effectuée")
    post = {
            "name": name,
            "email": email,
        }
    collection.delete_one(post)
    
for user in collection.find():
    st.write(user)




# Connexion Base SQL :
# host = "localhost" # L'hôte du serveur MySQL
# user = "root"  # Votre nom d'utilisateur MySQL
# password = "root"  # Votre mot de passe MySQL
# database_name = "ma_bdd_streamlit"
# port = "3307"
