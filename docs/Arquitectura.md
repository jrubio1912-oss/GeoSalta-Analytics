# Arquitectura de GeoSalta Analytics

## Objetivo

Desarrollar una plataforma web para el análisis territorial de la provincia de Salta, permitiendo visualizar indicadores geográficos mediante mapas interactivos y dashboards.

---

## Arquitectura

La aplicación sigue una arquitectura modular basada en separación de responsabilidades.

```
Usuario
      │
      ▼
 Streamlit (Interfaz)
      │
      ▼
Utilidades (utils)
      │
      ├── mapa.py
      ├── datos.py
      ├── indicadores.py
      ├── estilos.py
      └── sidebar.py
      │
      ▼
Datos

GeoJSON

Excel

CSV
```

---

## Tecnologías

* Python
* Streamlit
* Folium
* Pandas
* GeoPandas
* Plotly

---

## Principios del proyecto

* Código modular.
* Escalabilidad.
* Reutilización.
* Simplicidad.
* Buenas prácticas.
* Documentación continua.

---

## Organización

Cada módulo tendrá una única responsabilidad.

### app.py

Punto de entrada de la aplicación.

### mapa.py

Creación y configuración del mapa.

### datos.py

Lectura y transformación de datos.

### indicadores.py

Cálculo de indicadores.

### estilos.py

Definición de estilos visuales.

### sidebar.py

Construcción del menú lateral.

---

## Flujo de información

```
Usuario

     │
     ▼

Mapa Interactivo (Folium)

     │
     ▼

streamlit-folium

     │
     ▼

Session State

     │
     ▼

Panel de Información

     │
     ▼

Datos (GeoJSON)

     │
     ▼

Interfaz actualizada
```

Posteriormente se incorporará la lectura de archivos Excel para representar indicadores sobre el mapa.


## Estructura del proyecto

```
GeoSalta-Analytics/
│
├── app.py
│
├── components/
│   ├── header.py
│   ├── sidebar.py
│   └── panel.py
│
├── config/
│   └── config.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── geojson/
│
├── docs/
│
├── utils/
│   ├── mapa.py
│   ├── datos.py
│   ├── estilos.py
│   └── indicadores.py
│
└── assets/
```


## Evolución prevista

En las próximas versiones se incorporarán nuevas fuentes de datos para ampliar las capacidades analíticas de la plataforma.

```
GeoJSON
      │
Excel
      │
CSV
      │
SQLite
      │
PostgreSQL + PostGIS (futuro)
```

Esta arquitectura permitirá incorporar indicadores demográficos, económicos, financieros y sociales sin modificar la estructura principal de la aplicación.
