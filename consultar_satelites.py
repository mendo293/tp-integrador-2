import sys
from catalogo import cargar_registros, crear_catalogo, resumir_por_tipo_orbita, obtener_satelites_en_zona

def main():
    if len(sys.argv) < 3:
        print("Uso: python consultar_satelites.py <archivo.json> <resumen / zona> [coordenadas]")
        return

    registros = cargar_registros(sys.argv[1])
    catalogo = crear_catalogo(registros)
    comando = sys.argv[2]

    if comando == "resumen":
        resumen = resumir_por_tipo_orbita(catalogo)
        for tipo in ["LEO", "MEO", "GEO", "HEO"]:
            if tipo in resumen:
                d = resumen[tipo]
                print(f"Órbita {tipo}: Cantidad: {d['cantidad']} | Mín: {d['min_altitud']} | Máx: {d['max_altitud']} | Prom: {d['promedio_altitud']}")

    elif comando == "zona":
        coords = [float(x) for x in sys.argv[3:7]]
        encontrados = obtener_satelites_en_zona(catalogo, *coords)
        print(f"Satélites en zona: {len(encontrados)}")
        for sat in encontrados:
            print(sat)

if __name__ == "__main__":
    main()