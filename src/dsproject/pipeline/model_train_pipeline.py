from src.dsproject.config.configuration import DataConfigurationManager
from src.dsproject.components.model_trainer import ModelTrainer
from src.dsproject import logger

STAGE_NAME='Model Trainer Stage'


class ModelTraininigPipeline:

    def __init__(self):
        pass
    def model_train(self):
        config=DataConfigurationManager()
        model_trainer_config=config.get_model_train_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.trainer()

if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj= ModelTraininigPipeline()
        obj.model_train()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e