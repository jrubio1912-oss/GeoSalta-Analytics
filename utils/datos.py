import json

from config.config import GEOJSON_DEPARTAMENTOS, GEOJSON_MUNICIPIOS


def leer_departamentos():
    """
    Lee el GeoJSON de departamentos.
    """

    with open(GEOJSON_DEPARTAMENTOS, encoding="utf-8") as archivo:
        return json.load(archivo)


def leer_municipios():
    """
    Lee el GeoJSON de municipios.
    """

    with open(GEOJSON_MUNICIPIOS, encoding="utf-8") as archivo:
        return json.load(archivo)
    

def obtener_lista_departamentos():
    """
    Devuelve una lista ordenada de departamentos.
    """

    geojson = leer_departamentos()

    departamentos = []

    for feature in geojson["features"]:

        nombre = feature["properties"]["nombre"]

        departamentos.append(nombre)

    departamentos.sort()

    return departamentos


def obtener_lista_municipios():
    """
    Devuelve una lista ordenada de todos los municipios.
    """

    geojson = leer_municipios()

    municipios = []

    for feature in geojson["features"]:

        nombre = feature["properties"]["nombre"]

        municipios.append(nombre)

    municipios = sorted(set(municipios))

    return municipios


def obtener_municipios_por_departamento(nombre_departamento):
    """
    Devuelve la lista de municipios de un departamento.
    """

    if nombre_departamento == "Todos":
        return obtener_lista_municipios()

    geojson = leer_municipios()

    municipios = []

    for feature in geojson["features"]:

        propiedades = feature["properties"]

        departamento = propiedades["departamento"]
        municipio = propiedades["nombre"]

        if departamento.upper() == nombre_departamento.upper():
            municipios.append(municipio.title())

    return sorted(set(municipios))