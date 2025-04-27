from PIL import Image
import os


# Funcion para procesar la imagen
def procesar_imagen(image_path):
    # define un tamaño de imagen
    size = (128, 128)
    # abre la imagen para trabajarla
    img = Image.open(image_path)
    # toma la ruta del archivo
    nombre_archivo = os.path.basename(img.filename)
    # cambia el taño de la imagen sin deformarla
    img.thumbnail(size)
    print(img.format, img.size, img.mode, nombre_archivo)
    # guarda la imagen nueva en una ruta determinada
    nueva_ruta = f"/mnt/d/proyectoProgramacion/proyecto-django-platzi/coffee-shop-platzi/coffee_shop/media/logos/new_{nombre_archivo}"
    ruta_bd = f"logos/new_{nombre_archivo}"
    img.save(nueva_ruta, format="JPEG")
    # se trae la nueva ruta del archivo
    print(nueva_ruta)
    print(ruta_bd)
    return ruta_bd


procesar_imagen(
    "/mnt/d/proyectoProgramacion/proyecto-django-platzi/coffee-shop-platzi/coffee_shop/media/imagenes_base/escoba.jpg"
)
