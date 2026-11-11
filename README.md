# Trabajo Práctico Integrador 2: Seguimiento de Satélites
  
**Materia:** Programación 1 - UNRN   Comision 3 - Ingenieria en Telecomunicaciones.
**Estudiante:** Alan Michael Mendoza Ruffin
**Docente:** Lautaro Yamil Linquiman Ventura

## Descripción
Programa de línea de comandos para procesar un archivo JSON con satélites activos, obtener su posición y realizar consultas por tipo de órbita o por coordenadas geográficas.

## Configuración del entorno

Crear el ambiente virtual:
```bash
python -m venv .venv
```
Instalar las dependencias:

```bash
pip install -r requirements.txt
```
## Ejecución de consultas

Resumen por tipo de órbita:

```bash
python consultar_satelites.py datos/satelites.json resumen
```
Consulta por zona geográfica (ejemplo de Bariloche):

```bash
python consultar_satelites.py datos/satelites.json zona -76.30 -46.13 -66.30 -36.13
```

## Ejecución de pruebas

Correr las pruebas unitarias:

```bash
pytest
```

Verificar el porcentaje de cobertura:

```bash
pytest --cov=. --cov-report=html
```