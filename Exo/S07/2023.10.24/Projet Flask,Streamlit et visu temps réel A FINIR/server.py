##########################################################
# to run: FLASK_APP=server.py flask run ou flask --app server.py --debug run
##########################################################
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from flask import Flask, request
from os.path import join
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression , Perceptron, LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.svm import SVC

# Charger les données
# df = pd.read_csv(join("..","data","titanic.csv") )
df = pd.read_csv('titanic.csv')

app = Flask(__name__)

# Nettoyage Fichier:
# Remplacer les valeurs nulles de la colonne "age" par la moyenne de la colonne
df["Age"] = df["Age"].fillna(df["Age"].mean())
# Supprimer la colonne "Cabin" et "Ticket" car elles ne servent à rien pour du ML
df = df.drop(["Cabin","Ticket"], axis=1)
# Enlever l'espace dans le nom de colonne Passenger ID
df = df.rename(columns = {'Passenger ID':'Passenger_ID'})
# Créer des colonnes hot encoder pour les données catégorielles
# categorical_columns = ["Sex", "Embarked"]
# for column in categorical_columns:
#     df = pd.get_dummies(df, columns=[column])



@app.route("/api/labels")
def labels():
    return json.dumps(df.Passenger_ID.unique().tolist())

@app.route("/api/data")
def data():
    selector = request.args.get("selector")
    if not selector:
        selector = "Name"
    # print(selector)
    data = df[df["Name"].isin([selector])]
    # print(data)
    return json.dumps(data.to_json())

#Affichage du nombre de passager:
@app.route("/api/Nb_Pass")
def Nb_Pass():
    return json.dumps(len(df.Passenger_ID))