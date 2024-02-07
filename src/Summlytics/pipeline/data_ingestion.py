from Summlytics.config.configuration import ConfigurationManager
from Summlytics.components.data_ingestion import DataIngestion
from Summlytics.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info("Running Data Ingestion Training Pipeline")

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.download_data()
        data_ingestion.unzip_data()

        logger.info("Data Ingestion Training Pipeline Completed")