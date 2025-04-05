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