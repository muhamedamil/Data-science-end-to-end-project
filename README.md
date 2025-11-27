

This repository demonstrates a complete **Data Science / Machine Learning pipeline** with workflows for ingestion, validation, transformation, model training, and evaluation — along with a simple **Flask web application** to deploy and interact with the trained model.

---

## 🧠 Project Overview

This project covers the full lifecycle of a machine learning workflow — from raw data to deployment — built with tools like **MLflow**, **DagsHub**, and **Flask** for web deployment.

---

## 🛠 ML Pipeline Workflows

The project follows a modular and well-structured ML workflow:

1. **Data Ingestion** – Collect and import raw data.  
2. **Data Validation** – Ensure data quality and schema consistency.  
3. **Data Transformation** – Perform feature engineering and preprocessing.  
4. **Model Training** – Train and tune machine learning models.  
5. **Model Evaluation** – Track and visualize experiments using **MLflow** and **DagsHub**.  
6. **Model Deployment** – Deploy the trained model using a **Flask web app**.

---

## ⚙️ Development Workflow

To update and maintain the pipeline, follow these steps:

1. Update `config.yaml` – Configure project parameters.  
2. Update `schema.yaml` – Define and validate the data schema.  
3. Update `params.yaml` – Set model parameters or hyperparameters.  
4. Update entities – Modify data/model entities as needed.  
5. Update **Configuration Manager** in `src/config` – Manage configuration loading.  
6. Update components – Add or enhance data processing/modeling modules.  
7. Update pipeline – Integrate new components into the main pipeline.  
8. Update `main.py` – Control end-to-end pipeline execution.

---

## 🌐 Flask Web Application

The project includes a simple **Flask-based web interface** that allows users to input wine characteristics and get the predicted wine quality.

### **Files**
- `app.py` → Flask server entry point.  
- `templates/predict_form.html` → Front-end form for user input.  
- `templates/result.html` → Displays the prediction result.

### **How it works**
1. User fills in feature values (e.g., acidity, pH, alcohol).  
2. Flask app sends these inputs to the backend prediction pipeline.  
3. The pipeline loads the trained model and returns the quality prediction.  
4. The prediction result is displayed on the web page.

### **To run the Flask app**
```bash
# Activate your virtual environment
venv\\Scripts\\activate   # on Windows
# or
source venv/bin/activate  # on macOS/Linux

# Run Flask app
python app.py
