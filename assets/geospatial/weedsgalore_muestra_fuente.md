# Fuente de `weedsgalore_muestra/`

- **Conjunto:** [WeedsGalore](https://github.com/GFZ/weedsgalore), imágenes multiespectrales de dron sobre maíz en Marquardt, Alemania, registradas en cuatro fechas de 2023.
- **Artículo:** Celikkan et al., *WeedsGalore: A Multispectral and Multitemporal UAV-Based Dataset for Crop and Weed Segmentation in Agricultural Maize Fields*, WACV 2025. ([versión abierta](https://arxiv.org/html/2502.13103v1)).
- **Descarga original:** [weedsgalore-dataset.zip](https://doidata.gfz.de/weedsgalore_e_celikkan_2024/weedsgalore-dataset.zip) (~321 MB).
- **Muestra incluida:** `2023-06-06_0625`, de 600 × 600 píxeles con muestreo aproximado de 2,5 mm por píxel.
- **Archivos:** cinco bandas en `images/` (rojo `R`, verde `G`, azul `B`, borde rojo `RE`, infrarrojo cercano `NIR`) y máscara de referencia en `semantics/`.
- **Etiquetas de la máscara:** 0 = fondo/suelo, 1 = maíz, 2 a 5 = grupos de malezas. Fueron revisadas por personas en campo.
- **Licencia:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Atribución: *Celikkan et al., WeedsGalore, WACV 2025.*

Esta muestra se usa en las clases 3 y 4 tal como fue publicada, sin recortes ni reprocesamiento. Los notebooks la leen directamente desde esta carpeta; no requieren descarga ni conexión.
