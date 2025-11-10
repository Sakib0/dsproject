from src.dsproject import logger
from src.dsproject.pipeline.data_ingestion_pipeline import DataIngestiontrainingPipeline
import os

STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj= DataIngestiontrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e