from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/data', methods=['GET'])
def get_data():
    print("Sent the message")
    return "Hello, this is the data!"

if __name__ == '__main__':
    port = 2000
    print(f"Server running at http://localhost:{port}")
    app.run(host='0.0.0.0', port=port)
