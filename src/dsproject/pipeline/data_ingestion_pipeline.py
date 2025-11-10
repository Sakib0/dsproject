from src.dsproject.config.configuration import DataConfigurationManager
from src.dsproject.components.data_ingestion import DataIngestion
from src.dsproject import logger

STAGE_NAME= "Data Ingestion Stage"
class DataIngestiontrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):

        config=DataConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()
    

if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj= DataIngestiontrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
