from src.dsproject import logger
from src.dsproject.pipeline.data_ingestion_pipeline import DataIngestiontrainingPipeline
from src.dsproject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.dsproject.pipeline.data_transforamtion_pipeline import DataTransformationPipeline
from src.dsproject.pipeline.model_train_pipeline import ModelTraininigPipeline

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

STAGE_NAME= "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj= DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Transformation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj= DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Trainer Stage'
try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj= ModelTraininigPipeline()
        obj.model_train()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e