import streamlit as st
import pandas as pd
st.title('FIFAFURBO!')
st.write('Aquí descubrirás todo lo que el FIFA te puede ofrecer...')
prueba = pd.read_csv("resultados_elecciones_2019.csv", sep=';')
prueba.head()

