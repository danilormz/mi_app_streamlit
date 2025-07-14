import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Proyecto Licencias Médicas", layout="wide")

st.title("📊 Análisis de Licencias Médicas")
st.write("""
Aplicación creada para presentar el análisis exploratorio de licencias médicas,
siguiendo los criterios de la rúbrica del proyecto.
""")

# Sidebar
st.sidebar.title("Navegación")
seccion = st.sidebar.radio("Ir a:", [
    "Introducción / Objetivos",
    "Limpieza de Datos",
    "Análisis y Visualizaciones",
    "Insights y Conclusiones",
    "Propuesta de Mejora"
])

# Cargar datos (ajusta la ruta si tu archivo está en la carpeta data)
@st.cache_data
def cargar_datos():
    df = pd.read_csv('data/licencias_limpias.csv')
    return df

df = cargar_datos()

# Secciones
if seccion == "Introducción / Objetivos":
    st.header("🎯 Introducción y Objetivos")
    st.markdown("""
    Breve presentación del proyecto:
    - Comprender patrones en la emisión de licencias médicas.
    - Identificar tendencias por género, grupo etario, diagnóstico, etc.
    - Entregar insights para potenciales mejoras del sistema.
    """)

elif seccion == "Limpieza de Datos":
    st.header("🧹 Limpieza de Datos")
    st.markdown("""
    Explicación de pasos realizados:
    - Eliminación de duplicados
    - Homologación de nombres de columnas
    - Conversión de tipos de datos
    - Tratamiento de valores nulos
    """)
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

elif seccion == "Análisis y Visualizaciones":
    st.header("📈 Análisis y Visualizaciones")
    st.markdown("Principales KPIs y gráficos")

    # Ejemplo de gráfico: distribución de licencias por género
    fig, ax = plt.subplots()
    df['Genero'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title('Distribución de Licencias por Género')
    st.pyplot(fig)

    # Aquí puedes agregar más gráficos

elif seccion == "Insights y Conclusiones":
    st.header("💡 Insights y Conclusiones")
    st.markdown("""
    - Insight 1: Mayor cantidad de licencias emitidas a trabajadores de cierto grupo etario.
    - Insight 2: Diagnósticos más frecuentes corresponden a...
    - Insight 3: Diferencias significativas según género.
    """)

elif seccion == "Propuesta de Mejora":
    st.header("🚀 Propuesta de Mejora o Expansión Futura")
    st.markdown("""
    - Integrar datos históricos de más años para analizar evolución.
    - Incorporar Machine Learning para predicción de licencias.
    - Desarrollar dashboard interactivo para distintos perfiles de usuario.
    """)

# Footer bonito
st.markdown("---")
st.markdown("<p style='text-align: center; font-style: italic;'>Creado por el grupo para la entrega final de Business Intelligence</p>", unsafe_allow_html=True)
