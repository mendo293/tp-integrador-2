class Satelite:
    def __init__(self, nombre, norad_cat_id, latitud, longitud, altitud):
        if not nombre or not nombre.strip():
            raise ValueError("Nombre vacío")
        if not isinstance(norad_cat_id, int):
            raise ValueError("ID de catálogo debe ser int")
        if not (-90 <= latitud <= 90):
            raise ValueError("Latitud fuera de rango")
        if not (-180 <= longitud <= 180):
            raise ValueError("Longitud fuera de rango")
        if altitud < 100:
            raise ValueError("Altitud menor a 100 km")

        self.nombre = nombre.strip()
        self.norad_cat_id = norad_cat_id
        self.latitud = float(latitud)
        self.longitud = float(longitud)
        self.altitud = float(altitud)

    def tipo_orbita(self):
        if self.altitud < 2000:
            return "LEO"
        if self.altitud < 34000:
            return "MEO"
        if self.altitud <= 37000:
            return "GEO"
        return "HEO"

    def __str__(self):
        return f"{self.nombre} | {self.norad_cat_id} | {self.tipo_orbita()} | {self.altitud} km"

    def en_zona(self, lon_min, lat_min, lon_max, lat_max):
        return lon_min <= self.longitud <= lon_max and lat_min <= self.latitud <= lat_max