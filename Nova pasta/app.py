from flask import Flask, request, jsonify
from dataclasses import dataclass, asdict
from typing import List

app = Flask(__name__)

@dataclass
class Sinal:
    par: str
    direcao: str
    forca: int
    horario: str

# Banco de sinais em memória (para teste)
sinais_sniper: List[Sinal] = []

@app.route("/sinais", methods=["GET"])
def listar_sinais():
    return jsonify([asdict(s) for s in sinais_sniper])

@app.route("/novo-sinal", methods=["POST"])
def adicionar_sinal():
    dados = request.get_json()
    sinal = Sinal(**dados)
    sinais_sniper.insert(0, sinal)
    if len(sinais_sniper) > 10:
        sinais_sniper.pop()  # Limita a 10 sinais mais recentes
    return jsonify({"mensagem": "Sinal sniper adicionado com sucesso"})

@app.route("/")
def raiz():
    return jsonify({"mensagem": "API Sniper Online - Em execução"})

if __name__ == "__main__":
    app.run(debug=True)
