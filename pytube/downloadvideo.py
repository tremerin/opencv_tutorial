from pytubefix import YouTube

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=NxxLf-pKnVQ&ab_channel=Darwin"  # Reemplaza con tu URL

try:
    # Crear objeto YouTube
    yt = YouTube(url)
    #print(yt)

    # Mostrar información del video
    print("📌 Título:", yt.title)
    print("⏳ Duración:", yt.length, "segundos")
    print("👤 Autor:", yt.author)

    # Descargar la mejor resolución disponible
    stream = yt.streams.get_highest_resolution()
    print("⬇️ Descargando:", stream.resolution)
    #for stream in yt.streams:
    #    print(stream)
    
    # Ruta de descarga (opcional: omítelo para guardar en la carpeta actual)
    download_path = "../resources/downloads"
    stream.download(output_path=download_path)
    
    print("✅ ¡Descarga completada!")

except Exception as e:
    print("❌ Error:", str(e))



"""from pytubefix import YouTube
import os

url = "https://www.youtube.com/watch?v=NxxLf-pKnVQ"  # Tu URL

try:
    yt = YouTube(url)
    print("📌 Título:", yt.title)

    # Filtrar streams de video DASH (sin audio, alta resolución)
    video_stream = yt.streams.filter(
        type="video",          # Solo video
        progressive=False,     # Excluir streams combinados (video+audio)
        file_extension="mp4"  # Formato MP4
    ).order_by("resolution").desc().first()  # Mayor resolución disponible

    # Filtrar streams de audio (mejor calidad)
    audio_stream = yt.streams.filter(
        type="audio",
        file_extension="mp4"
    ).order_by("abr").desc().first()  # Mayor bitrate de audio

    print("🎬 Video seleccionado:", video_stream.resolution)
    print("🔊 Audio seleccionado:", audio_stream.abr)

    # Descargar ambos
    download_path = "../resources/downloads"
    os.makedirs(download_path, exist_ok=True)

    video_path = video_stream.download(output_path=download_path, filename="video_temp")
    audio_path = audio_stream.download(output_path=download_path, filename="audio_temp")

    print("⬇️ Descargados por separado. Combinando con ffmpeg...")

    # Combinar video y audio (requiere ffmpeg instalado)
    from pytubefix.cli import on_progress
    final_path = os.path.join(download_path, f"{yt.title}.mp4")
    os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{final_path}"')

    # Eliminar archivos temporales
    os.remove(video_path)
    os.remove(audio_path)

    print("✅ ¡Video en máxima calidad guardado como:", final_path)

except Exception as e:
    print("❌ Error:", str(e))"""