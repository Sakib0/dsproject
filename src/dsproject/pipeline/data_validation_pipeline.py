from src.dsproject.config.configuration import DataConfigurationManager
from src.dsproject.components.data_validation import DataValidation
from src.dsproject import logger

STAGE_NAME='Data Transforamtion Stage'

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):

        config=DataConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


    
if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj= DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e