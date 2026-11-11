from datetime import datetime, timezone

from skyfield.api import EarthSatellite, load, wgs84

FECHA_REFERENCIA = datetime(2026, 10, 19, 12, 0, tzinfo=timezone.utc)

_escala = load.timescale()


def obtener_posicion(registro, momento=FECHA_REFERENCIA):
    if momento.tzinfo is None:
        momento = momento.replace(tzinfo=timezone.utc)

    satelite = EarthSatellite.from_omm(_escala, registro)
    posicion = wgs84.subpoint(satelite.at(_escala.from_datetime(momento)))

    return (
        round(float(posicion.latitude.degrees), 4),
        round(float(posicion.longitude.degrees), 4),
        round(float(posicion.elevation.km), 3),
    )
