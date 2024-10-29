import pandas as pd
import streamlit as st

def cargar_datos(file_path='./UK_Property_Price_Data_1995-2023_Reduced.csv'):
    """
    Carga el archivo CSV desde la ruta especificada.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.write(f"Error: El archivo '{file_path}' no se encuentra.")
        return None
    except pd.errors.ParserError:
        st.write(f"Error: El archivo '{file_path}' no se pudo leer. Verifica el formato.")
        return None

def preprocesar_datos(df):
    """
    Realiza el preprocesamiento de los datos, incluyendo la limpieza de datos,
    creación de nuevas columnas y eliminación de outliers.
    """
    # Verificar la existencia de columnas requeridas antes de procesar
    required_columns = ['Date of Transfer', 'Price', 'County']
    for col in required_columns:
        if col not in df.columns:
            st.write(f"Error: '{col}' no se encuentra en el DataFrame.")
            return None

    # Convertir 'Date of Transfer' a datetime
    df['Date of Transfer'] = pd.to_datetime(df['Date of Transfer'])

    # Crear nuevas columnas para "Día", "Mes" y "Año"
    df['Day'] = df['Date of Transfer'].dt.day
    df['Month'] = df['Date of Transfer'].dt.month
    df['Year'] = df['Date of Transfer'].dt.year

    # Eliminar las columnas especificadas si existen en el DataFrame
    columns_to_drop = ['Transaction unique identifier', 'PAON', 'SAON', 'Street', 'Locality', 'Town/City', 'District', 'Date of Transfer', 'Record Status - monthly file only']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Identificar y eliminar outliers en la columna 'Price'
    Q1 = df['Price'].quantile(0.25)
    Q3 = df['Price'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df['Price'] >= lower_bound) & (df['Price'] <= upper_bound)]

    # Calcular la antigüedad y la frecuencia del condado
    current_year = pd.Timestamp.now().year
    df['Property Age'] = current_year - df['Year']
    county_freq = df['County'].value_counts(normalize=True)
    df['County_Frequency'] = df['County'].map(county_freq)

    return df