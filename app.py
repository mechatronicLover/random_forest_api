from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS en todas las rutas

# Cargar modelo entrenado
modelo = joblib.load('modelo_rf_p_lab.pkl')

# Nombres de las columnas usadas en el entrenamiento
columnas = ['N_sensor', 'P_sensor', 'K_sensor', 'CE_lab']

@app.route('/', methods=['GET'])
def predecir_con_get():
    try:
        # Obtener parámetros desde la URL (query string)
        N = float(request.args.get('N_sensor'))
        P = float(request.args.get('P_sensor'))
        K = float(request.args.get('K_sensor'))
        CE = float(request.args.get('CE_lab'))

        # Crear un DataFrame con nombres de columnas
        entrada_df = pd.DataFrame([[N, P, K, CE]], columns=columnas)

        # Realizar la predicción
        prediccion = modelo.predict(entrada_df)[0]

        return jsonify({
            'P_lab_predicho': round(prediccion, 2),
            'entrada': {
                'N_sensor': N,
                'P_sensor': P,
                'K_sensor': K,
                'CE_lab': CE
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
