from Summlytics.config.configuration import ConfigurationManager
from Summlytics.components.train_model import TrainModel
from Summlytics.logging import logger

class TrainModelTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info("Running Model Training Pipeline")

        try:
            
            config = ConfigurationManager()
            model_trainer_config = config.get_train_model_config()
            model_trainer_config = TrainModel(config=model_trainer_config)
            model_trainer_config.train()

        except Exception as e:
            logger.error(e)
            raise e

        logger.info("Model Training Pipeline Completed")