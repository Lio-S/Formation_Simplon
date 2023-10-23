from pymongo import MongoClient
import streamlit as st
import sqlite3
# import mysql.connector
import pandas as pd

st.title('Connexion à une Base de Données NoSQL (SQLite)')

# create a new database and open a database connection to allow sqlite3 to work with it
con = sqlite3.connect("Monty.db")

# Call con.cursor() to create the Cursor:
cur = con.cursor()

# create a database table movie with columns for title, release year, and review score
# cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
cur.execute("CREATE TABLE IF NOT EXISTS utilisateurs(nom varchar, email varchar)")

# verify that the new table has been created by querying the sqlite_master table built-in to SQLite
# res = cur.execute("SELECT nom FROM sqlite_master")

# print(res.fetchone())
# ('movie',)


nom = st.text_input("Entrez votre nom","nom")
email = st.text_input("Entrez votre email","email")

button = st.button("Enregistrer")

if button:
    st.write("Enregistrement effectué")
    res = cur.execute(f"INSERT INTO utilisateurs(nom, email) VALUES('{nom}', '{email}')")

con.commit()

button = st.button("Supprimer")

if button:
    st.write("Suppression effectuée")
    res = cur.execute(f"DELETE FROM utilisateurs WHERE nom = '{nom}' AND email = '{email}'")
    
con.commit()

res = cur.execute(f"SELECT * FROM utilisateurs")
st.dataframe(pd.DataFrame(cur.fetchall(), columns=['nom','email']))

# con.close() Toujours penser à fermer la connexion
# Pour vérifier que la connexion est fermée :
# res = cur.execute(f"SELECT * FROM utilisateurs")


# Afin de tester l'existence de la table:
# res.fetchone() is None
# >True

# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)

# con.commit()

# res = cur.execute("SELECT score FROM movie")

# res.fetchall()
# [(8.2,), (7.5,)]

# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# # con.commit()  Remember to commit the transaction after executing INSERT.

# for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):

#     print(row)
# (1971, 'And Now for Something Completely Different')
# (1975, 'Monty Python and the Holy Grail')
# (1979, "Monty Python's Life of Brian")
# (1982, 'Monty Python Live at the Hollywood Bowl')
# (1983, "Monty Python's The Meaning of Life")

# con.close()

# new_con = sqlite3.connect("tutorial.db")

# new_cur = new_con.cursor()

# res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")

# title, year = res.fetchone()

# print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
