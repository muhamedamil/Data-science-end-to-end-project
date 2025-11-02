from src.config.configuration import ConfigurationManager
from src.components.model_train import ModelTrainer
from src import logger


STAGE_NAME = "model training stage"


class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = ConfigurationManager()
        model_train_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_train_config)
        model_trainer.train_model()
        
