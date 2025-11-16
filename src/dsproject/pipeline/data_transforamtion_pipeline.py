from src.dsproject.config.configuration import DataConfigurationManager
from src.dsproject.components.data_transformation import DataTransformation
from src.dsproject import logger
from pathlib import Path
STAGE_NAME='Data Transforamtion Stage'

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'),'r') as f:
                status= f.read().split(" ")[-1]
                if status=="True":
                    config=DataConfigurationManager()
                    data_transformation_config=config.get_transformation_config()
                    data_transformation=DataTransformation(config=data_transformation_config)
                    data_transformation.train_test_splitting()
                else:
                     raise Exception("Data is not Valid")
        except Exception as e:
            logger.exception(e)
            raise e

        
                

                        
if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj= DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e