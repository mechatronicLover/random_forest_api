from flask import Flask, request, jsonify
import joblib
import numpy as np

# Carga el modelo
modelo = joblib.load('modelo_rf_p_lab.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return "🌱 API de Predicción de Fósforo con Random Forest"

@app.route('/predecir', methods=['POST'])
def predecir():
    data = request.get_json()
    # Extraer datos en el mismo orden del entrenamiento
    entrada = np.array([
        data['N_sensor'],
        data['P_sensor'],
        data['K_sensor'],
        data['CE_lab']
    ]).reshape(1, -1)

    prediccion = modelo.predict(entrada)[0]
    return jsonify({'P_lab_predicho': round(prediccion, 2)})

if __name__ == '__main__':
    app.run(debug=True)
