import streamlit as st
import pandas as pd

st.title('Lecture et Affichage de Données depuis Différents Fichiers')


forma = st.sidebar.radio('Select format:',['CSV', 'JSON', 'XLS'])

if forma == 'CSV':
    st.subheader('Format CSV')
    file = st.file_uploader('Choose a CSV file')
    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df)

if forma == 'JSON':
    st.subheader('Format JSON')
    file = st.file_uploader('Choose a JSON file')
    if file is not None:
        df = pd.read_json(file, orient='records', dtype="string")
        st.dataframe(df)

if forma == 'XLS':
    st.subheader('Format EXCEL')
    file = st.file_uploader('Choose an Excel file',type = ".xls")
    if file is not None:
        df = pd.read_excel(file)
        st.dataframe(df)