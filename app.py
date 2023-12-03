from flask import Flask, abort, request
from flask_cors import CORS
from tempfile import NamedTemporaryFile
import whisper
import torch

# Check if NVIDIA GPU is available
torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Whisper model:
model = whisper.load_model("base", device=DEVICE)

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Whisper Hello World!"


@app.route('/transcription', methods=['POST'])
def handler():
    if not request.files:
        abort(400)

    results = []

    for filename, handle in request.files.items():
        # Create a temporary file.
        temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(temp)
        # Let's get the transcript of the temporary file.
        result = model.transcribe(temp.name)
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    return {'results': results}
