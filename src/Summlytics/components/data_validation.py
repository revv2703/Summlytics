from Summlytics.logging import logger
from Summlytics.entity import DataValidationConfig
import json
import os

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    # def validate_all_files(self):
    #     """Validate all files in the data directory"""
    #     # return all([validate_file() for validate_file in [self.validate_file(file) for file in self.config.ALL_REQUIRED_FILES]])
    #     return all(self.validate_file(file) for file in self.config.ALL_REQUIRED_FILES)
    
    # def validate_file(self, file: str) -> bool:
    #     """Validate a file in the data directory"""
    #     file_path = Path(self.config.root_dir + "/" + file)
    #     if not file_path.exists():
    #         logger.error(f"Missing file: {file_path}")
    #         return False
    #     logger.info(f"File {file_path} exists")
    #     return True
        
    # def validate_all_files(self):
    #     """Validate all files in the data directory"""
    #     try:
    #         validation_status = None

    #         file_loc = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

    #         for file in file_loc:
    #             if file not in self.config.ALL_REQUIRED_FILES:
    #                 validation_status = False
    #                 with open(self.config.FILE_STATUS, "w") as f:
    #                     f.write(f"Validation status: {validation_status}")
    #             else:
    #                 validation_status = True
    #                 with open(self.config.FILE_STATUS, "w") as f:
    #                     f.write(f"Validation status: {validation_status}")

    #         return validation_status
        
    #     except Exception as e:
    #         logger.error(f"Validation failed: {e}")
    #         return False
    
    def validate_all_files(self) -> bool:
        try:
            all_valid = all(file in self.config.ALL_REQUIRED_FILES for file in os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset")))
            with open(self.config.FILE_STATUS, "w") as f:
                json.dump({"validation_status": all_valid}, f)
            return all_valid
        except Exception as e:
            logger.error(f"Validation failed: {e}")
            return False