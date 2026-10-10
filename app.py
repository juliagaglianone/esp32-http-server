from flask import Flask, request, jsonify

app = Flask(__name__)

dados_esp32 = {
    "temperatura": None,
    "botao": None
}

@app.route("/", methods=["GET"])
def inicio():
    return "Servidor HTTP das ESP32 funcionando!"

@app.route("/update", methods=["GET"])
def update():
    temperatura = request.args.get("temp")
    botao = request.args.get("button")

    dados_esp32["temperatura"] = temperatura
    dados_esp32["botao"] = botao

    print(f"Temperatura recebida: {temperatura} °C")
    print(f"Estado do botão recebido: {botao}")

    return jsonify({
        "status": "ok",
        "temperatura": temperatura,
        "botao": botao
    })

@app.route("/data", methods=["GET"])
def data():
    return jsonify(dados_esp32)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)