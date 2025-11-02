from src import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline


STAGE_NAME = "Data Ingestion Stage"


try :
    logger.info(f"<<<<stage {STAGE_NAME} started >>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data validation stage"

try :
    logger.info(f">>>>>stage {STAGE_NAME} is started<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>stage {STAGE_NAME} is completed")
except Exception as e :
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try :
    logger.info(f">>>>>>stage {STAGE_NAME} is started")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>stage {STAGE_NAME} is completed")
except Exception as e :
    logger.exception(e)
    raise e


STAGE_NAME = "Model training Stage"


try:
    logger.info(f">>>>>>stage {STAGE_NAME} is started")
    obj = ModelTrainerPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>stage {STAGE_NAME} is completed")
except Exception as e :
    logger.exception(e)
    raise e
    
