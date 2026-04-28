from flask import Flask, request, jsonify, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    url     = data.get('url')
    quality = data.get('quality', '192')
    fmt     = data.get('format', 'mp3')

    if not url:
        return jsonify({'error': 'URL requerida'}), 400

    output_id = str(uuid.uuid4())
    output_path = f'/tmp/{output_id}.%(ext)s'

    opciones = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': fmt,
            'preferredquality': quality,
        }],
        'outtmpl': output_path,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'audio')

        final_path = f'/tmp/{output_id}.{fmt}'
        return send_file(
            final_path,
            as_attachment=True,
            download_name=f'{title}.{fmt}',
            mimetype='audio/mpeg'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500