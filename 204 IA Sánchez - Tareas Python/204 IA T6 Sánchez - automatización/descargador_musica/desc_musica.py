import yt_dlp
import os
os.system("cls")

def crear_carpeta_si_no_existe(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def descargar_audio_youtube(url):

    ruta_descarga = './descargas'
    crear_carpeta_si_no_existe(ruta_descarga)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(ruta_descarga, '%(title)s.%(ext)s'), 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("descargando audio :) ...")
            ydl.download([url])
            print(f"descarga completada y guardada en: {ruta_descarga}")
    except Exception as e:
        print(f"error al descargar el video: {e}")


if __name__ == "__main__":
    url = input("---introduce la URL de YouTube: ---\n")
    descargar_audio_youtube(url)
