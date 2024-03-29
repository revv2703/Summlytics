from Summlytics.pipeline.data_ingestion import DataIngestionTrainingPipeline
from Summlytics.pipeline.data_tranformation import DataTransformationTrainingPipeline
from Summlytics.pipeline.data_validation import DataValidationTrainingPipeline
from Summlytics.pipeline.model_evaluation import ModelEvaluationTrainingPipeline
from Summlytics.pipeline.train_model import TrainModelTrainingPipeline
from Summlytics.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"Starting {STAGE_NAME}")

    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.run()
    
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"Starting {STAGE_NAME}")

    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.run()
    
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"Starting {STAGE_NAME}")

    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.run()
    
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Model Train stage"

try:
    logger.info(f"Starting {STAGE_NAME}")

    model_train_pipeline = TrainModelTrainingPipeline()
    model_train_pipeline.run()
    
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f"Starting {STAGE_NAME}")

    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    model_evaluation_pipeline.run()
    
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e
