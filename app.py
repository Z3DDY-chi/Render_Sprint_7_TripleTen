import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el dataset
df = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Cuadro de mandos – Análisis de vehículos')

st.write(
    'Esta aplicación permite explorar de forma visual un conjunto de datos '
    'sobre anuncios de venta de vehículos en Estados Unidos.'
)

# Checkbox para el histograma
show_hist = st.checkbox('Mostrar histograma del kilometraje')

if show_hist:
    st.write('Histograma de la columna odometer')

    fig_hist = px.histogram(
        df,
        x='odometer',
        nbins=50
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para el gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión precio vs kilometraje')

if show_scatter:
    st.write('Relación entre el precio y el kilometraje')

    fig_scatter = px.scatter(
        df,
        x='odometer',
        y='price',
        opacity=0.5
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
    