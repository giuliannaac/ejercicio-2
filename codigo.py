import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Título de la aplicación
st.title("Visualización de datos de Pingüinos")

# Cargar dataset
penguins = sns.load_dataset("penguins")

# Mostrar dataset
st.write("## Datos de los pingüinos 🐧")
st.dataframe(penguins)

# Gráfico de caja por especie
fig1 = px.box(penguins, x="species", y="flipper_length_mm", color="species", title="Longitud de Aletas por Especie")
st.plotly_chart(fig1)

# Gráfico de caja por sexo
fig2 = px.box(penguins, x="sex", y="flipper_length_mm", color="sex", title="Longitud de Aletas por Sexo")
st.plotly_chart(fig2)
