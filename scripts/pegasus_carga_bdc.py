from langchain_community.document_loaders import PyPDFLoader #Utilitario para leer PDFs
from langchain_text_splitters import CharacterTextSplitter #Utilitario para recortar el documento
from azure.core.credentials import AzureKeyCredential #Utilitario para enviar de manera segura contraseñas
from azure.search.documents import SearchClient #Utilitario para conectarnos al servicio de AI Search
import uuid #Librería para generar identificadores únicos
import os
from dotenv import load_dotenv
load_dotenv()
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Carga un archivo en una base de conocimiento
#------------------------------------------------------------------------------------------------------------------------------------------------------
def cargarArchivo(rutaDeArchivo = None, nombreDeBaseDeConocimiento = None):
  #Creamos el lector que leerá el documento
  lector = PyPDFLoader(rutaDeArchivo)
  #Leemos el documento
  documento = lector.load()
  #Definimos cómo se crearán los chunks del texto
  cortadorDeTexto = CharacterTextSplitter(
      separator = "\n", #Enter
      chunk_size = 1000,  #Tamaño de cada fragmento
      chunk_overlap = 100  #Superposición entre fragmentos
  )
  #Creamos los chunks
  chunks = cortadorDeTexto.split_documents(documento)
  #Lo convertimos a STRING
  id = str(uuid.uuid4())
  #Información del documento que se almacena
  chunksConIdentificadores = []
  #Iteramos los chunks para darle la estructura
  for chunk in chunks:
    #Definimos la estructura del chunk que insertaremos con su identificador
    estructuraDeChunk = {
        "id": str(uuid.uuid4()),
        "content": chunk.page_content
    }
    #Lo agregamos al array
    chunksConIdentificadores.append(estructuraDeChunk)

  #Nos conectamos a la base de conocimiento
  baseDeConocimiento = SearchClient(
        os.environ.get("CONF_AZURE_AI_SEARCH_ENDPOINT"),
        os.environ.get("CONF_AZURE_AI_SEARCH_BASE_DE_CONOCIMIENTO"),
        AzureKeyCredential(os.environ.get("CONF_AZURE_AI_SEARCH_KEY"))
  )
  #Insertamos los chunks en la base de conocimiento
  resultadosDeInserciones = baseDeConocimiento.upload_documents(chunksConIdentificadores)
  return resultadosDeInserciones

#------------------------------------------------------------------------------------------------------------------------------------------------------
# Proceso de cargamos archivos PDF
#------------------------------------------------------------------------------------------------------------------------------------------------------
resultado1 =  cargarArchivo(
  rutaDeArchivo =  "e:/Cursos/ONE_Tech_Builder/ChallengeAluraAgente/data/1_ManualNuevosDesarrolladores.pdf" , 
  nombreDeBaseDeConocimiento = os.environ.get("CONF_AZURE_AI_SEARCH_BASE_DE_CONOCIMIENTO")
)
resultado2 =  cargarArchivo(
  rutaDeArchivo =  "e:/Cursos/ONE_Tech_Builder/ChallengeAluraAgente/data/2_GuiaBackEnd.pdf" , 
  nombreDeBaseDeConocimiento = os.environ.get("CONF_AZURE_AI_SEARCH_BASE_DE_CONOCIMIENTO")
)
resultado3 =  cargarArchivo(
  rutaDeArchivo =  "e:/Cursos/ONE_Tech_Builder/ChallengeAluraAgente/data/3_GuiaFrontEnd.pdf" , 
  nombreDeBaseDeConocimiento = os.environ.get("CONF_AZURE_AI_SEARCH_BASE_DE_CONOCIMIENTO")
)
resultado4 =  cargarArchivo(
  rutaDeArchivo =  "e:/Cursos/ONE_Tech_Builder/ChallengeAluraAgente/data/4_ProtocoloIncidentes.pdf" , 
  nombreDeBaseDeConocimiento = os.environ.get("CONF_AZURE_AI_SEARCH_BASE_DE_CONOCIMIENTO")
)
resultado5 =  cargarArchivo(
  rutaDeArchivo =  "e:/Cursos/ONE_Tech_Builder/ChallengeAluraAgente/data/5_ArquitecturaMicroservicios.pdf" , 
  nombreDeBaseDeConocimiento = os.environ.get("CONF_AZURE_AI_SEARCH_BASE_DE_CONOCIMIENTO")
)
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)