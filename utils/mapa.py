import json
import folium
from config.config import *


def crear_mapa(departamento_seleccionado=None):

    # Centro aproximado de la provincia
    mapa = folium.Map(
        location=MAP_CENTER,
        zoom_start=MAP_ZOOM,
        tiles=MAP_TILES
    )

    # Leer GeoJSON
    with open(GEOJSON_DEPARTAMENTOS, encoding="utf-8") as f:
        departamentos = json.load(f)

    # Función de estilo
    def estilo_departamento(feature):

        nombre = feature["properties"]["nombre"].title()

        if (
            departamento_seleccionado
            and nombre == departamento_seleccionado
        ):

            return {
                "fillColor": "#1B5E20",
                "color": "#0D3D14",
                "weight": 3,
                "fillOpacity": 0.9,
            }

        return {
            "fillColor": COLOR_PRIMARY,
            "color": COLOR_BORDER,
            "weight": 2,
            "fillOpacity": 0.5,
        }

    folium.GeoJson(
        departamentos,
        name="Departamentos",
        style_function=estilo_departamento,
        tooltip=folium.GeoJsonTooltip(
            fields=["nombre"],
            aliases=["Departamento:"]
        ),
    ).add_to(mapa)

    return mapa