from PIL import Image
import os


#Funcion para procesar la imagen
def procesar_imagen(image_path):
    size = (128, 128)
    img = Image.open(image_path)
    nombre_archivo = os.path.basename(img.filename)
    img.thumbnail(size)
    print(img.format, img.size, img.mode, nombre_archivo)
    img.save(f"media/logos/new_{nombre_archivo}", format="JPEG")
    nueva_ruta = img.filename
    print(nueva_ruta)
    return nueva_ruta

