# '/api/v1/details'
# '/api/v1/health'

from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])

def details():
    return jsonify({
        'name': 'Flask API',
        'version': '1.0.0',
        'description': 'A simple Flask API for demonstration purposes',
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'port': request.host.split(':')[1],
        'protocol': request.scheme,
        'message': 'OK!'
    }), 200

@app.route('/api/v1/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'message': 'The API is running smoothly'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)