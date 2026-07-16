# Sprint 02 – Arquitectura e Identidad Visual

## Proyecto

**GeoSalta Analytics**

Plataforma Inteligente de Análisis Territorial para la Provincia de Salta.

---

## Versión

**v0.2.0**

---

## Estado

✅ Completado

---

## Fecha

Julio 2026

---

# Objetivo del Sprint

Transformar la aplicación inicial en una plataforma modular, escalable y preparada para incorporar nuevas funcionalidades de análisis territorial.

---

# Objetivos específicos

- Mejorar la interfaz de usuario.
- Incorporar un tema visual propio.
- Modularizar la aplicación.
- Centralizar la configuración.
- Reorganizar la estructura del proyecto.
- Preparar la aplicación para trabajar con datos dinámicos.

---

# Tecnologías utilizadas

- Python
- Streamlit
- Folium
- Pathlib
- CSS
- Git
- GitHub
- Visual Studio Code

---

# Funcionalidades implementadas

## Interfaz

- Header profesional.
- Sidebar con filtros.
- Panel de información.
- Layout responsivo.

---

## Estilos

- Archivo CSS independiente.
- Colores institucionales.
- Mejora del aspecto visual.

---

## Arquitectura

Se creó una arquitectura modular basada en componentes.

```
components/

header.py

sidebar.py

panel.py
```

---

## Configuración

Se creó el módulo:

```
config/config.py
```

donde se centralizó:

- rutas
- colores
- configuración del mapa
- títulos de la aplicación

---

## Organización de datos

Se reorganizó la carpeta de datos siguiendo buenas prácticas de proyectos de análisis de datos.

```
data/

raw/
    excel/
    geojson/

processed/

outputs/
```

---

## Uso de pathlib

Se reemplazaron rutas fijas por objetos `Path`, permitiendo compatibilidad entre distintos sistemas operativos.

---

# Archivos creados

- config/config.py
- assets/styles.css
- components/header.py
- components/sidebar.py
- components/panel.py

---

# Resultado obtenido

La aplicación quedó preparada para crecer sin necesidad de reorganizar nuevamente la estructura del proyecto.

La interfaz presenta una organización modular y una identidad visual propia.

---

# Lecciones aprendidas

- Modularización de aplicaciones Streamlit.
- Organización profesional de proyectos Python.
- Centralización de configuración.
- Uso de pathlib.
- Buenas prácticas de arquitectura.

---

# Próximo Sprint

Sprint 03

Objetivos:

- Crear el módulo de datos.
- Leer automáticamente los GeoJSON.
- Obtener departamentos.
- Obtener municipios.
- Conectar los datos con la interfaz.

---

# Estado del proyecto

Versión estable.

**Release:** v0.2.0