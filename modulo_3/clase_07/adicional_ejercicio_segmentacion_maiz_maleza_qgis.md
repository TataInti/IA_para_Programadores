# Ejercicio guiado — Crear una máscara de maíz y malezas en QGIS

## De polígonos dibujados a etiquetas por píxel

**Duración:** 50–60 minutos · **Versión de referencia:** QGIS 3.44.15

## Qué vas a hacer

Vas a dibujar el contorno de **una planta de maíz y una maleza**, asignarles valores y convertir esos polígonos en un ráster de clases del mismo tamaño que la imagen.

Al terminar vas a tener una máscara de **600 × 600 píxeles** con estos valores:

| Valor | Significado en tu máscara |
|---:|---|
| `0` | Zona que no etiquetaste |
| `1` | Maíz |
| `2` | Maleza |

El `0` no quiere decir que todos esos píxeles sean suelo: solo marca lo que todavía no dibujaste. La imagen de referencia trae más clases de malezas; acá las agrupamos para practicar el recorrido sin agregar dificultad.

## Antes de empezar: qué significa «píxel a píxel»

La máscara de salida será un ráster: cada celda guarda un número de clase. En este ejercicio no vas a hacer un clic en cada píxel. Vas a dibujar polígonos alrededor de dos plantas y QGIS asignará el número correspondiente a los píxeles que cubren. El borde depende de cómo dibujes esas formas.

La muestra es de un recorte de dron de maíz, de **600 × 600 píxeles**, con una banda roja y una máscara de referencia ya etiquetada. Sus archivos originales no tienen coordenadas terrestres. Para conservar la cuadrícula y facilitar el trabajo, preparé dos rásteres virtuales que usan coordenadas locales de píxel; no modifican las imágenes originales.

## Archivos de la práctica

Desde la carpeta `media/clase_07/` de la raíz del repositorio, usá estos dos archivos:

- **Imagen base:** [`maiz_maleza_banda_roja_pixelgrid.vrt`](../../media/clase_07/maiz_maleza_banda_roja_pixelgrid.vrt)
- **Máscara de referencia:** [`maiz_maleza_mascara_referencia_pixelgrid.vrt`](../../media/clase_07/maiz_maleza_mascara_referencia_pixelgrid.vrt)

Los VRT consultan las imágenes originales de [`weedsgalore_muestra/`](../../assets/geospatial/weedsgalore_muestra/). Mantené disponible la carpeta `assets` del curso. No asignes `EPSG:32619`: este ejercicio trabaja en una cuadrícula de píxeles, no en coordenadas de un campo.

## 1. Abrí las imágenes en una cuadrícula local

1. En QGIS elegí **Proyecto → Nuevo**.
2. Abrí **Proyecto → Propiedades → SRC** y seleccioná **No CRS (o proyección desconocida/no terrestre)**. QGIS va a tratar las posiciones como coordenadas planas de la imagen, sin ubicarlas sobre la Tierra.
3. Elegí **Capa → Añadir capa → Añadir capa ráster…** y agregá los dos VRT.
4. En el panel **Capas**, poné `maiz_maleza_mascara_referencia_pixelgrid` encima de `maiz_maleza_banda_roja_pixelgrid`.
5. Usá **Zoom a la capa** para encuadrar la banda roja.

Ambos archivos tienen el mismo tamaño, origen y resolución de píxel. Si no coinciden, revisá que hayas abierto los dos VRT de esta carpeta y que el proyecto siga en **No CRS**.

## 2. Coloreá la máscara de referencia

La máscara tiene valores numéricos; la simbología nos ayuda a verlos sobre la banda.

1. Abrí **Propiedades** de `maiz_maleza_mascara_referencia_pixelgrid`.
2. En **Simbología**, elegí **Valores en paleta/valores únicos** y presioná **Clasificar**.
3. Asigná etiquetas fáciles de leer:

   | Valor | Etiqueta |
   |---:|---|
   | `0` | Fondo / suelo |
   | `1` | Maíz |
   | `2` | Maleza grupo 1 |
   | `3` | Maleza grupo 2 |
   | `4` | Maleza grupo 3 |
   | `5` | Maleza grupo 4 |

4. Elegí colores contrastantes: por ejemplo, verde para maíz y distintos tonos para cada grupo de malezas.
5. Aplicá los cambios. Encendé y apagá la máscara para comparar las clases con la banda roja.

La máscara de referencia sirve para ubicar un ejemplo bien delimitado de maíz y otro de maleza. Seleccioná el ráster de referencia y usá **Identificar objetos espaciales** para consultar valores: `1` es maíz y los valores `2` a `5` son grupos de malezas.

## 3. Creá una capa para tus etiquetas

Ahora vas a guardar los contornos como entidades vectoriales. Cada polígono tendrá un campo numérico que después se copiará a los píxeles.

1. Elegí **Capa → Crear capa → Nueva capa GeoPackage…**.
2. Guardá el archivo como `etiquetas_maiz_maleza.gpkg`, por ejemplo en `Documentos/Clase07_MaizMaleza`.
3. En **Nombre de tabla**, escribí `etiquetas`.
4. Elegí **Polígono** como tipo de geometría.
5. En **SRC**, elegí el **SRC del proyecto**. Debe ser **No CRS**; no elijas un EPSG.
6. Agregá el campo `valor` de tipo **Entero (32 bit)** y presioná **Añadir a la lista de campos**.
7. Presioná **Aceptar**. En el panel **Capas**, dejá `etiquetas` encima de la banda roja y debajo de la máscara de referencia.

Si el selector no muestra `Project CRS: No CRS`, volvé a **Proyecto → Propiedades → SRC** y confirmá que elegiste **No CRS** antes de crear esta capa.

