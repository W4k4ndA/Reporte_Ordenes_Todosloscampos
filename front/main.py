import streamlit as st
from datetime import datetime


# Título de la aplicación
with st.container():
    st.write("<h1 style='text-align: center;'>Reporte Ordenes Todos los Campos</h1>", unsafe_allow_html=True)


with st.expander("--Instrucciones--"):
    st.write("""
    - Seleccione el rango de fechas sobre el que desea generar el reporte.
    - Seleccione los campos que se deben mostrar en el reporte. Puede escribirlos o seleccionarlos de la lista.
    - Presione el boton "Generar Reporte" para obtener los resultados y optar a visualizar los datos y/o descargalos
    """)

st.write("") # Espacio entre las filas
st.write("") # Espacio entre las filas

with st.container():
    st.subheader("Seleccione el rango de fechas para el reporte")

col1, col2 = st.columns(2)
fecha_inicio = col1.date_input("Fecha Inicio", value=datetime.today())
fecha_final = col2.date_input("Fecha Final", value=datetime.today())

st.write("") # Espacio entre las filas
st.write("") # Espacio entre las filas


with st.container():
    st.subheader("Seleccione los campos a mostrar en el reporte")

#Lista de checkbox para seleccionar los campos que se deben mostrar en el reporte
campos_disponibles = ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4", "Opcion 5"]
campos_prefijados = ["Opcion 1", "Opcion 2", "Opcion 4"]
campos_seleccionados = st.multiselect("Campos", campos_disponibles, default=campos_prefijados)


#Boton para generar el reporte
if st.button("Generar Reporte", type='primary'):
    
    st.write("") # Espacio entre las filas
    st.write("") # Espacio entre las filas

    st.write("Fecha de inicio del rango:", fecha_inicio)
    st.write("Fecha de final del rango:", fecha_final)
    
    # st.write("Reporte generado con los siguientes campos:", campos_seleccionados)
    #Resultado de la consulta   
    st.dataframe([i for i in range(10)])