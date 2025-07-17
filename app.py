from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo
modelo = joblib.load("modelo_rf_p_lab.pkl")

@app.route('/')
def index():
    return "API del modelo Random Forest en Flask."

@app.route('/predict', methods=['POST'])
def predict():
    datos = request.get_json()
    entrada = np.array(datos['data']).reshape(1, -1)
    prediccion = modelo.predict(entrada)
    return jsonify({'prediccion': int(prediccion[0])})

if __name__ == '__main__':
    app.run(debug=True)
