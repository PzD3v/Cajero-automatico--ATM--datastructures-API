"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"family": members}
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_member():
    member=request.json #obtener el diccionario que el POST envía
    jackson_family.add_member(member) #agregar el miembro
    return jsonify([{"msg":"Miembro agregado"}]), 200 #retornar la respuesta si todo esta bien 

@app.route('/member/<int:id>', methods=["GET"])
def get_member(id):
    member = jackson_family.get_member(id)
    return jsonify(member), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    
    success = jackson_family.delete_member(id)
    if success:
        members = jackson_family.get_all_members()
        return jsonify({"msg": f"El miembro con id {id} ha sido eliminado"},{"family":members}),200
    else:
        return jsonify({"msg":"No se encontro un miembro con ese ID "})

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
