import json
from flask import request, jsonify
from bson import json_util
from bson.objectid import ObjectId

from app import app, db

# ─── LISTAR TODOS OS CARROS ───────────────────────────────────────────────
@app.route("/carros", methods=["GET"])
def listar_carros():
    cursor = db.carros.find().sort("_id", 1)
    carros = json.loads(json_util.dumps(cursor))
    return jsonify(carros), 200


# ─── OBTER CARRO POR ID ───────────────────────────────────────────────────
@app.route("/carros/<string:carro_id>", methods=["GET"])
def get_carro(carro_id):
    carro = db.carros.find_one({"_id": ObjectId(carro_id)})
    if not carro:
        return jsonify({"erro": "Carro não encontrado"}), 404
    return jsonify(json.loads(json_util.dumps(carro))), 200


# ─── CRIAR NOVO CARRO ────────────────────────────────────────────────────
@app.route("/carros", methods=["POST"])
def criar_carro():
    dados = request.json
    # aqui pode validar campos obrigatórios, ex: nome, marca, preco...
    result = db.carros.insert_one(dados)
    return jsonify({
        "mensagem": "Carro criado com sucesso",
        "id": str(result.inserted_id)
    }), 201


# ─── ATUALIZAR CARRO EXISTENTE ────────────────────────────────────────────
@app.route("/carros/<string:carro_id>", methods=["PUT"])
def atualizar_carro(carro_id):
    dados = request.json
    resultado = db.carros.update_one(
        {"_id": ObjectId(carro_id)},
        {"$set": dados}
    )
    if resultado.matched_count == 0:
        return jsonify({"erro": "Carro não encontrado"}), 404
    return jsonify({"mensagem": "Carro atualizado com sucesso"}), 200


# ─── DELETAR CARRO ────────────────────────────────────────────────────────
@app.route("/carros/<string:carro_id>", methods=["DELETE"])
def deletar_carro(carro_id):
    resultado = db.carros.delete_one({"_id": ObjectId(carro_id)})
    if resultado.deleted_count == 0:
        return jsonify({"erro": "Carro não encontrado"}), 404
    return jsonify({"mensagem": "Carro removido com sucesso"}), 200
