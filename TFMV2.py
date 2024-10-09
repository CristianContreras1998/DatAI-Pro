import asyncio
import streamlit as st
from dotenv import load_dotenv
import os
import openai # type: ignore
import plotly.graph_objects as go
import plotly.express as px
import re
import pandas as pd
import dask.dataframe as dd
import requests
from tqdm import tqdm

# Cargar las variables de entorno desde el archivo .env
load_dotenv("apikeytfm.env")
api_key = os.getenv("apikey")

# Verificar si la clave API se ha cargado correctamente
if api_key:
    openai.api_key = api_key
    st.sidebar.success("Clave API cargada exitosamente.")
else:
    st.sidebar.error("Error: API Key no encontrada. Verifica el archivo .env")

# Título de la aplicación
st.title("💻 DatAI Pro 🤖")

# Inicializar el estado de la sesión para almacenar mensajes, datos y gráficos
if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True
if "data_loaded" not in st.session_state:
    st.session_state.data_loaded = False
if "charts" not in st.session_state:
    st.session_state.charts = []

# Preprocesamiento de datos (solo se ejecuta la primera vez)
    # Verificar si el archivo ya existe
    output_file = './reduced_property_price_datav2.csv'

    if not os.path.exists(output_file):
        print("El archivo no existe. Se procederá a realizar el muestreo estratificado y guardarlo.")

        # Ver cuántos chunks se procesarán
        num_chunks = df_dask.npartitions
        print(f"El archivo se dividirá en {num_chunks} chunks.")

        # Escribir el encabezado solo la primera vez
        df_dask.head(0).to_csv(output_file, mode='w', header=True, index=False)

        # Función para muestreo estratificado
        def stratified_sample(df, frac=40000/28276228):
            return df.groupby(categorical_columns, observed=True, group_keys=False).apply(lambda x: x.sample(frac=frac), meta=df)

        # Procesar cada chunk de datos, aplicar muestreo y guardar incrementalmente
        for i, chunk in enumerate(df_dask.to_delayed()):
            print(f"Procesando chunk {i+1} de {num_chunks}...")
            chunk_df = dd.from_delayed([chunk])  # Convertir cada chunk en un dataframe
            chunk_sampled = stratified_sample(chunk_df)  # Aplicar muestreo estratificado

            # Guardar el chunk muestreado en el archivo CSV (añadir al archivo)
            chunk_sampled.compute().to_csv(output_file, mode='a', header=False, index=False)  # Añadir al archivo existente

        print("Proceso completado, archivo CSV guardado.")
    else:
        print(f"El archivo '{output_file}' ya existe. Se procederá a leer el archivo.")

        # Leer el archivo existente
        df_sampled = pd.read_csv(output_file)

        print(f"El archivo ya existe y ha sido leído correctamente con {len(df_sampled)} filas.")

    # Leer el archivo CSV completo
    df = pd.read_csv(output_file)

    # Asegurarte de que la columna 'Date of Transfer' está en formato datetime
    df['Date of Transfer'] = pd.to_datetime(df['Date of Transfer'])

    # Crear nuevas columnas para "Día", "Mes" y "Año"
    df['Day'] = df['Date of Transfer'].dt.day
    df['Month'] = df['Date of Transfer'].dt.month
    df['Year'] = df['Date of Transfer'].dt.year

    # Contar los valores faltantes (NaN) por cada columna
    missing_values = df.isnull().sum()

    # Mostrar el resultado
    print(missing_values)

    # Lista de columnas que deseas eliminar
    columns_to_drop = ['Transaction unique identifier', 'PAON', 'SAON', 'Street', 'Locality', 'Town/City', 'District', 'Date of Transfer', 'Record Status - monthly file only']

    # Filtrar las columnas que existen en el dataframe
    columns_to_drop_existing = [col for col in columns_to_drop if col in df.columns]

    # Eliminar solo las columnas que existen en el dataframe
    if columns_to_drop_existing:
        df = df.drop(columns=columns_to_drop_existing)
        print(f"Las siguientes columnas se eliminaron: {columns_to_drop_existing}")
    else:
        print("Las columnas ya han sido eliminadas")

    # Calcular los cuartiles y el IQR
    Q1 = df['Price'].quantile(0.25)
    Q3 = df['Price'].quantile(0.75)
    IQR = Q3 - Q1

    # Definir los límites para detectar outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filtrar los outliers
    outliers = df[(df['Price'] < lower_bound) | (df['Price'] > upper_bound)]
    print(f"Total de outliers detectados: {outliers.shape[0]}")

    # Filtrar los datos sin outliers
    data_without_outliers = df[(df['Price'] >= lower_bound) & (df['Price'] <= upper_bound)]

    # Eliminar outliers usando IQR
    data = data_without_outliers.copy()

    current_year = 2024
    data['Property Age'] = current_year - data['Year']
    district_freq = data['County'].value_counts(normalize=True)
    data['County_Frequency'] = data['County'].map(district_freq)

    # Almacenar los datos preprocesados en el estado de la sesión
    st.session_state.data = data
    st.session_state.data_loaded = True

# Mostrar los mensajes almacenados en el estado de la sesión
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mostrar los gráficos almacenados en el estado de la sesión
for i, chart in enumerate(st.session_state.charts):
    st.plotly_chart(chart, key=f'chart_{i}')

# Mostrar el primer mensaje del asistente si es la primera vez que se carga la aplicación
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿cómo puedo ayudarte?")
    st.session_state.messages.append({"role": "assistant", "content": "Hola, ¿cómo puedo ayudarte?"})
    st.session_state.first_message = False

