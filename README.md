# YT→MP3

Convierte videos de YouTube a audio MP3, M4A, WAV u OPUS directamente desde el navegador.

![Estado](https://img.shields.io/badge/estado-activo-brightgreen)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Flask](https://img.shields.io/badge/flask-3.1.3-lightgrey)

## Demo

🔗 [ytmp3-delta.vercel.app](https://ytmp3-delta.vercel.app)

## Características

- Convierte videos de YouTube a MP3, M4A, WAV u OPUS
- Selección de calidad: 64, 128, 192 o 320 kbps
- Descarga automática al terminar la conversión
- Interfaz limpia y responsiva

## Tecnologías

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python + Flask
- **Audio:** yt-dlp + FFmpeg

## Uso local

```bash
# 1. Clona el repositorio
git clone https://github.com/FaiberCh/ytmp3.git
cd ytmp3

# 2. Crea y activa el entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Corre el servidor
python server.py
```

Abre tu navegador en **http://localhost:5000**

## Requisitos del sistema

- Python 3.12+
- FFmpeg instalado y en el PATH

## ⚠ Uso responsable

Esta herramienta está diseñada para descargar contenido que tengas permiso explícito de usar — tus propios videos, contenido con licencia Creative Commons o material de dominio público. Respetar los términos de servicio de YouTube y las leyes de propiedad intelectual de tu país.

## Autor

Hecho por [@FaiberCh](https://github.com/FaiberCh)
