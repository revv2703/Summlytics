from Summlytics.config.configuration import ConfigurationManager
from Summlytics.components.model_evaluation import ModelEvaluation
from Summlytics.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info("Running Model Evaluation Training Pipeline")

        try:
            
            config_manager = ConfigurationManager()
            model_eval_config = config_manager.get_model_eval_config()
            model_evaluation = ModelEvaluation(model_eval_config)
            model_evaluation.evaluate()

        except Exception as e:
            logger.error(e)
            raise e

        logger.info("Model Evaluation Training Pipeline Completed")