# Fuente de `costa_paises_bajos_s2_20240812_reflectancia.tif`

- **Producto:** Sentinel‑2B Level‑2A, reflectancia de superficie.
- **Escena:** [`S2B_T31UET_20240812T105014_L2A`](https://earth-search.aws.element84.com/v1/collections/sentinel-2-c1-l2a/items/S2B_T31UET_20240812T105014_L2A), adquirida el 12 de agosto de 2024.
- **Catálogo:** [Earth Search de Element 84](https://earth-search.aws.element84.com/v1/), colección `sentinel-2-c1-l2a`.
- **Bandas del recorte:** B02 azul, B03 verde, B04 rojo y B08 infrarrojo cercano; 10 m por píxel.
- **Área:** la misma extensión cartográfica de la muestra costera de la clase 2, 1001 × 1001 píxeles en EPSG:32631. Las fechas y los productos son distintos.
- **Atribución:** *Contains modified Copernicus Sentinel data 2024.* [Condiciones de uso de Sentinel](https://dataspace.copernicus.eu/terms-and-conditions).

## Preparación para la demostración

Se recortaron las cuatro bandas de la misma escena y grilla. Los valores de cada banda se convirtieron a reflectancia de superficie mediante `reflectancia = DN × 0,0001 − 0,1`, según la escala y el offset de los activos de esta colección. Se reproyectó la clasificación de escena SCL de 20 m a la grilla de 10 m con vecino más cercano; se conservaron las clases 4 (vegetación), 5 (superficie no vegetada) y 6 (agua). Las demás clases, incluida la 2 (áreas oscuras, que pueden incluir sombras), y siete píxeles con alguna reflectancia negativa se guardaron como `NaN`. Quedaron 1.000.426 píxeles válidos.

El GeoTIFF resultante contiene reflectancia `float32` en cuatro bandas, en el orden B02, B03, B04 y B08. Su RGB de pantalla se obtiene estirando esos valores **solo para visualizar**. NDVI y NDWI se calculan con la reflectancia, nunca con el RGB estirado. Esta selección de una escena con baja nubosidad y la máscara SCL facilitan la demostración; no equivalen a una validación de campo ni a una clasificación agronómica.
