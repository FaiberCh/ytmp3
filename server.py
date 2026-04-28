from flask import Flask, request, jsonify, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

def get_cookies_file():
    cookies_content = os.environ.get('COOKIES_CONTENT')
    if cookies_content:
        cookies_path = f'/tmp/cookies_{uuid.uuid4().hex}.txt'
        with open(cookies_path, 'w') as f:
            f.write(cookies_content)
        return cookies_path
    return None

@app.route('/')
def index():
    return send_file('index.html')

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
    cookies_path = get_cookies_file()


    opciones = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': fmt,
            'preferredquality': quality,
        }],
        'outtmpl': output_path,
        'quiet': True,
        'extractor_args': {
            'youtube': {
                'po_token': ['web+' + os.environ.get('PO_TOKEN', '')]
            }
        },
    }

    if cookies_path:
        opciones['cookiefile'] = cookies_path

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'audio')

        final_path = f'/tmp/{output_id}.{fmt}'

        if cookies_path and os.path.exists(cookies_path):
            os.remove(cookies_path)

        return send_file(
            final_path,
            as_attachment=True,
            download_name=f'{title}.{fmt}',
            mimetype='audio/mpeg'
        )
    except Exception as e:
        if cookies_path and os.path.exists(cookies_path):
            os.remove(cookies_path)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)