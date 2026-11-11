import json
from satelite import Satelite
from catalogo import cargar_registros, crear_catalogo, resumir_por_tipo_orbita, obtener_satelites_en_zona

REGISTRO_EJEMPLO = {
    "OBJECT_NAME": "ISS (ZARYA)",
    "OBJECT_ID": "1998-067A",
    "EPOCH": "2026-10-14T08:06:39.057984",
    "MEAN_MOTION": 15.48861773,
    "ECCENTRICITY": 0.00067245,
    "INCLINATION": 51.6325,
    "RA_OF_ASC_NODE": 200.0,
    "ARG_OF_PERICENTER": 100.0,
    "MEAN_ANOMALY": 50.0,
    "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U",
    "NORAD_CAT_ID": 25544,
    "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 10000,
    "BSTAR": 0.0001,
    "MEAN_MOTION_DOT": 0.00001,
    "MEAN_MOTION_DDOT": 0.0
}

def test_cargar_registros(tmp_path):
    archivo = tmp_path / "prueba.json"
    datos = [REGISTRO_EJEMPLO]
    archivo.write_text(json.dumps(datos))

    res = cargar_registros(str(archivo))
    assert res == datos

def test_crear_catalogo():
    datos = [REGISTRO_EJEMPLO]
    catalogo = crear_catalogo(datos)
    assert len(catalogo) == 1
    assert catalogo[0].nombre == "ISS (ZARYA)"
    assert catalogo[0].norad_cat_id == 25544

def test_resumir_por_tipo_orbita():
    lista = [
        Satelite("Sat1", 1, 0, 0, 400),
        Satelite("Sat2", 2, 0, 0, 600),
        Satelite("Sat3", 3, 0, 0, 35000)
    ]
    resumen = resumir_por_tipo_orbita(lista)
    assert resumen["LEO"]["cantidad"] == 2
    assert resumen["LEO"]["min_altitud"] == 400
    assert resumen["LEO"]["max_altitud"] == 600
    assert resumen["LEO"]["promedio_altitud"] == 500.0
    assert resumen["GEO"]["cantidad"] == 1

def test_obtener_satelites_en_zona():
    lista = [
        Satelite("Sat1", 1, -41.0, -71.0, 500),
        Satelite("Sat2", 2, 0.0, 0.0, 500)
    ]
    en_zona = obtener_satelites_en_zona(lista, -76.3, -46.13, -66.3, -36.13)
    assert len(en_zona) == 1
    assert en_zona[0].nombre == "Sat1"