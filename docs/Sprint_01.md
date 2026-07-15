# Sprint 01 – Configuración Inicial y Visualización del Mapa Base

## Proyecto

**GeoSalta Analytics**

Plataforma Inteligente de Análisis Territorial para la Provincia de Salta.

---

## Versión

**v0.1.0**

---

## Estado

✅ Completado

---

## Fecha

Julio 2026

---

# Objetivo del Sprint

Construir la base del proyecto y visualizar el mapa interactivo de los departamentos de la provincia de Salta mediante Streamlit y Folium.

---

# Objetivos específicos

* Crear la estructura inicial del proyecto.
* Configurar el entorno virtual.
* Inicializar el repositorio Git.
* Crear el repositorio en GitHub.
* Instalar las dependencias necesarias.
* Integrar Streamlit con Folium.
* Cargar el GeoJSON oficial de los departamentos.
* Mostrar el mapa interactivo.
* Visualizar el nombre de cada departamento mediante tooltips.

---

# Tecnologías utilizadas

* Python
* Streamlit
* Folium
* Streamlit-Folium
* GeoJSON
* Git
* GitHub
* Visual Studio Code

---

# Estructura del proyecto

```
GeoSalta-Analytics/

├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
├── data/
│   ├── geojson/
│   └── excel/
│
├── docs/
├── pages/
├── tests/
└── utils/
```

---

# Funcionalidades implementadas

* Configuración del proyecto.
* Integración con Streamlit.
* Integración con Folium.
* Visualización del mapa base.
* Tooltips con el nombre de cada departamento.
* Código organizado mediante módulos.

---

# Archivos creados

* app.py
* utils/mapa.py
* requirements.txt
* README.md
* .gitignore

---

# Dificultades encontradas

### Error de importación

Durante la implementación apareció el siguiente error:

```
ImportError: cannot import name 'crear_mapa'
```

La causa fue que el archivo `mapa.py` no había sido guardado antes de ejecutar la aplicación.

La solución consistió en guardar los cambios y volver a ejecutar Streamlit.

---

# Resultado obtenido

Se obtuvo un mapa interactivo de la provincia de Salta con los 23 departamentos correctamente representados.

Cada departamento muestra su nombre al pasar el cursor.

La aplicación quedó preparada para incorporar nuevas funcionalidades en los siguientes sprints.

---

# Lecciones aprendidas

* Organización modular del código.
* Integración entre Streamlit y Folium.
* Uso de archivos GeoJSON.
* Buenas prácticas de estructura de proyectos.
* Flujo de trabajo con Git y GitHub.

---

# Próximo Sprint

Sprint 02

Objetivos:

* Mejorar la interfaz.
* Incorporar panel lateral.
* Selección de departamentos.
* Efecto Hover.
* Integrar municipios.
* Preparar carga de indicadores.

---

# Estado del proyecto

Versión estable.

**Release:** v0.1.0
