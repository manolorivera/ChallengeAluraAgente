#Utilitario de conexión a Azure OpenAI Foundry
from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
#Utilitario para crear la memoria a corto plazo del modelo
from langchain_core.chat_history import InMemoryChatMessageHistory
#Utilitario para definir reglas de "personalidad" en el modelo
from langchain_core.messages import SystemMessage
#Utilitario para enviar mensajes más complejos
from langchain_core.messages import HumanMessage

#Utilitario para conectarnos a bases de conocimiento
from langchain_community.retrievers import AzureAISearchRetriever

import os
from dotenv import load_dotenv

load_dotenv()

#----------------------------------------------------------------------------------------------------------------------------------------
# Obtiene el modelo con el que trabajamos
#----------------------------------------------------------------------------------------------------------------------------------------
def obtenerModelo():
    #Conexión a un modelo
    llm = AzureAIOpenAIApiChatModel(
        endpoint = os.environ.get("CONF_AZURE_AI_FOUNDRY_ENDPOINT"),
        credential = os.environ.get("CONF_AZURE_AI_FOUNDRY_KEY"),
        model = os.environ.get("CONF_AZURE_AI_FOUNDRY_MODEL")
    )
    return llm

#----------------------------------------------------------------------------------------------------------------------------------------
#Crea la memoria a corto plazo, con un contexto
#----------------------------------------------------------------------------------------------------------------------------------------
def crearMemoriaCortoPlazo(contexto = None):
    #Definimos el mensaje del sistema
    mensajeDelSistema = SystemMessage(content = contexto)
    #Creamos la memoria a corto plazo
    memoriaCortoPlazo = InMemoryChatMessageHistory()
    #Agregamos la personalidad en la memoria a corto plazo
    memoriaCortoPlazo.add_message(mensajeDelSistema)
    return memoriaCortoPlazo

#----------------------------------------------------------------------------------------------------------------------------------------
# Envia un mensaje al modelo
#----------------------------------------------------------------------------------------------------------------------------------------
def enviarMensajeAlModelo(llm=None,memoriaCortoPlazo=None,mensaje=None):
    #Construmos el JSON del mensaje
    mensajeHumano = HumanMessage(
    content=[
            {
                "type": "text",
                "text": mensaje
            }
        ]
    )
    #Agregamos el mensaje del ser humano
    memoriaCortoPlazo.add_user_message(mensajeHumano)
    #Envíamos el mensaje
    respuesta = llm.invoke(memoriaCortoPlazo.messages)
    #Guardamos en la memoria a corto plazo la respuesta de la IA
    memoriaCortoPlazo.add_ai_message(respuesta)
    return respuesta.content


#----------------------------------------------------------------------------------------------------------------------------------------
# Agrega el contexto al mensaje del usuario, desde una base de conocimiento
#----------------------------------------------------------------------------------------------------------------------------------------
def mensajeConContextoDesdeBaseDeConocimiento(mensaje=None):
    #Conexión a una base de conocimientos
    baseDeConocimiento = AzureAISearchRetriever(
        service_name = os.environ.get("CONF_AZURE_AI_SEARCH_NAME"),
        api_key = os.environ.get("CONF_AZURE_AI_SEARCH_KEY"),
        index_name = os.environ.get("CONF_AZURE_AI_SEARCH_BASE_DE_CONOCIMIENTO"),
        content_key = "content",
        top_k = 3
    )
    #Hacemos una búsqueda
    respuestaRag = baseDeConocimiento.invoke(mensaje)
    #Variable que acumula todos los chunks de textos
    resultadoDeBusqueda = ""
    #Acumulamos todos los chunks
    for chunk in respuestaRag:
        resultadoDeBusqueda = resultadoDeBusqueda + chunk.page_content + "\n"

    #Definimos el mensaje con contexto
    mensajeConContexto = f"""
        Usa los siguientes fragmentos de contexto para responder la pregunta.
        Si no encuentras la respuesta en el contexto, di que no lo sabes.
        
        Contexto:
        {resultadoDeBusqueda}
        
        Pregunta:
        {mensaje}
    """
    return mensajeConContexto

#----------------------------------------------------------------------------------------------------------------------------------------
# Envia un mensaje al modelo
#----------------------------------------------------------------------------------------------------------------------------------------
def enviarMensajeAlModeloConContextoDeBaseDeConocimiento(llm=None,memoriaCortoPlazo=None,mensaje=None):
    #Definimos el mensaje por enviar
    mensajePorEnviar = mensajeConContextoDesdeBaseDeConocimiento(mensaje)
    #Construmos el JSON del mensaje
    mensajeHumano = HumanMessage(
        content=[
            {
                "type": "text",
                "text": mensajePorEnviar
            }
        ]
    )
    #Agregamos el mensaje del ser humano
    memoriaCortoPlazo.add_user_message(mensajeHumano)
    #Envíamos el mensaje
    respuesta = llm.invoke(memoriaCortoPlazo.messages)
    #Guardamos en la memoria a corto plazo la respuesta de la IA
    memoriaCortoPlazo.add_ai_message(respuesta)
    return respuesta.content
