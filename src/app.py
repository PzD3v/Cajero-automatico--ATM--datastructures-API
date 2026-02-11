"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import BankAccount
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app) # Con el Cors se puede acceder a la API desde otros dominios sin ello NO

# Create object
my_account = BankAccount("ppesant","12345")
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/') #Esta funcion se encarga de lo que pase cuando alguien ingrese a la API 
def sitemap(): #definimos el nombre de la funcion
    return generate_sitemap(app) #lEscanea el codigo, revisa todas las rutas creadas y crea una lista que muestra todos los endpoints disponibles de la API

@app.route('/withdraw', methods=['POST'])
def withdraw_money():
    data = request.get_json(silent=True)
    # 1. Validación de existencia
    if data is None or 'amount' not in data or 'pin' not in data:
        return jsonify({"msg": "Error: Faltan datos (amount o pin)"}), 400

    try:
        # 2. Conversión a FLOAT para los centavos
        monto = float(data['amount'])
        pin_usuario = str(data['pin']) # El PIN suele ser mejor tratarlo como string
    except ValueError:
        return jsonify({"msg": "Error: El monto debe ser un número válido"}), 400

    if monto <= 0:
        return jsonify({"msg": "Error: El monto a retirar debe ser mayor a cero"}), 400
        
    # 3. Llamada a la lógica de la clase
    result = my_account.withdraw(monto, pin_usuario)
    
    # 4. Interpretación de resultados
    if result == "CUENTA_BLOQUEADA":
        return jsonify({"msg": "SEGURIDAD: Cuenta bloqueada por exceso de intentos"}), 403
    
    if result == "PIN INCORRECTO":
        return jsonify({"msg": "PIN incorrecto. Inténtalo de nuevo"}), 401
        
    if result == "FONDOS_INSUFICIENTES":
        return jsonify({"msg": "Saldo insuficiente para completar el retiro"}), 400

    # Si llegamos aquí, result es el nuevo saldo (float)
    return jsonify({"msg": f"Retiro exitoso. Saldo restante: {result:.2f}"}), 200

@app.route('/deposit', methods=['POST'])
def deposit_money():
    data = request.get_json(silent=True)
    
    # 1. Validación de existencia (como siempre)
    if data is None or 'amount' not in data:
        return jsonify({"msg": "Error: Falta el campo 'amount'"}), 400

    try:
        # 2. Convertimos a FLOAT para aceptar decimales
        # Esto convierte "11.50" en 11.5
        monto = float(data['amount']) 
    except ValueError:
        return jsonify({"msg": "Error: El monto debe ser un número válido (ej: 10.50)"}), 400

    if monto <= 0:
        return jsonify({"msg": "El monto debe ser mayor a cero"}), 400
        
    result = my_account.deposit(monto) 
    
    # Usamos :.2f para mostrar siempre dos decimales en el mensaje (ej: 11.50)
    return jsonify({"msg": f"Depósito con éxito. Nuevo saldo: {result:.2f}"}), 200
    
@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify({"balance": my_account.balance}), 200




# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
