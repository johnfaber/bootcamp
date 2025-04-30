from flask import Flask, request, jsonify
import threading
import time
import os

app = Flask(__name__)

def cpu_burn(duration):
    """Función que consume CPU durante `duration` segundos."""
    end_time = time.time() + duration
    while time.time() < end_time:
        pass  # Busy loop

def handle_request(seconds):
    """Lanza un hilo para quemar CPU."""
    thread = threading.Thread(target=cpu_burn, args=(seconds,))
    thread.start()
    print(f"Hilo lanzado para consumir CPU {seconds} segundos.")

@app.route('/consume_cpu', methods=['POST'])
def consume_cpu():
    try:
        data = request.get_json()
        seconds = float(data.get('seconds'))
        if seconds <= 0:
            return jsonify({"error": "El tiempo debe ser mayor que 0"}), 400
        handle_request(seconds)
        return jsonify({"message": f"Hilo lanzado para consumir CPU {seconds} segundos en contenedor {os.environ.get('HOSTNAME')}."}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Solicitud inválida. Debe enviar 'seconds' como número."}), 400

print("Iniciando servidor...")  # debug print

app.run(host='0.0.0.0', port=5000)
