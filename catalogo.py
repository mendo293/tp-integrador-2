import json
from satelite import Satelite
from funciones_base import obtener_posicion

def cargar_registros(ruta):
    with open(ruta, "r") as f:
        return json.load(f)

def crear_catalogo(registros):
    catalogo = []
    for reg in registros:
        try:
            lat, lon, alt = obtener_posicion(reg)
            sat = Satelite(reg.get("OBJECT_NAME"), reg.get("NORAD_CAT_ID"), lat, lon, alt)
            catalogo.append(sat)
        except (ValueError, TypeError, KeyError):
            continue
    return catalogo

def resumir_por_tipo_orbita(catalogo):
    resumen = {}
    for sat in catalogo:
        tipo = sat.tipo_orbita()
        if tipo not in resumen:
            resumen[tipo] = {"cantidad": 0, "min_altitud": sat.altitud, "max_altitud": sat.altitud, "suma": 0.0}
        
        datos = resumen[tipo]
        datos["cantidad"] += 1
        datos["suma"] += sat.altitud
        datos["min_altitud"] = min(datos["min_altitud"], sat.altitud)
        datos["max_altitud"] = max(datos["max_altitud"], sat.altitud)

    for datos in resumen.values():
        datos["promedio_altitud"] = round(datos.pop("suma") / datos["cantidad"], 2)

    return resumen

def obtener_satelites_en_zona(catalogo, lon_min, lat_min, lon_max, lat_max):
    return [sat for sat in catalogo if sat.en_zona(lon_min, lat_min, lon_max, lat_max)]