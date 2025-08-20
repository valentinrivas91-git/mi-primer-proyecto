from flask import Flask, request, render_template, jsonify
import datetime

app = Flask(__name__)

# Guardar datos en memoria
datos = []

@app.route("/guardar", methods=["POST"])
def guardar():
    temp = request.form.get("temp")
    hum = request.form.get("hum")
    now = datetime.datetime.now().strftime("%H:%M:%S")

    datos.append({"hora": now, "temp": temp, "hum": hum})

    # Limitar a últimos 20 registros
    if len(datos) > 20:
        datos.pop(0)

    return "OK", 200

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(datos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)