##########################################################
# to run: streamlit run app.py
##########################################################
import plotly.express as px
import streamlit as st
import pandas as pd
import requests

# labels
labels = requests.get("http://localhost:5000/api/labels").json()
selector = st.multiselect("Select WELL:", labels)

# load data
data = pd.read_json(
    requests.get("http://localhost:5000/api/data", params={"selector": selector}).json()
)

st.title('Application Streamlit avec communication vers Flask')

# setup figure
fig = px.scatter(
    x=data["PHIND"],
    y=data["GR"],
)
st.write(fig)

st.json

# freq_slider = st.slider("selectionnez la fréquence",0,512)
# st.write("Fréquence =", freq_slider, "Hz")

# def sinusoid(f, T=0.01, ech=40000):
#     x = np.arange(0, T, 1/ech)
#     y = np.sin(np.pi*2*f*x)

#     return x, y

# fig, ax = plt.subplots()
# s_x, s_y = sinusoid(freq_slider)
# ax.plot(s_x, s_y)
# # st.pyplot(fig)
# st.line_chart(s_y)