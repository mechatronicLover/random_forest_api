
# 🌿 random_forest_api

**Despliegue de modelo de Machine Learning para Agricultura de Precisión.**  
Esta API utiliza un modelo Random Forest entrenado para predecir los niveles de fósforo en el suelo (`P_lab`) a partir de mediciones de sensores de nutrientes (`N_sensor`, `P_sensor`, `K_sensor`) y conductividad eléctrica del suelo (`CE_lab`).

## 📁 Estructura del Proyecto

```
random_forest_api/
├── app.py                  # Archivo principal con la API Flask
├── modelo_entrenado.pkl    # Modelo Random Forest entrenado
├── requirements.txt        # Dependencias necesarias para correr la API
├── README.md               # Documentación del proyecto
└── test/
    └── request_test.py     # Ejemplo de petición para probar la API
```

## 🚀 Uso de la API

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/random_forest_api.git
cd random_forest_api
```

### 2. Instalar dependencias

Se recomienda usar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Ejecutar la API

```bash
python app.py
```

Esto iniciará un servidor local en `http://127.0.0.1:5000/`.

### 4. Hacer una predicción

Realiza una petición POST a la ruta `/predict` con un JSON que contenga:

```json
{
  "N_sensor": 10.5,
  "P_sensor": 8.3,
  "K_sensor": 12.1,
  "CE_lab": 1.85
}
```

#### Ejemplo con `curl`:

```bash
curl -X POST http://127.0.0.1:5000/predict   -H "Content-Type: application/json"   -d '{"N_sensor": 10.5, "P_sensor": 8.3, "K_sensor": 12.1, "CE_lab": 1.85}'
```

#### Respuesta esperada:

```json
{
  "P_lab_predicho": 7.94
}
```

## 🧪 Pruebas

Puedes usar `test/request_test.py` para validar el funcionamiento básico de la API.

---

Creado con ❤️ para apoyar la agricultura de precisión en el Perú.
