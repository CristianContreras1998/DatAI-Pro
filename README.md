🤖 DatAI-Pro 🚀
DatAI-Pro es una aplicación desarrollada en Streamlit que permite cargar datos, preprocesarlos, visualizar gráficos y aplicar modelos de Machine Learning para el análisis de precios de propiedades en el Reino Unido.

📋 Requisitos previos
Python: Asegúrate de tener instalado Python 3.8 o superior. Puedes descargarlo desde python.org.
Clave de API de OpenAI: Necesitarás una clave de API de OpenAI para realizar ciertas funciones en la aplicación. Solicítala al creador de la aplicación y recibirás un archivo .env con la clave ya configurada.
🛠️ Pasos para ejecutar la aplicación en local
Sigue estos pasos para clonar el repositorio, configurar el entorno y ejecutar la aplicación en tu computadora.

1️⃣ Clonar el repositorio
Primero, debes clonar este repositorio en tu máquina local. Para hacerlo:

Abre la terminal o línea de comandos.
Ejecuta el siguiente comando:
bash
Copiar código
git clone https://github.com/CristianContreras1998/DatAI-Pro.git
Cambia al directorio del proyecto:
bash
Copiar código
cd DatAI-Pro
Esto descargará todos los archivos necesarios para la aplicación en tu computadora.

2️⃣ Instalar las dependencias
Una vez que hayas clonado el repositorio, debes instalar las dependencias necesarias. Estas están listadas en el archivo requirements.txt.

Para instalarlas:

Asegúrate de estar en el directorio del proyecto (DatAI-Pro).
Ejecuta el siguiente comando en la terminal:
bash
Copiar código
pip install -r requirements.txt
Esto instalará todas las bibliotecas necesarias, como Streamlit, OpenAI, y otras librerías de Python.

3️⃣ Configurar la clave de API de OpenAI
Para que la aplicación funcione correctamente, es necesario autenticarse con la API de OpenAI.

🔑 Instrucciones para la clave de API:

Solicitar al creador: Solicita el archivo .env con la clave de API al creador de la aplicación.
Ubicación del archivo: Coloca el archivo .env en la carpeta principal del proyecto DatAI-Pro, asegurándote de que esté en el mismo directorio donde se encuentra main.py. Esto permitirá que la aplicación acceda a la clave de API sin configuración adicional.
⚠️ Nota importante: El archivo .env contiene la clave de API de OpenAI, la cual es confidencial. No compartas este archivo ni lo subas a repositorios públicos.

4️⃣ Ejecutar la aplicación
Ahora que todo está configurado, puedes iniciar la aplicación:

En la terminal, asegúrate de estar en el directorio del proyecto.

Ejecuta el siguiente comando:

bash
Copiar código
streamlit run main.py
La aplicación se abrirá automáticamente en tu navegador predeterminado. Si no se abre automáticamente, puedes acceder manualmente ingresando la siguiente dirección en tu navegador:

arduino
Copiar código
http://localhost:8501
5️⃣ Interactuar con la aplicación
Recomendamos empezar con las acciones:

Cargar dataset 📂
Preprocesar Dataset 🛠️
Después de eso, puedes presentar gráficos como:

📊 Visualiza cómo afectó la crisis de 2008 al mercado inmobiliario.
📈 Muestra la estacionalidad de ventas a lo largo del año.
🏠 Muestra la evolución de precios para propiedades nuevas y antiguas.
Para aplicar modelos de Machine Learning, actualmente están disponibles:

Regresión Lineal
Random Forest
XGBoost
LightGBM
CatBoost
ℹ️ Notas adicionales
Si tienes problemas para instalar las dependencias o ejecutar la aplicación, verifica que tengas la versión correcta de Python y que las bibliotecas hayan sido instaladas correctamente.
La clave de API de OpenAI es esencial para que funcionen ciertas funciones de la aplicación, así que asegúrate de que esté bien configurada en el archivo .env.
Esta guía proporciona todos los detalles para que puedas configurar y ejecutar la aplicación sin problemas. Si necesitas más ayuda, no dudes en pedírmela.
