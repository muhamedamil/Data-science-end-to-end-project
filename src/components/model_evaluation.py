import os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import joblib

from src.entity.config_entity import ModelEvaluationConfig
from src.utils.common import read_yaml,save_json,create_directories


os.environ["MLFLOW_TRACKING_URI"]= "https://dagshub.com/amilasnils008/Data-science-end-to-end-project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]= "amilasnils008"
os.environ["MLFLOW_TRACKING_PASSWORD"]= "f34b09f6dafe0c38be253c9456fe1018d05a4b88"

class ModelEvaluation:
    def __init__(self, config = ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2
    
    def log_to_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_X = test_data.drop([self.config.target_column], axis=1)
        test_Y = test_data[[self.config.target_column]]

        mlflow.set_tracking_uri(self.config.mlflow_uri)

        mlflow.set_experiment("ElasticNet_Regression_Experiment")

        with mlflow.start_run(run_name="Model_Evaluation_Run"):
            predicted_qualities = model.predict(test_X)
            rmse, mae, r2 = self.eval_metrics(test_Y, predicted_qualities)
            
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
    
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)
    
            # Model Signature
            from mlflow.models import infer_signature
            signature = infer_signature(test_X, model.predict(test_X))
    
            # Tags
            mlflow.set_tags({
                "model_type": "ElasticNet Regression",
                "developer": "Muhammed Amil",
                "dataset": "Wine Quality",
                "stage": "evaluation"
            })
    
            # Plot as Artifact
            import matplotlib.pyplot as plt
            plt.scatter(test_Y, predicted_qualities)
            plt.xlabel("Actual")
            plt.ylabel("Predicted")
            plt.title("Actual vs Predicted")
            plot_path = "reports/actual_vs_predicted.png"
            os.makedirs("reports", exist_ok=True)
            plt.savefig(plot_path)
            mlflow.log_artifact(plot_path)
    
            # Model Logging
            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="model",
                signature=signature,
                input_example=test_X.iloc[:1]
            )
