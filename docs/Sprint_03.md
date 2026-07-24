# Sprint 3 - Interactividad y Navegación Territorial

## Información General

**Proyecto:** GeoSalta Analytics

**Sprint:** 03

**Estado:** Finalizado ✅

---

# Objetivo

Transformar el mapa de departamentos de Salta en una aplicación interactiva, permitiendo que la selección de un departamento actualice automáticamente la información mostrada en el panel lateral.

El objetivo principal fue comenzar a convertir el mapa en el eje central de navegación de la aplicación.

---

# Funcionalidades implementadas

## 1. Lectura dinámica de datos territoriales

Se desarrolló un módulo para leer automáticamente los archivos GeoJSON de departamentos y municipios.

### Resultado

- Eliminación de datos estáticos.
- Lectura automática de GeoJSON.
- Centralización del acceso a datos en un único módulo.

Archivos involucrados:

- `utils/datos.py`

---

## 2. Sidebar dinámico

El panel lateral ahora obtiene la información directamente desde los archivos GeoJSON.

Se implementó:

- listado automático de departamentos
- filtrado automático de municipios según el departamento seleccionado

Esto permite que cualquier modificación futura del GeoJSON sea reflejada automáticamente en la aplicación.

---

## 3. Captura de eventos del mapa

Se incorporó la detección de clics sobre los departamentos utilizando **streamlit-folium**.

Cuando el usuario selecciona un departamento, la aplicación obtiene automáticamente la información contenida en el GeoJSON.

Información capturada:

- nombre del departamento
- cabecera
- código
- identificador
- número de departamento

---

## 4. Panel dinámico de información

El panel lateral dejó de contener información fija y ahora muestra los datos correspondientes al departamento seleccionado.

Actualmente se visualiza:

- Departamento
- Cabecera departamental
- Cantidad de municipios
- Listado de municipios

---

## 5. Gestión del estado de la aplicación

Se incorporó `st.session_state` para mantener la selección del usuario entre las diferentes ejecuciones de Streamlit.

Esto permitió conservar el departamento seleccionado durante la navegación.

---

# Arquitectura implementada

```
Usuario

        │

        ▼

Mapa Interactivo (Folium)

        │

        ▼

Evento de selección

        │

        ▼

Session State

        │

        ▼

Panel de información

        │

        ▼

Datos territoriales
```

---

# Archivos modificados

```
app.py

components/
    header.py
    sidebar.py
    panel.py

utils/
    datos.py
    mapa.py

config/
    config.py
```

---

# Problemas encontrados

Durante el desarrollo del Sprint se resolvieron los siguientes inconvenientes:

- diferencias entre los nombres de departamentos en los GeoJSON
- importación de módulos
- organización del proyecto
- captura de eventos de Folium
- actualización del mapa tras la selección
- utilización de Session State
- errores de sintaxis durante la modularización

Todos los inconvenientes fueron solucionados satisfactoriamente.

---

# Lecciones aprendidas

Durante este Sprint se incorporaron nuevos conocimientos sobre:

- arquitectura modular en Streamlit
- lectura de archivos GeoJSON
- gestión de estado mediante Session State
- interacción entre Streamlit y Folium
- organización de componentes reutilizables
- separación entre interfaz, lógica de negocio y acceso a datos

---

# Resultado obtenido

Al finalizar el Sprint 3 se dispone de una aplicación capaz de:

- visualizar el mapa interactivo de los departamentos de Salta
- detectar el departamento seleccionado mediante un clic
- actualizar automáticamente el panel de información
- mostrar la cabecera del departamento
- listar los municipios correspondientes
- mantener el estado de la selección durante la navegación

GeoSalta Analytics deja de ser un mapa estático y pasa a convertirse en una aplicación interactiva orientada al análisis territorial.

---

# Estado del proyecto

| Sprint | Estado |
|---------|--------|
| Sprint 1 | ✅ Finalizado |
| Sprint 2 | ✅ Finalizado |
| Sprint 3 | ✅ Finalizado |

---

# Próximo Sprint

## Sprint 4 - Base de Datos Territorial

Objetivos principales:

- integrar datos oficiales desde Excel
- incorporar población por departamento
- incorporar superficie
- calcular indicadores territoriales
- preparar la estructura para nuevos datasets
- comenzar el desarrollo del dashboard analítico

---

# Conclusión

El Sprint 3 representa un punto de inflexión en el desarrollo de GeoSalta Analytics.

Se logró integrar el mapa, la lógica de negocio y la interfaz de usuario en un único flujo de navegación, estableciendo una arquitectura sólida que permitirá incorporar indicadores, gráficos y análisis territoriales en los próximos sprints.

A partir de este Sprint, el mapa se convierte en el principal mecanismo de interacción de la aplicación, sentando las bases para la evolución hacia una plataforma de inteligencia territorial para la provincia de Salta.