## 4. Dibujá las dos etiquetas

La máscara de referencia sirve como guía para encontrar plantas. Para dibujar, apagá su casilla y dejá visible la banda roja junto con `etiquetas`.

1. Seleccioná `etiquetas` y activá **Conmutar edición**.
2. Elegí **Añadir polígono** y acercate a una planta de maíz.
3. Hacé clic en varios puntos alrededor del borde visible de la planta. Usá suficientes puntos para seguir su forma, sin intentar marcar cada píxel por separado.
4. Cerrá el polígono con clic derecho. En el formulario, escribí `1` en `valor` y aceptá.
5. Repetí el procedimiento alrededor de una maleza bien delimitada. Al terminar, escribí `2` en `valor`.
6. Apagá la edición y guardá los cambios cuando QGIS lo pregunte.

**Pregunta para revisar el dibujo:** ¿el contorno sigue a la planta o también incluye suelo que no querías etiquetar?

## 5. Convertí los polígonos en un ráster

La herramienta de rasterización copia el valor de cada polígono a las celdas que cubre.

1. Abrí la **Caja de herramientas de Procesos** y buscá **Rasterizar (vectorial a ráster)**.
2. Completá los parámetros:

   | Parámetro | Valor |
   |---|---|
   | **Capa de entrada** | `etiquetas` |
   | **Campo para el valor de quemado** | `valor` |
   | **Unidades de tamaño del ráster** | Píxeles |
   | **Anchura** | `600` |
   | **Altura** | `600` |
   | **Extensión de salida** | Calcular desde `maiz_maleza_banda_roja_pixelgrid` |
   | **Tipo de datos salientes** | Byte |
   | **Preinicializar la imagen de salida con valor** | `0` |
   | **NoData** | `255` |
   | **Salida** | Guardar como `mascara_manual.tif` |

3. Ejecutá la herramienta.
4. En **Propiedades → Simbología** de `mascara_manual`, elegí **Valores en paleta/valores únicos** y clasificá los valores `0`, `1` y `2`.
5. Etiquetá `0` como `Sin marcar`, `1` como `Maíz` y `2` como `Maleza`.

La extensión y las 600 filas por 600 columnas hacen que la salida tenga la misma cuadrícula que la banda de entrada. El `0` preinicializa las zonas que no cubren los polígonos. Reservamos `255` como NoData, aunque no se usa en las etiquetas; así `0` sigue siendo un valor válido que significa «sin marcar».

## 6. Compará tu máscara con la referencia

1. Mantené la banda roja abajo y encendé `mascara_manual`.
2. Encendé y apagá `maiz_maleza_mascara_referencia_pixelgrid` para comparar las dos máscaras.
3. Usá **Identificar objetos espaciales** sobre `mascara_manual`. Comprobá que un píxel dentro del polígono de maíz tenga valor `1`, uno dentro de la maleza tenga valor `2` y uno fuera de ambos polígonos tenga valor `0`.

La comparación no mide la calidad de un modelo. Muestra cómo se convierte una forma vectorial en etiquetas ráster y qué partes de la planta quedaron dentro o fuera del dibujo.

## Entrega

Guardá estos tres archivos en tu carpeta de práctica:

- `etiquetas_maiz_maleza.gpkg`: los dos polígonos y el campo `valor`.
- `mascara_manual.tif`: la máscara de 600 × 600 píxeles.
- `ejercicio_maiz_maleza.qgz`: el proyecto con las capas ordenadas y visibles.

Antes de cerrar, comprobá:

| Comprobación | Listo |
|---|---|
| El polígono del maíz tiene `valor = 1`. | ☐ |
| El polígono de maleza tiene `valor = 2`. | ☐ |
| `mascara_manual` tiene valores `0`, `1` y `2`. | ☐ |
| La máscara manual coincide en tamaño y extensión con la banda. | ☐ |
| Puedo alternar mi máscara y la de referencia. | ☐ |
| Guardé el GeoPackage, el GeoTIFF y el proyecto. | ☐ |

### Contalo en una frase

> “Dibujé las clases ___ y ___, les asigné los valores ___ y ___, y QGIS los convirtió en píxeles con la herramienta ___.”

## Para ubicar la práctica

Este ejercicio enseña a **crear una máscara manual sencilla** a partir de polígonos. No hace que QGIS identifique automáticamente las plantas. El conjunto WeedsGalore incluye anotaciones de referencia detalladas; en trabajos de segmentación se usan esas etiquetas para entrenar o revisar modelos. La imagen, sus etiquetas y el recorte se describen en la [ficha de la muestra](../../assets/geospatial/weedsgalore_muestra_fuente.md).

## Referencias de QGIS

- [Valores en paleta/valores únicos](https://docs.qgis.org/3.44/es/docs/user_manual/working_with_raster/raster_properties.html#paletted-unique-values).
- [Identificar celdas ráster](https://docs.qgis.org/3.44/es/docs/user_manual/working_with_raster/raster_properties.html#identify-raster-cells).
- [Proyecto sin CRS](https://docs.qgis.org/3.44/es/docs/user_manual/working_with_projections/working_with_projections.html#project-coordinate-reference-systems).
- [Rasterizar geometrías vectoriales en un ráster](https://docs.qgis.org/3.44/es/docs/user_manual/processing_algs/gdal/vectorconversion.html#rasterize-vector-to-raster).
- Celikkan et al., [WeedsGalore: segmentación semántica y por instancias de maíz y malezas](https://openaccess.thecvf.com/content/WACV2025/papers/Celikkan_WeedsGalore_A_Multispectral_and_Multitemporal_UAV-Based_Dataset_for_Crop_and_WACV_2025_paper.pdf), WACV 2025.
