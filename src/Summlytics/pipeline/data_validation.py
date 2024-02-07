from Summlytics.config.configuration import ConfigurationManager
from Summlytics.components.data_validation import DataValidation
from Summlytics.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info("Running Data validation Training Pipeline")

        try:
            
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_all_files()

        except Exception as e:
            logger.error(e)
            raise e

        logger.info("Data validation Training Pipeline Completed")