from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  #CORS para todas las rutas

# Cargar modelo entrenado
modelo = joblib.load('modelo_rf_p_lab.pkl')

@app.route('/', methods=['GET'])
def predecir_con_get():
    try:
        # Obtener parámetros desde la URL (query string)
        N = float(request.args.get('N_sensor'))
        P = float(request.args.get('P_sensor'))
        K = float(request.args.get('K_sensor'))
        CE = float(request.args.get('CE_lab'))

        # Organizar entrada en el orden exacto del entrenamiento
        entrada = np.array([[N, P, K, CE]])
        prediccion = modelo.predict(entrada)[0]

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
