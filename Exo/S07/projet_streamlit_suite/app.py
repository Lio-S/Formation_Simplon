from matplotlib.widgets import Slider
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Personnalisation des widgets")

# Personnaliser un widget bouton
button = st.button("Cliquez-moi")

if button:
    st.write("Vous avez cliqué sur le bouton !")

# Personnaliser un widget Curseur
age = st.slider("selectionnez votre âge",0,100,25 )
st.write("Vous avez", age, "ans")

# Personnaliser un widget Zone de texte
nom = st.text_input("Entrez votre nom","Nom")
st.write("Bonjour", nom,"!")

# Personnaliser un widget Case à cocher
details = st.checkbox("Montrez les détails")
if details:
    st.write("Les détails sont affichés !")


freq_slider = st.slider("selectionnez la fréquence",0,512)
st.write("Fréquence =", freq_slider, "Hz")

def sinusoid(f, T=0.01, ech=40000):
    x = np.arange(0, T, 1/ech)
    y = np.sin(np.pi*2*f*x)

    return x, y

fig, ax = plt.subplots()
s_x, s_y = sinusoid(freq_slider)
ax.plot(s_x, s_y)
# st.pyplot(fig)
st.line_chart(s_y)
    

# # Utiliser du HTML pour personnaliser le bouton
button_html = """
<style>
    .stButton>button {
        background-color: green;
        color: white;
        border: 2px solid black;
        border-radius: 8px;
    }
</style>
"""
st.markdown(button_html, unsafe_allow_html=True)
