import urllib.request as request
import os
from pathlib import Path
import zipfile
from Summlytics.logging import logger
from Summlytics.utils.common import get_size
from Summlytics.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_data(self):
        logger.info("Downloading data")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_url, self.config.local_data_file)
            logger.info(f"{filename} downloaded with the following information: \n{headers}")
        else:
            logger.info(f"Data file already exists at {self.config.local_data_file} of size: {get_size(Path(self.config.local_data_file))}")


    def unzip_data(self):
        logger.info("Unzipping data")

        os.makedirs(self.config.unzip_dir, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Unzipped data to {self.config.unzip_dir}")