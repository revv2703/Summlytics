from Summlytics.pipeline.data_ingestion import DataIngestionTrainingPipeline
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