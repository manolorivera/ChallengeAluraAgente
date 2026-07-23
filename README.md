# ChallengeAluraAgente

Challenge Alura Agente | Caso : BimBam Buy E-commerce 

# Descripcion del caso : BimBam Buy

E-commerce multiplataforma enfocado en la experiencia de compra digital ágil y segura. Se destaca por un modelo de negocio orientado al cliente, con políticas robustas de reembolso, un programa de afiliados dinámico y una infraestructura logística optimizada para garantizar entregas rápidas y soporte constante al usuário final.

Proyecto ha cotemplado los sigueintes procesos
- Carga de base de conocimientos
  - Carga de 5 archivos PDFs
- CharBot para la consulta de datos en base a la informacion de la base de conocimientos cargada

## Objetivo del proyecto

Aplicar los conocimientos de CURSOS TECH de Alura Latam adquiridos del 02/06/2026 al 22/07/2026 

## Instalacion 

Crea y activa el entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Instalacion de dependencias:

```bash
#Actualizamos PIP, la cual permite descargar nuevas librerías
pip install --upgrade pip

#Actualizamos WHEEL, la cual permite instalar las librerías pre-compiladas
pip install --upgrade wheel

#Actualizamos PACKING, la cual permite resolver dependencias compatibles entre librerías
pip install --upgrade packaging

#Actualizamos SETUPTOOLS, la cual permite instalar las librerías
pip install --upgrade setuptools

#Librería para implementar la arquitectura RAG
pip install langchain

#Librería con utilitarios comunes para proyectos de I.A. Generativa
pip install langchain-community

#Librería con más utilitarios de langchain
pip install langchain-core

#Librerías de langchain para que funcione con Azure
#pip install langchain-azure-ai

#Librería para enviar credenciales de manera segura
pip install azure-identity

#Librería para cortar documentos
pip install langchain-text-splitters

#Librería para manipulación del servicio de Azure AI Search
pip install azure-search-documents

#Librería para manipulación de PDFs
pip install pypdf

## Tecnologías utilizadas

- Python 3.12+
- Azure AI
- uuid
- pypdf


## Estructura general
```text
src/ Código fuente del proyecto
data_bdc/ Documentos fuentes para la base de conocimientos
scripts/ Scripts ejecutables
evidencia/ Documentación de la evidencia del proyecto
```


