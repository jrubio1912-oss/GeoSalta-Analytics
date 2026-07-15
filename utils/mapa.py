import json
import folium


def crear_mapa():

    # Centro aproximado de la provincia
    mapa = folium.Map(
        location=[-24.8, -65.4],
        zoom_start=7,
        tiles="CartoDB positron"
    )

    # Leer GeoJSON
    with open(
        "data/geojson/salta_departamentos_limpio.geojson",
        encoding="utf-8"
    ) as f:

        departamentos = json.load(f)

    # Estilo
    estilo = {
        "fillColor": "#4CAF50",
        "color": "#1B5E20",
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