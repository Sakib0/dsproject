import os
import urllib.request as request
from src.dsproject import logger
import zipfile
from src.dsproject.entity.config_entity import (DataIngestionConfig)

# Data Ingestion components
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # Download the zip file
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, 
                filename=self.config.local_data_file
            )
            logger.info(f"File: {filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {os.path.getsize(self.config.local_data_file)}")
    # Unzip the downloaded file
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)