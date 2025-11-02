import os
import pandas as pd
from src import logger 
from sklearn.linear_model import ElasticNet
from src.entity.config_entity import ModelTrainerConfig
import joblib


class ModelTrainer:
    def __init__(self, config = ModelTrainerConfig):
        self.config = config
        
    def train_model(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        train_X = train_data.drop([self.config.target_name],axis= 1)
        test_X = test_data.drop([self.config.target_name], axis = 1)
        
        train_Y = train_data[[self.config.target_name]]
        test_Y = test_data[[self.config.target_name]]
        
        lr = ElasticNet(alpha = self.config.alpha, l1_ratio = self.config.l1_ratio, random_state =42)
        lr.fit(train_X,train_Y)
        
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))