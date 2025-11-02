import os
import urllib.request as request 
import zipfile

from src.config.configuration import (DataIngestionConfig)
from src import logger



## Component : Data-Ingestion
class DataIngestion :
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    
    # Downloading the zip files Q
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{file_name} download!, with following info :{headers}")
        else:
            logger.info(f"File already existed")
            
    def extract_zip_file(self):
        """
        this function will helps to extract the zip files
        zip_file_path :str
        function return None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref :
            zip_ref.extractall(unzip_path)
            