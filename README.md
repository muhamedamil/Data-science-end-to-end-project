# End-to-End Data Science Project

This repository demonstrates a complete **Data Science / Machine Learning pipeline** with workflows for ingestion, validation, transformation, model training, and evaluation.

---

## 🛠 ML Pipeline Workflows

The project follows a structured ML workflow:

1. **Data Ingestion** – Collecting and importing raw data.
2. **Data Validation** – Checking data quality and consistency.
3. **Data Transformation** – Feature engineering and data preprocessing.
4. **Model Training** – Training machine learning models.
5. **Model Evaluation** – Evaluating models using tools like **MLflow** and **DagsHub**.

---

## ⚙️ Development Workflow

To update and maintain the pipeline, follow these steps:

1. Update `config.yaml` – Configure project parameters.
2. Update `schema.yaml` – Define and validate data schema.
3. Update `params.yaml` – Set hyperparameters or model parameters.
4. Update entities – Update data or model entities as needed.
5. Update **Configuration Manager** in `src/config` – Handle configurations programmatically.
6. Update components – Modify or add new pipeline components.
7. Update pipeline – Integrate components into the main pipeline.
8. Update `main.py` – Orchestrate the execution of the entire pipeline.

---

## 📌 Notes

- This project is modular and scalable for end-to-end machine learning workflows.
- Integrates best practices like configuration management, validation, and experiment tracking.
