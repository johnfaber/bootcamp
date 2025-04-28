# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Crear la app Flask
app = Flask(__name__)

# Configurar base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Definir el modelo de la tabla
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Ruta para recibir JSON y guardar en la base de datos
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or not 'name' in data or not 'email' in data:
        return jsonify({"error": "Faltan datos"}), 400

    new_user = User(name=data['name'], email=data['email'])

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuario creado exitosamente", "user_id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Opcional: ruta para listar usuarios
@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    result = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(result)

print("Iniciando servidor...")  # debug print

app.run(host="0.0.0.0", port=5000, debug=True)
