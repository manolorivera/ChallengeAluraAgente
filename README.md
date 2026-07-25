# ChallengeAluraAgente

Caso : Santos Pegasus Soluciones 

# Descripcion

Empresa de tecnología especializada en el desarrollo de software escalable bajo arquitectura de microservicios y soluciones de Inteligencia Artificial (RAG). Se destaca por sus rigurosos estándares técnicos en ingeniería back-end y front-end, garantizando excelencia operativa y seguridad en infraestructuras de nube (OCI).

Proyecto ha cotemplado los sigueintes procesos

- Carga de base de conocimientos
  - 1_ManualNuevosDesarrolladores.pdf
  - 2_GuiaBackEnd.pdf
  - 3_GuiaFrontEnd.pdf
  - 4_ProtocoloIncidentes.pdf
  - 5_ArquitecturaMicroservicios.pdf

- Agente  para la consulta de datos en base a la informacion de la base de conocimientos cargada

## Objetivo del proyecto

Aplicar los conocimientos de CURSOS TECH de Alura Latam adquiridos del 02/06/2026 al 22/07/2026 

## Instalacion 

Crea y activa el entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate
```


Actualización de librerías

```bash
#Actualizamos PIP, la cual permite descargar nuevas librerías
python.exe -m pip install --upgrade pip

#Actualizamos WHEEL, la cual permite instalar las librerías pre-compiladas
python.exe -m pip install --upgrade wheel

#Actualizamos PACKING, la cual permite resolver dependencias compatibles entre librerías
python.exe -m pip install --upgrade packaging

#Actualizamos SETUPTOOLS, la cual permite instalar las librerías
!pip install --upgrade setuptools

#Librería para enviar credenciales de manera segura
python.exe -m pip install azure-identity
```

Instalación de librerías
```bash
#Librería para implementar la arquitectura RAG
python.exe -m pip install langchain

#Librería con utilitarios comunes para proyectos de I.A. Generativa
python.exe -m pip install langchain-community

#Librería con más utilitarios de langchain
python.exe -m pip install langchain-core

#Librerías de langchain para que funcione con Azure
python.exe -m pip install langchain-azure-ai

#Librería para enviar credenciales de manera segura
python.exe -m pip install azure-identity

#Librería para manipulación de PDFs
python.exe -m pip install pypdf

#Librería para manipulación del servicio de Azure AI Search
python.exe -m pip install azure-search-documents
```

## Tecnologías utilizadas
- Python 3.12+
- langchain
- Azure AI
- pypdf
- uuid
- dotenv

## Estructura general
```text
src/ Código fuente del proyecto
data/ Documentos fuentes para la base de conocimientos
doc/ Documentación de la evidencia del proyecto
```
