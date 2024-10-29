# visualization.py

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import warnings
import matplotlib.ticker as mtick
import pandas as pd
import zipfile
import requests
import os
import folium
from folium.plugins import HeatMap
import streamlit as st
from streamlit_folium import st_folium

warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")

def plot_histogram_price_outliers(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Price'], kde=True, color='blue', ax=ax)
    ax.set_title('Distribución de Precios sin outliers')
    ax.set_xlabel('Precio')
    ax.set_ylabel('Frecuencia')
    return fig

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

        # Mostrar el gráfico en Streamlit
        return fig

def plot_price_distribution_by_property_type(df):
    fig = px.box(df, x='Property Type', y='Price', title='Distribución de Precios según el Tipo de Propiedad', template="plotly_white")
    fig.update_layout(xaxis_title="Tipo de Propiedad", yaxis_title="Precio de Venta (€)")
    return fig


def plot_price_trends_by_property_type(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Year', y='Price', hue='Property Type', data=df, ax=ax)
    ax.set_title('Tendencias de precios a lo largo del tiempo para cada tipo de propiedad')
    ax.set_xlabel('Año')
    ax.set_ylabel('Precio')
    return fig


def plot_price_distribution_by_county(df, top_n=10):
    top_county = df['County'].value_counts().nlargest(top_n).index
    df_filtered = df[df['County'].isin(top_county)]
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='County', y='Price', data=df_filtered, palette="Set3", ax=ax)
    ax.set_title(f'Distribución de precios por los {top_n} condados más representativos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig


def plot_new_vs_old_property_prices(df):
    """
    Función para graficar la comparativa interactiva de precios entre propiedades nuevas y de segunda mano.

    Parámetros:
    - df: DataFrame - El conjunto de datos que contiene los precios y la categoría (nueva o de segunda mano).
    """
    fig = px.box(df, x='Old/New', y='Price', title='Comparativa de Precios entre Propiedades Nuevas y de Segunda Mano', template="plotly_white", color='Old/New')
    fig.update_layout(xaxis_title="Tipo de Propiedad", yaxis_title="Precio (€)")
    st.plotly_chart(fig)


def plot_price_evolution_new_vs_old(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Year', y='Price', hue='Old/New', data=df, ax=ax)
    ax.set_title('Evolución de los precios de propiedades nuevas vs. de segunda mano')
    ax.set_xlabel('Año')
    ax.set_ylabel('Precio')
    return fig


def plot_sales_frequency_by_property_and_county(df, top_n_county=10):
    """
    Función para graficar la frecuencia de ventas según el tipo de propiedad en los condados más relevantes.
    """
    top_county = df['County'].value_counts().nlargest(top_n_county).index
    df_filtered = df[df['County'].isin(top_county)]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Property Type', data=df_filtered, hue='Property Type', palette="Set3", ax=ax, legend=False)  # Usando hue y legend=False
    ax.set_title(f'Frecuencia de ventas según el tipo de propiedad en los {top_n_county} condados más frecuentes')
    plt.xticks(rotation=90)
    return fig


def plot_price_vs_property_age_violin(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='Old/New', y='Price', data=df, palette="Set2", hue='Old/New', ax=ax)
    ax.set_title('Relación entre el precio y la antigüedad de la propiedad')
    return fig


def plot_transactions_per_year(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Year', data=df, ax=ax)
    ax.set_title('Número de transacciones por año')
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de transacciones')
    plt.xticks(rotation=45, ha='right')
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}K'))
    return fig


def plot_sales_trends_by_property_type_line(df):
    df_grouped = df.groupby(['Year', 'Property Type'], as_index=False).size().rename(columns={'size': 'Sales'})
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='Year', y='Sales', hue='Property Type', data=df_grouped, marker="o", ax=ax)
    ax.set_title('Tendencias de ventas según el tipo de propiedad')
    return fig


def plot_sales_per_month_heatmap(df, selected_years=None):
    if selected_years:
        df = df[df['Year'].isin(selected_years)]
    df_grouped = df.groupby(['Year', 'Month']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df_grouped, cmap="YlGnBu", annot=True, fmt='d', linewidths=.5, ax=ax)
    ax.set_title('Número de ventas por mes a lo largo de los años (Heatmap)')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Año')
    return fig


def plot_crisis_impact(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Year', y='Price', data=df, linewidth=2, color='blue', ax=ax)
    ax.axvline(x=2008, color='red', linestyle='--', label='Crisis 2008')
    ax.set_title('Impacto de la crisis financiera de 2008 en los precios de venta', fontsize=16)
    ax.set_xlabel('Año', fontsize=12)
    ax.set_ylabel('Precio (en €)', fontsize=12)
    plt.xticks(rotation=45)
    ax.legend(loc='upper left')
    plt.tight_layout()
    return fig


def plot_seasonality_with_rotated_month_names(df):
    month_names = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Month', data=df, palette="Blues_d", ax=ax)
    
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=10, color='black')

    avg = df['Month'].value_counts().mean()
    ax.axhline(y=avg, color='red', linestyle='--', label=f'Promedio: {int(avg)}')
    ax.set_title('Estacionalidad en las transacciones a lo largo del año', fontsize=16)
    ax.set_xlabel('Mes', fontsize=12)
    ax.set_ylabel('Número de transacciones', fontsize=12)
    ax.set_xticks(range(12))
    ax.set_xticklabels(month_names, rotation=45, ha='right')
    ax.legend(loc='upper right')
    plt.tight_layout()
    return fig


def create_price_heatmap_from_zip(df, csv_path='GB_full.txt'):
    """
    Descarga un archivo ZIP con coordenadas, lo extrae, une los datos de coordenadas con el DataFrame de precios,
    calcula la media de precios por código postal y genera un mapa de calor basado en la distribución de precios.

    Parámetros:
    - df: DataFrame - Datos de propiedades que contienen precios y códigos postales.
    - csv_path (str): Ruta para el archivo descomprimido.
    
    Retorna:
    - folium.Map: Mapa de calor generado.
    """
    try:
        # Cargar el archivo descomprimido como DataFrame
        coordinates_data = pd.read_csv(csv_path, sep='\t', header=None, 
                                       names=['Zone', 'Postcode', 'Town', 'Region', 'Country_Code', 
                                              'County', 'County2', 'AdminDistrict', 'AdminDistrictCode', 
                                              'Latitude', 'Longitude', 'Precision'],
                                       dtype={'County2': str, 'AdminDistrict': str})
    except FileNotFoundError:
        print(f"Error: El archivo '{csv_path}' no se encuentra.")
        return None
    except pd.errors.ParserError:
        print(f"Error: El archivo '{csv_path}' no se pudo leer. Verifica el formato.")
        return None
    
    # Unir el dataset de propiedades con las coordenadas y calcular la media de precios por código postal
    if 'Postcode' not in df.columns or 'Price' not in df.columns:
        print("Error: El DataFrame debe contener las columnas 'Postcode' y 'Price'.")
        return None

    data_merged = pd.merge(df, coordinates_data[['Postcode', 'Latitude', 'Longitude']], on='Postcode', how='left')
    media_precios_postal = data_merged.groupby('Postcode').agg(
        {'Price': 'mean', 'Latitude': 'first', 'Longitude': 'first'}).reset_index()
    media_precios_postal_clean = media_precios_postal.dropna(subset=['Latitude', 'Longitude'])

    if media_precios_postal_clean.empty:
        print("Error: No se encontraron datos para generar el mapa de calor.")
        return None

    # Generar el mapa de calor
    mapa = folium.Map(location=[54.0, -2.0], zoom_start=6)
    heat_data = [[row['Latitude'], row['Longitude'], row['Price']] for index, row in media_precios_postal_clean.iterrows()]
    HeatMap(heat_data, radius=15).add_to(mapa)
    
    st_folium(mapa, width=800)

