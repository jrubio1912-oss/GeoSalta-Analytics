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

## Flujo de datos

```
GeoJSON
        │
        ▼
 mapa.py
        │
        ▼
 Folium
        │
        ▼
 Streamlit
```

Posteriormente se incorporará la lectura de archivos Excel para representar indicadores sobre el mapa.
