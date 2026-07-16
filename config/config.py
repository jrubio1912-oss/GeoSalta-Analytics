"""
Configuración general de GeoSalta Analytics
"""

from pathlib import Path

# =====================================================
# RUTAS DEL PROYECTO
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"

PROCESSED_DIR = DATA_DIR / "processed"

OUTPUTS_DIR = DATA_DIR / "outputs"

GEOJSON_DIR = RAW_DIR / "geojson"

EXCEL_DIR = RAW_DIR / "excel"

# =====================================================
# ARCHIVOS
# =====================================================

GEOJSON_DEPARTAMENTOS = GEOJSON_DIR / "salta_departamentos_limpio.geojson"

GEOJSON_MUNICIPIOS = GEOJSON_DIR / "salta_municipios_limpio.geojson"

# =====================================================
# APLICACIÓN
# =====================================================

APP_TITLE = "GeoSalta Analytics"

APP_SUBTITLE = "Plataforma Inteligente de Análisis Territorial"

# =====================================================
# MAPA
# =====================================================

MAP_CENTER = [-24.8, -65.4]

MAP_ZOOM = 7

MAP_HEIGHT = 700

MAP_WIDTH = None

MAP_TILES = "CartoDB positron"

# =====================================================
# COLORES
# =====================================================

COLOR_PRIMARY = "#2E7D32"

COLOR_BORDER = "#1B5E20"

COLOR_HOVER = "#43A047"

COLOR_BACKGROUND = "#F5F7FA"