# Manejar la entrada del usuario
if prompt := st.chat_input("Escribe tu pregunta..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Consultar el modelo LLM con la pregunta del usuario
    async def consulta_llm(pregunta):
        try:
            respuesta = await openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                          {"role": "user", "content": pregunta}],
                max_tokens=150
)
            return respuesta.choices[0].message['content'].strip()
        except Exception as e:
            return f"Error al consultar el LLM: {e}"

    # Obtener la respuesta del modelo LLM
    respuesta = asyncio.run(consulta_llm(prompt))

    # Mostrar la respuesta del asistente solo si no se va a graficar
    if not re.search(r"evolución|precio|gráfico|tendencia|distribución|tipo de propiedad|variación|segmentación", respuesta, re.IGNORECASE):
        with st.chat_message("assistant"):
            st.markdown(respuesta)
        st.session_state.messages.append({"role": "assistant", "content": respuesta})

    # Funciones para graficar
    def plot_price_evolution_interactive(df):
        """
        Función para graficar la evolución interactiva del precio promedio de las propiedades a lo largo del tiempo.

        Parámetros:
        df: DataFrame - El conjunto de datos que contiene los precios y el año de transferencia.
        Esta función ayuda a visualizar cómo han cambiado los precios promedio de propiedades a lo largo del tiempo,
        lo cual es útil para identificar tendencias y patrones en el mercado inmobiliario.
        """
        # Agrupar por año y calcular el precio promedio
        data_grouped = df.groupby('Year')['Price'].mean().reset_index()

        # Crear la figura para el gráfico
        fig = go.Figure()

        # Añadir la traza del gráfico de línea
        fig.add_trace(go.Scatter(
            x=data_grouped['Year'],
            y=data_grouped['Price'],
            mode='lines+markers',
            line=dict(color='royalblue', width=2),
            marker=dict(size=6, color='darkblue'),
            name='Precio promedio',
            hovertemplate='%{y:.2f} €<extra></extra>'  # Formato del tooltip
        ))

        # Añadir títulos y detalles del gráfico
        fig.update_layout(
            title="Evolución del Precio Promedio de Propiedades (1995-2023)",
            xaxis_title="Año",
            yaxis_title="Precio Promedio",
            template="plotly_white",
            hovermode="x",
            font=dict(family="Arial", size=12),
            width=900, height=600,
            xaxis=dict(
                tickmode='linear',  # Mostrar cada año como un tick en el eje x
                tick0=1995,  # Año inicial
                dtick=1  # Incremento de un año
            ),
        )

        # Almacenar el gráfico en el estado de la sesión
        st.session_state.charts.append(fig)

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, key=f'chart_{len(st.session_state.charts)}')

    def plot_price_distribution_by_property_type(df):
        """
        Función para graficar la distribución de los precios según el tipo de propiedad de manera más eficiente.

        Parámetros:
        df: DataFrame - El conjunto de datos que contiene los precios y el tipo de propiedad.
        Esta función permite visualizar cómo varían los precios según diferentes tipos de propiedades, lo cual es útil
        para entender la segmentación del mercado y detectar variaciones de precios entre diferentes categorías de propiedades.
        """
        # Crear el gráfico de caja con Plotly Express sin puntos individuales
        fig = px.box(
            df,
            x='Property Type',
            y='Price',
            title='Distribución de Precios según el Tipo de Propiedad',
            labels={'Property Type': 'Tipo de Propiedad', 'Price': 'Precio (€)'},  # Etiquetas más claras
            template="plotly_white"
        )

        # Ajustar el layout y formato del gráfico
        fig.update_layout(
            xaxis_title="Tipo de Propiedad",
            yaxis_title="Precio de Venta (€)",
            font=dict(family="Arial", size=12),
            width=900, height=600,
            yaxis=dict(tickprefix="€")  # Añadir el prefijo del euro al eje y
        )

        # Almacenar el gráfico en el estado de la sesión
        st.session_state.charts.append(fig)

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, key=f'chart_{len(st.session_state.charts)}')

    # Crear el diccionario de funciones y descripciones
    funciones = {
        "Graficar la evolución del precio promedio de propiedades a lo largo del tiempo.": plot_price_evolution_interactive,
        "Graficar la distribución de precios según el tipo de propiedad.": plot_price_distribution_by_property_type,
        "Visualizar las tendencias generales de precios en el mercado a lo largo de los años.": plot_price_evolution_interactive,
        "Mostrar cómo varían los precios entre diferentes tipos de propiedades residenciales y comerciales.": plot_price_distribution_by_property_type
    }

    # Ejecutar la función con base en la respuesta del LLM
    def ejecutar_comando_llm(respuesta, df):
        # Buscar la función que coincida con las palabras clave de la respuesta
        for descripcion, funcion in funciones.items():
            # Buscar coincidencias con palabras clave en la respuesta para determinar qué función ejecutar
            if re.search(r"evolución|precio|gráfico|tendencia", respuesta, re.IGNORECASE) and "evolución" in descripcion:
                funcion(df)
                st.write(f"Ejecutando función: {descripcion}")
                return
            elif re.search(r"distribución|tipo de propiedad|variación|segmentación", respuesta, re.IGNORECASE) and "distribución" in descripcion:
                funcion(df)
                st.write(f"Ejecutando función: {descripcion}")
                return
        # Si no se encuentra una función correspondiente
        st.write("No se encontró una función correspondiente para la respuesta.")

    # Ejecutar el comando basado en la respuesta del LLM
    ejecutar_comando_llm(respuesta, st.session_state.data)
