"""Carga una muestra pequeña del conjunto abierto WeedsGalore para la clase 3."""
from pathlib import Path, PurePosixPath
from io import BytesIO
import ssl
import urllib.error
import urllib.request
import zipfile
import certifi
import numpy as np
from PIL import Image

URL_DATOS = "https://doidata.gfz.de/weedsgalore_e_celikkan_2024/weedsgalore-dataset.zip"
BANDAS_ARCHIVO = {"rojo": "R", "verde": "G", "azul": "B", "nir": "NIR", "borde_rojo": "RE"}


def _ruta_segura(carpeta, miembro):
    partes = PurePosixPath(miembro).parts
    if ".." in partes:
        raise ValueError("La ruta del archivo de datos no es válida.")
    return carpeta.joinpath(*partes)


def _buscar_muestra(archivo):
    nombres = set(archivo.namelist())
    for fecha in ("2023-06-06", "2023-05-30", "2023-06-15", "2023-05-25"):
        candidatos = sorted(n for n in nombres if f"/{fecha}/semantics/" in f"/{n}" and n.endswith(".png"))
        opciones = []
        for miembro in candidatos:
            mascara = np.asarray(Image.open(BytesIO(archivo.read(miembro))))
            if mascara.ndim != 2:
                continue
            cultivo = np.count_nonzero(mascara == 1)
            malezas = np.count_nonzero(mascara > 1)
            if cultivo and malezas:
                opciones.append((min(cultivo, malezas) / mascara.size, miembro))
        if opciones:
            return max(opciones)[1]
    raise FileNotFoundError("No se encontró una muestra anotada con maíz y malezas.")


def _descargar(archivo_zip):
    if archivo_zip.exists() and zipfile.is_zipfile(archivo_zip):
        return
    print("Descargando el conjunto oficial (aprox. 321 MB); puede tardar unos minutos.")
    temporal = archivo_zip.with_suffix(".zip.part")

    # Usa el almacén actualizado de certifi y mantiene activa la verificación TLS.
    contexto_ssl = ssl.create_default_context(cafile=certifi.where())
    try:
        with urllib.request.urlopen(URL_DATOS, context=contexto_ssl, timeout=60) as respuesta:
            total = int(respuesta.headers.get("Content-Length", 0))
            recibidos = 0
            ultimo_porcentaje = -20
            with temporal.open("wb") as salida:
                while bloque := respuesta.read(1024 * 1024):
                    salida.write(bloque)
                    recibidos += len(bloque)
                    if total:
                        porcentaje = min(100, int(recibidos * 100 / total))
                        if porcentaje >= ultimo_porcentaje + 20:
                            print(f"Descarga: {porcentaje}%")
                            ultimo_porcentaje = porcentaje
            if total and ultimo_porcentaje < 100:
                print("Descarga: 100%")
    except (urllib.error.URLError, ssl.SSLCertVerificationError) as error:
        temporal.unlink(missing_ok=True)
        causa = error.reason if isinstance(error, urllib.error.URLError) else error
        if isinstance(causa, ssl.SSLCertVerificationError) or "CERTIFICATE_VERIFY_FAILED" in str(causa):
            raise RuntimeError(
                "No se pudo verificar el certificado del servidor. Se usó el almacén de certifi; "
                "actualizalo con `python -m pip install --upgrade certifi` y volvé a ejecutar. "
                "Si estás en una red institucional, pedí la CA de esa red y configurala para Python."
            ) from error
        raise
    except Exception:
        temporal.unlink(missing_ok=True)
        raise

    temporal.replace(archivo_zip)


def cargar_muestra():
    raiz_repo = Path(__file__).resolve().parents[2]
    cache = raiz_repo / "datos_cache"
    cache.mkdir(exist_ok=True)
    archivo_zip = cache / "weedsgalore-dataset.zip"
    carpeta_muestra = cache / "weedsgalore_muestra"
    marcador = cache / "weedsgalore_muestra.txt"

    miembro = marcador.read_text(encoding="utf-8").strip() if marcador.exists() else ""
    ruta_mascara = _ruta_segura(carpeta_muestra, miembro) if miembro else None
    rutas_bandas = {}
    if ruta_mascara is not None:
        stem = PurePosixPath(miembro).stem
        carpeta_imagenes = ruta_mascara.parent.parent / "images"
        rutas_bandas = {nombre: _ruta_segura(carpeta_muestra, str(carpeta_imagenes.relative_to(carpeta_muestra) / f"{stem}_{sufijo}.png"))
                        for nombre, sufijo in BANDAS_ARCHIVO.items()}
    if ruta_mascara is None or not ruta_mascara.exists() or any(not p.exists() for p in rutas_bandas.values()):
        marcador.unlink(missing_ok=True)
        _descargar(archivo_zip)
        with zipfile.ZipFile(archivo_zip) as zf:
            miembro = _buscar_muestra(zf)
            ruta_relativa = PurePosixPath(miembro)
            stem = ruta_relativa.stem
            carpeta_imagenes = ruta_relativa.parent.parent / "images"
            miembros = [miembro] + [str(carpeta_imagenes / f"{stem}_{sufijo}.png") for sufijo in BANDAS_ARCHIVO.values()]
            for nombre in miembros:
                salida = _ruta_segura(carpeta_muestra, nombre)
                salida.parent.mkdir(parents=True, exist_ok=True)
                salida.write_bytes(zf.read(nombre))
        marcador.write_text(miembro, encoding="utf-8")
        ruta_mascara = _ruta_segura(carpeta_muestra, miembro)
        stem = PurePosixPath(miembro).stem
        carpeta_imagenes = ruta_mascara.parent.parent / "images"
        rutas_bandas = {nombre: _ruta_segura(carpeta_muestra, str(carpeta_imagenes.relative_to(carpeta_muestra) / f"{stem}_{sufijo}.png"))
                        for nombre, sufijo in BANDAS_ARCHIVO.items()}

    etiqueta = np.asarray(Image.open(ruta_mascara))
    bandas = {nombre: np.asarray(Image.open(ruta), dtype=np.float32) for nombre, ruta in rutas_bandas.items()}
    if len({b.shape for b in bandas.values()} | {etiqueta.shape}) != 1:
        raise ValueError("Las bandas y la máscara no tienen el mismo tamaño.")
    identificador = PurePosixPath(miembro).stem
    fecha = next((parte for parte in PurePosixPath(miembro).parts if parte.startswith("2023-")), "fecha sin registrar")
    print(f"Muestra: {identificador} · fecha: {fecha} · tamaño: {etiqueta.shape[1]} × {etiqueta.shape[0]} píxeles")
    print(f"Píxeles anotados como maíz: {np.count_nonzero(etiqueta == 1):,} · malezas: {np.count_nonzero(etiqueta > 1):,} · fondo: {np.count_nonzero(etiqueta == 0):,}")
    return bandas, etiqueta, identificador, fecha
