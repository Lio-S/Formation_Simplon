##########################################################
# to run: FLASK_APP=server.py flask run ou flask --app server.py --debug run
##########################################################
import json
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from flask import Flask, request
from pathlib import Path
from os import path
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression , Perceptron, LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.svm import SVC
from datetime import datetime

# Charger les données
# df = pd.read_csv(join("..","data","titanic.csv") )
filepath = Path('data/titanic.csv')
df = pd.read_csv(filepath)

app = Flask(__name__)

app.testing = True # <> à flask --app server.py --debug run
app.config.update( # Update automatique des templates 
    TEMPLATES_AUTO_RELOAD = True
)
# Nettoyage Fichier:
# Remplacer les valeurs nulles de la colonne "age" par la moyenne de la colonne
df["Age"] = df["Age"].fillna(df["Age"].mean())
# Supprimer la colonne "Cabin" et "Ticket" car elles ne servent à rien pour du ML
df = df.drop(["Cabin","Ticket"], axis=1)
# df = df[1:]
# Enlever l'espace dans le nom de colonne Passenger ID
df = df.rename(columns = {'PassengerId':'Passenger_ID'})
print(df.columns)
df.to_csv('titanic_modified.csv',index=False)

# Créer des colonnes hot encoder pour les données catégorielles
# categorical_columns = ["Sex", "Embarked"]
# for column in categorical_columns:
#     df = pd.get_dummies(df, columns=[column])



@app.route("/api/id")
def id():
    selector = request.args.get("selector")
    if not selector:
        selector = df.Passenger_ID[0]
    Passenger_ID = df[df["Name"].isin([selector])]
    return json.dumps(df.Passenger_ID.unique().tolist())

@app.route("/api/data")
def data():
    selector = request.args.get("selector")
    if not selector:
        selector = df.Name[0]
    # print(selector)
    data = df[df["Name"].isin([selector])]
    # print(data)
    return json.dumps(data.to_json())

#Affichage de l'heure:
@app.route("/api/heure")
def heure():
    heure = str(datetime.now())
    return json.dumps(heure)

print(heure())

if __name__ == "__main__":
    app.run(port=5000)