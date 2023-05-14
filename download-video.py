import argparse
from pytube import YouTube

# Configurar el parser de argumentos
parser = argparse.ArgumentParser(description='Descargar video de YouTube')
parser.add_argument('url', type=str, help='URL del video de YouTube a descargar')

# Obtener la URL del video a descargar
args = parser.parse_args()
video_url = args.url

# Descargar el video
yt = YouTube(video_url)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print('Video descargado.')