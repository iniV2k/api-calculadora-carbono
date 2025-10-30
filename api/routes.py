from flask import Blueprint, request, jsonify

from .services.calculation_service import calcular_pegada_carbono
from .data.fatores_emissao import fatoresEmissao

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/calcular", methods=["POST"])
def handle_calcular_pegada():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Nenhum dado recebido"}), 400
        
        response_data = calcular_pegada_carbono(data)
        
        return jsonify(response_data), 200
    except Exception as e:
        print(f"Erro inesperado na rota /calcular: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500
    
@api_bp.route("/fatores", methods=["GET"])
def get_fatores():
    try:
        return jsonify(fatoresEmissao()), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500