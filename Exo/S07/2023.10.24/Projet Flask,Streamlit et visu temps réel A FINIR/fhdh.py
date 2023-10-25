##########################################################
# to run: FLASK_APP=server.py flask run ou flask --app server.py --debug run
##########################################################
import json
import pandas as pd
# Charger les données
# df = pd.read_csv(join("..","data","titanic.csv") )
df = pd.read_csv('titanic_modified.csv')
selector = df.Name[0]
print(selector)