import os
from dotenv import load_dotenv
import openai
from function_description import function_descriptions

# Cargar la clave de API
load_dotenv("apikey.env")
API_KEY = os.environ.get("OPENAI_API_KEY")

# Depuración: Verificar si la clave se cargó correctamente
if API_KEY is None:
    print("Error: No se encontró la clave de API.")
else:
    print("Clave de API cargada:", API_KEY)

# Configurar la clave de API directamente en openai
openai.api_key = API_KEY

def identificar_funcion_avanzada(pregunta_usuario):
    opciones = list(function_descriptions.keys())
    prompt = (
        "A continuación se presentan diferentes funciones para analizar datos de propiedades inmobiliarias. "
        "Devuelve solo el nombre exacto de la función que mejor se ajuste a la solicitud del usuario. "
        "Las funciones disponibles son:\n"
    )
    for funcion, info in function_descriptions.items():
        prompt += f"- {funcion}:\n  Descripción: {info['description']}\n  Ejemplos: {', '.join(info['examples'])}\n\n"
    
    prompt += f"El usuario ha solicitado: '{pregunta_usuario}'\n"
    prompt += f"Por favor, responde solo con uno de estos nombres de función exactos: {', '.join(opciones)}."

    try:
        # Nueva llamada a la API usando el cliente instanciado
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
            temperature=0
        )
        funcion_recomendada = response.choices[0].message.content.strip()
        print(f"GPT-3.5-turbo sugiere la función: {funcion_recomendada}")

        # Extraer el nombre exacto de la función si viene con más texto
        for key in opciones:
            if key.lower() in funcion_recomendada.lower():
                return key
        return None

    except Exception as e:
        print(f"Error al identificar función: {e}")
        return None
