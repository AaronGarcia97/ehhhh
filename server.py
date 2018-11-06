from flask import jsonify
from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

#Scan a single device, receive ip address
@app.route("/")
def hello():
	return "hello world"
