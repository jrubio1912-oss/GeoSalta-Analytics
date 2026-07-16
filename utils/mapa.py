import json
import folium
from config.config import *

def crear_mapa():

    # Centro aproximado de la provincia
    mapa = folium.Map(
        location=MAP_CENTER,
        zoom_start=MAP_ZOOM,
        tiles=MAP_TILES
    )

    # Leer GeoJSON
    with open(
        GEOJSON_DEPARTAMENTOS,
        encoding="utf-8"
    ) as f:

        departamentos = json.load(f)

    # Estilo
    estilo = {
    "fillColor": COLOR_PRIMARY,
    "color": COLOR_BORDER,
    "weight": 2,
    "fillOpacity": 0.5,
    }

    folium.GeoJson(
        departamentos,
        name="Departamentos",
        style_function=lambda x: estilo,
        tooltip=folium.GeoJsonTooltip(
            fields=["nombre"],
            aliases=["Departamento:"]
        ),
    ).add_to(mapa)

    return mapa