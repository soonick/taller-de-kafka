from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/student', methods=['POST'])
def add_student():
    resp = {
        "hello": "you"
    }
    return resp
