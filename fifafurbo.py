import streamlit as st
import pandas as pd
st.title('FIFAFURBO!')
st.write('Aquí descubrirás todo lo que el FIFA te puede ofrecer...')
prueba = pd.read_csv("C:\Users\tomas\OneDrive - UPV\PRIMERO\2o cuatrimestre (1b)\PRG\PRÁCTICAS\resultados_elecciones_2019.csv", sep=';')
prueba.head()

