import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.header('Análisis interactivo de autos en venta')

# Cargar los datos
df = pd.read_csv('vehicles_us.csv')

st.write(
    """
    Bienvenido a esta aplicación interactiva. Aquí puedes explorar la información de anuncios de autos en venta en EE. UU.,
    visualizando su distribución de kilometraje y la relación entre precio y odómetro según la condición del vehículo.
    """
)

# Mostrar el DataFrame si el usuario lo desea
if st.checkbox('Mostrar datos completos'):
    st.write(df)

# Histograma del odómetro
st.header('Distribución del odómetro')
st.write('El siguiente histograma muestra cómo se distribuyen los kilometrajes de los autos publicados en el dataset.')

fig_hist = px.histogram(df, x='odometer')
st.plotly_chart(fig_hist)

# Gráfico de dispersión precio vs odómetro
st.header('Precio vs. Odómetro')
st.write('Este gráfico compara el precio con el kilometraje, coloreado según la condición del vehículo.')

fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', hover_data=['model', 'model_year'])
st.plotly_chart(fig_scatter)
