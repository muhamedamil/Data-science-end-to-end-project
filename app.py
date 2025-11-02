from flask import Flask, render_template, request
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

# Route for home page (form input)
@app.route('/', methods=['GET'])
def home_page():
    return render_template('predict_form.html')  # form page for user input

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # mapping: form name → model feature name
        rename_map = {
            "fixed_acidity": "fixed acidity",
            "volatile_acidity": "volatile acidity",
            "citric_acid": "citric acid",
            "residual_sugar": "residual sugar",
            "chlorides": "chlorides",
            "free_sulfur_dioxide": "free sulfur dioxide",
            "total_sulfur_dioxide": "total sulfur dioxide",
            "density": "density",
            "pH": "pH",
            "sulphates": "sulphates",
            "alcohol": "alcohol"
        }

        # Rename keys to match model training
        converted = {rename_map[k]: float(v) for k, v in data.items()}
        df = pd.DataFrame([converted])

        prediction_pipeline = PredictionPipeline()
        prediction = prediction_pipeline.predict(df)[0]

        return {"prediction": round(float(prediction), 2)}

    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
