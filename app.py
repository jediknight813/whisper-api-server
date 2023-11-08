from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'audio_files'
WHISPER_MODEL = os.environ.get('WHISPER_MODEL', 'small.en')

model = whisper.load_model(WHISPER_MODEL)


@app.route('/transcribe_audio', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})


    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        result = model.transcribe(filename)
        return jsonify({'text': result, "all_data": result})


if __name__ == '__main__':
    app.run(debug=True, port=8888, host="0.0.0.0")
