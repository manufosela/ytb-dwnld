import argparse
from pytube import YouTube
import os

# Configurar el parser de argumentos
parser = argparse.ArgumentParser(description='Descargar audio de YouTube')
parser.add_argument('url', type=str, help='URL del video de YouTube del que se quiere descargar el audio')

# Obtener la URL del video de YouTube
args = parser.parse_args()
video_url = args.url

# Descargar el audio del video de YouTube
yt = YouTube(video_url)
audio_stream = yt.streams.filter(only_audio=True).first()
audio_filename = f'{yt.title}-audio.mp3'
audio_stream.download(output_path='.', filename_prefix='temp')
os.rename(f'temp.{audio_stream.subtype}', audio_filename)

print(f'Audio del video "{yt.title}" descargado como "{audio_filename}".')