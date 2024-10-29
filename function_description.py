function_descriptions = {
    "cargar_datos": {
        "description": "Esta función carga el conjunto de datos completo de precios de propiedades desde un archivo CSV y lo coloca en un DataFrame de pandas. Este paso es necesario antes de cualquier análisis o preprocesamiento, ya que permite trabajar con los datos originales tal como fueron almacenados. Sin cargar el dataset, no se pueden realizar otras operaciones como limpieza, visualización o modelado.",
        "examples": [
            "Cargar los datos de precios de propiedades", 
            "Importar el dataset desde el archivo CSV", 
            "Abrir y traer los datos desde el archivo para iniciar el análisis", 
            "Carga el archivo CSV de propiedades", 
            "Quiero empezar el análisis, trae el dataset", 
            "Carga el archivo de datos completo"
        ]
    },
    "preprocesar_datos": {
        "description": "Esta función realiza un preprocesamiento detallado de los datos cargados, lo que incluye limpieza, normalización, eliminación de outliers y creación de nuevas columnas para mejorar el análisis posterior. El preprocesamiento es crucial para asegurar la calidad de los datos antes de generar visualizaciones o construir modelos predictivos. Se centra en ajustar los datos para que estén listos para análisis avanzados y visualizaciones.",
        "examples": [
            "Limpia los datos para el análisis", 
            "Prepara el dataset eliminando valores extremos y ajustando columnas", 
            "Normaliza y elimina outliers en el conjunto de datos", 
            "Preprocesa el archivo para que esté listo para el análisis", 
            "Aplica el preprocesamiento necesario para limpiar el dataset", 
            "Quiero eliminar valores atípicos y preparar los datos"
        ]
    },
    "preparar_datos_para_modelos": {
    "description": "Esta función prepara los datos para entrenar modelos de machine learning, aplicando encoding a variables categóricas, normalización de variables numéricas y dividiendo el dataset en conjuntos de entrenamiento y prueba. Este paso es esencial para garantizar que los datos estén listos para modelar de manera eficiente.",
    "examples": [
        "Prepara los datos para entrenar modelos de machine learning",
        "Divide los datos en entrenamiento y prueba para el análisis",
        "Aplica encoding y normalización a las características del dataset",
        "Ajusta los datos para usarlos en modelos predictivos",
        "Configura los datos para un modelo de machine learning",
        "Organiza el dataset para aplicar machine learning"
        ]
    },
    "plot_histogram_price_outliers": {
        "description": "Esta función genera un histograma detallado de la distribución de precios de propiedades, lo que permite visualizar la frecuencia de los precios y detectar outliers en los datos. Este gráfico es útil para entender la dispersión de los precios y para identificar posibles anomalías que puedan distorsionar el análisis, como valores extremadamente altos o bajos.",
        "examples": [
            "Genera un histograma para ver la distribución de los precios de las propiedades", 
            "Muestra un gráfico de precios para detectar valores atípicos", 
            "Quiero ver un histograma de los precios para identificar outliers", 
            "Haz un gráfico de distribución de precios", 
            "Visualiza un histograma de la frecuencia de precios de propiedades", 
            "Enséñame un gráfico que muestre los precios y los outliers"
        ]
    },
    "plot_price_evolution_interactive": {
        "description": "Esta función crea un gráfico interactivo que muestra cómo ha evolucionado el precio promedio de propiedades a lo largo de los años. El gráfico permite explorar tendencias de largo plazo y observar variaciones en los precios que pueden estar relacionadas con factores económicos. La interactividad del gráfico permite profundizar en períodos específicos o analizar variaciones estacionales.",
        "examples": [
            "Genera un gráfico interactivo para ver la evolución de precios a lo largo del tiempo", 
            "Muestra cómo han cambiado los precios año tras año", 
            "Quiero ver la tendencia de precios de propiedades con un gráfico de evolución", 
            "Crea un gráfico que muestre la evolución temporal de los precios", 
            "Muestra el cambio de los precios de propiedades a lo largo de los años", 
            "Quiero ver un gráfico interactivo de la evolución del precio promedio"
        ]
    },
    "plot_price_distribution_by_property_type": {
        "description": "Esta función genera un gráfico de caja o box plot que muestra cómo varían los precios de propiedades según el tipo de propiedad, como residencial, comercial, etc. Este gráfico ayuda a comprender cómo se distribuyen los precios dentro de cada categoría de propiedad, permitiendo comparaciones directas entre tipos de propiedades y detectando posibles diferencias de precio significativas.",
        "examples": [
            "Genera un gráfico que compare los precios por tipo de propiedad", 
            "Muestra cómo varían los precios entre propiedades residenciales y comerciales", 
            "Quiero ver la distribución de precios para diferentes tipos de propiedades", 
            "Visualiza la dispersión de precios según el tipo de propiedad", 
            "Haz un boxplot para comparar precios por categoría de propiedad", 
            "Comparar los precios de propiedades por su tipo con un gráfico"
        ]
    },
    "entrenar_regresion_lineal": {
        "description": "Esta función entrena un modelo de regresión lineal para predecir los precios de propiedades utilizando las características del dataset. La regresión lineal es un modelo sencillo que asume una relación lineal entre las variables de entrada y el precio. Se utiliza como modelo base para establecer un punto de comparación con modelos más avanzados y determinar la relación directa entre las variables independientes y el precio.",
        "examples": [
            "Entrena un modelo de regresión lineal para predecir precios de propiedades", 
            "Quiero usar regresión lineal para hacer predicciones de precios", 
            "Construye un modelo lineal para predecir el valor de las propiedades", 
            "Aplicar regresión lineal para el análisis de precios de propiedades", 
            "Haz un modelo de regresión lineal sobre el dataset de precios", 
            "Predecir precios utilizando un modelo de regresión lineal"
        ]
    },
    "entrenar_random_forest": {
        "description": "Esta función entrena un modelo de Random Forest para predecir los precios de propiedades. Random Forest es un modelo de ensamble que utiliza múltiples árboles de decisión para mejorar la precisión y reducir el riesgo de sobreajuste. Es útil para capturar relaciones complejas entre las variables del dataset y es más robusto que los modelos lineales simples.",
        "examples": [
            "Entrena un modelo Random Forest para predicción de precios de propiedades", 
            "Quiero usar Random Forest para predecir los valores de propiedades", 
            "Construye un modelo Random Forest para estimar el precio de las propiedades", 
            "Usa Random Forest para analizar precios de propiedades", 
            "Aplica un modelo de Random Forest para el dataset de precios", 
            "Haz predicciones con un modelo de Random Forest"
        ]
    },
    "entrenar_xgboost": {
        "description": "Esta función entrena un modelo XGBoost para predecir los precios de propiedades. XGBoost es un modelo avanzado de boosting que suele obtener buenos resultados en problemas de regresión y clasificación con grandes volúmenes de datos. Es eficiente y escalable, y su capacidad para manejar relaciones complejas lo hace muy preciso para tareas de predicción de precios.",
        "examples": [
            "Entrena un modelo XGBoost para predecir precios de propiedades", 
            "Usa XGBoost para hacer predicciones de precios de propiedades", 
            "Quiero aplicar XGBoost para analizar los precios de propiedades", 
            "Construye un modelo XGBoost para estimar precios de propiedades", 
            "Aplica XGBoost para hacer una predicción de precios", 
            "Predecir valores de propiedades con XGBoost"
        ]
    },
    "entrenar_lightgbm": {
        "description": "Esta función entrena un modelo LightGBM para predecir precios de propiedades. LightGBM es un modelo de boosting optimizado para velocidad y eficiencia, especialmente útil para conjuntos de datos grandes. Su enfoque en estructuras de árbol lo hace ideal para capturar relaciones no lineales en los datos, ofreciendo predicciones precisas en un tiempo reducido.",
        "examples": [
            "Entrena un modelo LightGBM para predecir precios de propiedades", 
            "Utiliza LightGBM para analizar precios de propiedades", 
            "Haz predicciones de precios usando un modelo LightGBM", 
            "Quiero entrenar LightGBM para predecir los precios de propiedades", 
            "Aplica LightGBM para estimar valores de propiedades", 
            "Predecir precios de propiedades con LightGBM"
        ]
    },
    "entrenar_catboost": {
        "description": "Esta función entrena un modelo CatBoost para predecir precios de propiedades. CatBoost está diseñado para manejar datos categóricos de manera eficaz y suele ofrecer buenas precisiones sin necesidad de un preprocesamiento extenso. Es útil para conjuntos de datos mixtos y puede ofrecer un rendimiento rápido y preciso, aprovechando las características categóricas en el dataset.",
        "examples": [
            "Entrena un modelo CatBoost para predecir precios de propiedades", 
            "Quiero utilizar CatBoost para hacer predicciones de precios", 
            "Haz un modelo CatBoost para estimar los valores de propiedades", 
            "Aplica CatBoost para predecir precios en el dataset", 
            "Utiliza CatBoost para el análisis de precios de propiedades", 
            "Predecir precios de propiedades usando CatBoost"
        ]
    },
    "plot_price_trends_by_property_type": {
        "description": "Genera un gráfico de líneas que muestra la tendencia de precios a lo largo del tiempo para cada tipo de propiedad. Esto ayuda a analizar cómo han evolucionado los precios en función del tipo de propiedad y permite comparar su comportamiento en el tiempo.",
        "examples": [
            "Muestra la tendencia de precios por tipo de propiedad",
            "Visualiza cómo cambian los precios con el tiempo según el tipo de propiedad",
            "Quiero ver un gráfico de precios a lo largo del tiempo para cada tipo de propiedad",
            "Genera un gráfico de evolución de precios por tipo de propiedad"
        ]
    },
    "plot_price_distribution_by_county": {
        "description": "Muestra la distribución de precios en los condados más representativos mediante un gráfico de caja, permitiendo observar las variaciones de precios en diferentes ubicaciones.",
        "examples": [
            "Visualiza la distribución de precios por condado",
            "Genera un gráfico de caja para ver los precios por los condados principales",
            "Quiero ver cómo varían los precios en diferentes condados",
            "Haz un boxplot de precios para los condados más comunes"
        ]
    },
    "plot_new_vs_old_property_prices": {
        "description": "Crea un gráfico interactivo comparativo de los precios de propiedades nuevas y de segunda mano, útil para analizar diferencias de precio entre ambos tipos de propiedad.",
        "examples": [
            "Comparar precios de propiedades nuevas y de segunda mano",
            "Muestra un gráfico de precios para propiedades nuevas y usadas",
            "Visualiza los precios de propiedades nuevas vs. antiguas",
            "Haz un gráfico comparativo de propiedades nuevas y de segunda mano"
        ]
    },
    "plot_price_evolution_new_vs_old": {
        "description": "Genera un gráfico que muestra la evolución de los precios de propiedades nuevas y de segunda mano a lo largo del tiempo, ideal para analizar cómo han cambiado sus valores relativos.",
        "examples": [
            "Muestra la evolución de precios para propiedades nuevas y antiguas",
            "Visualiza cómo cambian los precios de propiedades nuevas y usadas",
            "Quiero ver un gráfico de la evolución de propiedades nuevas vs. antiguas",
            "Genera un gráfico de precios de propiedades nuevas y de segunda mano a lo largo del tiempo"
        ]
    },
    "plot_sales_frequency_by_property_and_county": {
        "description": "Muestra la frecuencia de ventas por tipo de propiedad en los condados más representativos, lo cual permite identificar las ubicaciones con mayor volumen de ventas y las propiedades más populares.",
        "examples": [
            "Visualiza la frecuencia de ventas por tipo de propiedad y condado",
            "Muestra un gráfico de ventas de propiedades por condado y tipo",
            "Genera un gráfico de ventas por tipo de propiedad en los condados principales",
            "Quiero ver la frecuencia de ventas de propiedades en diferentes condados"
        ]
    },
    "plot_price_vs_property_age_violin": {
        "description": "Genera un gráfico de violín para analizar la relación entre el precio de la propiedad y su antigüedad, mostrando cómo varían los precios en propiedades nuevas y usadas.",
        "examples": [
            "   ",
            "Genera un gráfico de violín para ver la relación entre antigüedad y precio",
            "Quiero ver cómo afecta la antigüedad al precio de las propiedades",
            "Haz un gráfico de violín de precios y antigüedad de propiedades"
        ]
    },
    "plot_transactions_per_year": {
        "description": "Muestra un gráfico del número de transacciones por año, útil para observar tendencias en el volumen de ventas anuales.",
        "examples": [
            "Visualiza el número de transacciones de propiedades por año",
            "Muestra un gráfico de la cantidad de ventas anuales",
            "Quiero ver las transacciones de propiedades año a año",
            "Genera un gráfico de la frecuencia de transacciones por año"
        ]
    },
    "plot_sales_trends_by_property_type_line": {
        "description": "Genera un gráfico de líneas que muestra las tendencias de ventas por tipo de propiedad, lo que permite ver cómo ha cambiado la popularidad de cada tipo a lo largo del tiempo.",
        "examples": [
            "Visualiza la tendencia de ventas por tipo de propiedad",
            "Muestra un gráfico de líneas de ventas de propiedades según su tipo",
            "Quiero ver cómo cambian las ventas de propiedades según el tipo",
            "Genera un gráfico de ventas por tipo de propiedad en el tiempo"
        ]
    },
    "plot_sales_per_month_heatmap": {
        "description": "Crea un mapa de calor para mostrar el número de ventas por mes a lo largo de los años, permitiendo identificar patrones de estacionalidad en las transacciones.",
        "examples": [
            "Muestra un heatmap de ventas mensuales a lo largo de los años",
            "Visualiza la frecuencia de ventas por mes",
            "Quiero ver un mapa de calor de ventas mensuales",
            "Genera un heatmap de ventas para cada mes y año"
        ]
    },
    "plot_crisis_impact": {
        "description": "Genera un gráfico que muestra el impacto de la crisis financiera de 2008 en los precios de las propiedades, útil para evaluar el efecto de eventos económicos en el mercado inmobiliario.",
        "examples": [
            "Muestra el impacto de la crisis financiera en los precios de propiedades",
            "Visualiza cómo afectó la crisis de 2008 al mercado inmobiliario",
            "Quiero ver un gráfico de precios durante la crisis",
            "Genera un gráfico de precios destacando el impacto de la crisis de 2008"
        ]
    },
    "plot_seasonality_with_rotated_month_names": {
        "description": "Genera un gráfico de barras que muestra la estacionalidad en las transacciones de propiedades a lo largo del año con nombres de meses rotados, ideal para detectar patrones estacionales.",
        "examples": [
            "Muestra la estacionalidad de ventas a lo largo del año",
            "Visualiza un gráfico con los meses rotados para ver ventas mensuales",
            "Quiero ver la frecuencia de ventas por cada mes del año",
            "Genera un gráfico de transacciones mensuales de propiedades"
        ]
    },
    "create_price_heatmap_from_zip": {
        "description": "Crea un mapa de calor de precios de propiedades a partir de datos de coordenadas en un archivo ZIP, mostrando la distribución geográfica de los precios promedio por código postal.",
        "examples": [
            "Genera un mapa de calor de precios usando datos geográficos",
            "Muestra la distribución de precios por ubicación en un mapa",
            "Quiero ver un mapa de calor de precios promedio por código postal",
            "Crea un heatmap de precios de propiedades usando coordenadas"
        ]
    }  
}
