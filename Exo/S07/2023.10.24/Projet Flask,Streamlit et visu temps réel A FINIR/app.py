##########################################################
# to run: streamlit run app.py
##########################################################
import plotly.express as px
import streamlit as st
import pandas as pd
import requests

# # labels
id = requests.get("http://localhost:5000/api/id").json()
selector = st.multiselect("Select Passenger_ID:", id)

# # load data
data = pd.read_json(
    requests.get("http://localhost:5000/api/data", params={"selector": selector}).json()
)
print("data = ", data)
st.title('Application Streamlit avec communication vers Flask av Données temps réel')


# load heure
Heure_Server = (
    requests.get("http://localhost:5000/api/heure").json()
)
st.write(Heure_Server)
st.dataframe(data)

# setup figure
fig = px.scatter(
    x=data["Age"],
    y=data["Survived"],
)
st.write(fig)

st.json