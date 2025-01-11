from datetime import datetime


from ..back.report.infrastructure.handlers.StreamlitReportHandler import StreamlitReportHandler as srh
from ..back.report.domain.entities.Report import Report
from ..back.report.domain.patterns.ValueObjects.ReportCampos import ReportCampos



def main(st):
    
    st.set_page_config(
                        # layout="wide",
                        page_title="Reporte de Ordenes"
                        )
    
    
    # Título de la aplicación
    with st.container():
        st.write("<h1 style='text-align: center;'>Reporte Ordenes Todos los Campos</h1>", unsafe_allow_html=True)


    with st.expander("--Instrucciones de uso--"):
        st.write("""
        - Seleccione el rango de fechas sobre el que desea generar el reporte. Si desea consultar para un solo dia, la fecha de fin debe ser un dia mayor a la fecha de inicio. 
        - Seleccione los campos que se deben mostrar en el reporte. Puede escribirlos o seleccionarlos de la lista. Hay un grupo de campos ya preseleccionados.
        - Presione el boton "Generar Reporte" para obtener los resultados y optar a descargalos.
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
    # campos_disponibles = ["CodOrden", "NombreCliente", "Entregado"]
    campos_disponibles = Report(ReportCampos({"CodOrden":"CodOrden"})).campos.campos_validos
    campos_prefijados = ["CodOrden", "OrdenExterna", "TipoOrden", "StatusDOA", "Reingreso", "CodEstado", "NombreStatus", 
                         "CodCliente", "NombreCliente", "Email", "Tlf", "NombreMarca", "NombreSegmento", 
                         "NombreModelo", "Serial1Marca", "Serial1", "Serial2Marca", "Serial2",
                         "Serial3Marca", "Serial3", "Serial4Marca", "Serial4", "Serial5Marca", "Serial5", 
                         "NombreOperadora", "NoLinea", "FechaCompra", "GarantiaFabricante", "GarantiaCS", 
                         "NombreCentro", "NombreNivel", "LoginIngreso", "FechaIngreso", "LoginRevision", 
                         "FechaRevision", "LoginReparacion", "FechaReparacion", "GarantiaFabricanteTCS", 
                         "GarantiaCSTCS", "ObsCliente", "NombreTipoSintoma", "NombreSintoma", "Condiciones", 
                         "Repuestos"]
    campos_seleccionados = st.multiselect("Campos a mostrar", campos_disponibles, default=campos_prefijados)


    #Boton para generar el reporte
    if st.button("Generar Reporte", type='secondary'):
        
        st.write("") # Espacio entre las filas
        st.write("") # Espacio entre las filas

        st.write("Fecha de inicio del rango:", fecha_inicio)
        st.write("Fecha de final del rango:", fecha_final)
        
        data = srh().get_data_report(fecha_inicio, fecha_final, campos_seleccionados)
        
        #Estilo de la tabla
        st.markdown("""
                    <style>
                        .dataframe th, .dataframe td {
                            border: 1px solid #ddd;
                            padding: 8px;
                            text-align: center;
                        }
                        .dataframe th {
                            background-color: #f0f0f0;
                        }
                    </style>
                    """, unsafe_allow_html=True)
        
        #Tabulacion del resultado de la consulta   
        st.dataframe(data, use_container_width=True)
        
        data_bytearray = srh.get_excel_data_report(data)
        
        #Descarga del reporte
        st.download_button(
            type="primary",
            label="Descargar Reporte",
            data=data_bytearray.getvalue(),
            file_name=f"reporte_todos_los_campos {datetime.now()}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )