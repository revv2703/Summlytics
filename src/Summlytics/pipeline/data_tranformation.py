from Summlytics.config.configuration import ConfigurationManager
from Summlytics.components.data_transformation import DataTransformation
from Summlytics.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info("Running Data Transformation Training Pipeline")

        try:
            
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.convert()

        except Exception as e:
            logger.error(e)
            raise e

        logger.info("Data Transformation Training Pipeline Completed")