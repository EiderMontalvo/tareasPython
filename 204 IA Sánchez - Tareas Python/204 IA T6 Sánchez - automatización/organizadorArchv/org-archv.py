import os
import shutil

carpeta_origen = r'C:\Users\anonimo\Downloads' #colocar la ruta a ordenar


tipos_archivos = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Música': ['.mp3', '.wav'],
    'Otros': []
}


def organizar_archivos(carpeta_origen, tipos_archivos):
    
    for archivo in os.listdir(carpeta_origen):
        ruta_archivo = os.path.join(carpeta_origen, archivo)

        
        if os.path.isdir(ruta_archivo):
            continue

        _, extension = os.path.splitext(archivo)

        movido = False
        for carpeta, extensiones in tipos_archivos.items():
            if extension.lower() in extensiones:
                carpeta_destino = os.path.join(carpeta_origen, carpeta)

                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)

                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                movido = True
                print(f'Movido: {archivo} -> {carpeta_destino}')
                break

        if not movido:
            carpeta_destino = os.path.join(carpeta_origen, 'Otros')
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
            print(f'Movido: {archivo} -> {carpeta_destino}')

organizar_archivos(carpeta_origen, tipos_archivos)
