from Summlytics.constants import *
from Summlytics.utils.common import read_yaml, create_directories
from Summlytics.entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config.data_validation

        create_directories([config.root_dir])
        
        return DataValidationConfig(
            root_dir = config.root_dir,
            FILE_STATUS = config.FILE_STATUS,
            ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES
        )
    
    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation

        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
        )