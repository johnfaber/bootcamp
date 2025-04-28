from flask import Flask, request, jsonify
import socket
import os
import time
# Crear la app Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hola desde el servidor Flask"

@app.route('/uname')
def uname():
    time.sleep(2)
    return {"hostname": socket.gethostname(),
            "ip": socket.gethostbyname(socket.gethostname()),
            "env": os.environ.get('ENV')}


print("Iniciando servidor...")  # debug print

app.run(host="0.0.0.0", port=5000, debug=True)