# main.py
import streamlit as st
import matplotlib.pyplot as plt
from openai_integration import identificar_funcion_avanzada
from function_description import function_descriptions
from preprocessing import cargar_datos, preprocesar_datos
from visualization import (
    plot_histogram_price_outliers,
    plot_price_evolution_interactive,
    plot_price_distribution_by_property_type,
    plot_price_trends_by_property_type,
    plot_price_distribution_by_county,
    plot_new_vs_old_property_prices,
    plot_price_evolution_new_vs_old,
    plot_sales_frequency_by_property_and_county,
    plot_price_vs_property_age_violin,
    plot_transactions_per_year,
    plot_sales_trends_by_property_type_line,
    plot_sales_per_month_heatmap,
    plot_crisis_impact,
    plot_seasonality_with_rotated_month_names,
    create_price_heatmap_from_zip,
)
from machine_learning import (
    preparar_datos_para_modelos,
    entrenar_regresion_lineal,
    entrenar_random_forest,
    entrenar_xgboost,
    entrenar_lightgbm,
    entrenar_catboost,
)

# Inicialización
st.title("📊 DatAI Pro 💻")
if "messages" not in st.session_state:
    st.session_state.messages = []
if "df" not in st.session_state:
    st.session_state.df = None

# Mensaje de bienvenida
if not st.session_state.messages:
    st.session_state.messages.append({"role": "assistant", "content": "¡Bienvenido a DatAI Pro 🤖! Estaré encantado de ayudarte en lo que necesites. Para comenzar con el análisis, debes cargar el dataset."})

# Mostrar el historial de mensajes con emojis y estilos diferenciados
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").markdown(f"**Usuario:**\n{message['content']}")
    elif message["role"] == "assistant":
        st.chat_message("assistant").markdown(f"**Asistente:**\n{message['content']}")
    elif message["role"] == "plotly_chart" and message["content"] is not None:
        st.plotly_chart(message["content"])
    elif message["role"] == "matplotlib_chart" and message["content"] is not None:
        st.pyplot(message["content"])

# Procesar entrada de usuario
if prompt := st.chat_input("Escribe tu solicitud..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)
    
    # Inicialización del mensaje de respuesta
    response_message = "No se encontró una función correspondiente. Asegúrate de utilizar términos relacionados con las opciones disponibles."

    # Identificación de la función
    funcion = identificar_funcion_avanzada(prompt)
    print(f"Función devuelta después de verificación: {funcion}")

    # Ejecutar la función si existe
    if funcion:
        if funcion == "cargar_datos":
            df = cargar_datos()
            if df is not None:
                st.session_state.df = df
                response_message = "Datos cargados con éxito."
            else:
                response_message = "Error al cargar los datos."
        elif funcion == "preprocesar_datos" and st.session_state.df is not None:
            st.session_state.df = preprocesar_datos(st.session_state.df)
            response_message = "Datos preprocesados con éxito."
        elif funcion == "plot_histogram_price_outliers" and st.session_state.df is not None:
            fig = plot_histogram_price_outliers(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando histograma de precios."
        elif funcion == "plot_price_evolution_interactive" and st.session_state.df is not None:
            fig = plot_price_evolution_interactive(st.session_state.df)
            if fig:
                st.plotly_chart(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "plotly_chart", "content": fig})
            response_message = "Mostrando gráfico interactivo de evolución de precios."
        elif funcion == "plot_price_distribution_by_property_type" and st.session_state.df is not None:
            fig = plot_price_distribution_by_property_type(st.session_state.df)
            if fig:
                st.plotly_chart(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "plotly_chart", "content": fig})
            response_message = "Mostrando distribución de precios por tipo de propiedad."
        elif funcion == "plot_price_trends_by_property_type" and st.session_state.df is not None:
            fig = plot_price_trends_by_property_type(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando tendencias de precios por tipo de propiedad."
        elif funcion == "plot_price_distribution_by_county" and st.session_state.df is not None:
            fig = plot_price_distribution_by_county(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando distribución de precios por condado."
        elif funcion == "plot_new_vs_old_property_prices" and st.session_state.df is not None:
            fig = plot_new_vs_old_property_prices(st.session_state.df)
            if fig:
                st.plotly_chart(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "plotly_chart", "content": fig})
            response_message = "Mostrando comparativa de precios entre propiedades nuevas y de segunda mano."
        elif funcion == "plot_price_evolution_new_vs_old" and st.session_state.df is not None:
            fig = plot_price_evolution_new_vs_old(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando evolución de precios de propiedades nuevas vs. de segunda mano."
        elif funcion == "plot_sales_frequency_by_property_and_county" and st.session_state.df is not None:
            fig = plot_sales_frequency_by_property_and_county(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando frecuencia de ventas según tipo de propiedad y condado."
        elif funcion == "plot_price_vs_property_age_violin" and st.session_state.df is not None:
            fig = plot_price_vs_property_age_violin(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando relación entre precio y antigüedad de la propiedad."
        elif funcion == "plot_transactions_per_year" and st.session_state.df is not None:
            fig = plot_transactions_per_year(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando número de transacciones por año."
        elif funcion == "plot_sales_trends_by_property_type_line" and st.session_state.df is not None:
            fig = plot_sales_trends_by_property_type_line(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando tendencias de ventas según tipo de propiedad."
        elif funcion == "plot_sales_per_month_heatmap" and st.session_state.df is not None:
            fig = plot_sales_per_month_heatmap(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando ventas por mes (heatmap)."
        elif funcion == "plot_crisis_impact" and st.session_state.df is not None:
            fig = plot_crisis_impact(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando impacto de la crisis financiera de 2008 en los precios."
        elif funcion == "plot_seasonality_with_rotated_month_names" and st.session_state.df is not None:
            fig = plot_seasonality_with_rotated_month_names(st.session_state.df)
            if fig:
                st.pyplot(fig)  # Mostrar inmediatamente
                st.session_state.messages.append({"role": "matplotlib_chart", "content": fig})
            response_message = "Mostrando estacionalidad en las transacciones a lo largo del año."
        elif funcion == "create_price_heatmap_from_zip" and st.session_state.df is not None:
            create_price_heatmap_from_zip(st.session_state.df)  # Se mostrará directamente sin almacenar en st.session_state.messages
            response_message = "Mostrando mapa de calor de precios."
        elif funcion in ["entrenar_regresion_lineal", "entrenar_random_forest", "entrenar_xgboost", "entrenar_lightgbm", "entrenar_catboost"]:
            X_train, X_test, y_train, y_test = preparar_datos_para_modelos(st.session_state.df)
            if funcion == "entrenar_regresion_lineal":
                mse, r2 = entrenar_regresion_lineal(X_train, X_test, y_train, y_test)
            elif funcion == "entrenar_random_forest":
                mse, r2 = entrenar_random_forest(X_train, X_test, y_train, y_test)
            elif funcion == "entrenar_xgboost":
                mse, r2 = entrenar_xgboost(X_train, X_test, y_train, y_test)
            elif funcion == "entrenar_lightgbm":
                mse, r2 = entrenar_lightgbm(X_train, X_test, y_train, y_test)
            elif funcion == "entrenar_catboost":
                mse, r2 = entrenar_catboost(X_train, X_test, y_train, y_test)
            response_message = f"Modelo entrenado con éxito. MSE: {mse}, R²: {r2}"

    # Agregar el mensaje de respuesta a la sesión
    st.session_state.messages.append({"role": "assistant", "content": response_message})
    st.chat_message("assistant").markdown(response_message)
