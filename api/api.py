from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Aktiviert CORS für alle Routen

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/<filename>')
def serve_file(filename):
    return send_from_directory('./logs', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)