from flask import Flask, request, jsonify

app = Flask(__name__)

estado_botao = None

@app.route("/", methods=["GET"])
def inicio():
    return "Servidor HTTP das ESP32 funcionando!"

@app.route("/update", methods=["GET"])
def update():
    global estado_botao

    estado_botao = request.args.get("button")

    print(f"Estado do botão recebido: {estado_botao}")

    return jsonify({
        "botao": estado_botao
    })

@app.route("/data", methods=["GET"])
def data():
    return jsonify({
        "botao": estado_botao
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)