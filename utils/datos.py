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