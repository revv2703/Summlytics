import os
from box.exceptions import BoxValueError
import yaml
from Summlytics.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations     # ensure_annotations: checks if the function is called with the correct type of arguments, e.g. you can actually give string as an input where int is expected, it prevents you from doing that.
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as file:
            config = yaml.safe_load(file)
            logger.info(f"yaml file: {file} loaded successfully.")
            return ConfigBox(config)    # ConfigBox: lets me access the keys using dot notation -> config.key instead of config['key']
    except BoxValueError as e:
        logger.error(f"Error reading the yaml file: {e}")
        raise e
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading the yaml file: {e}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Create directories if they don't exist.
    """
    for directory in path_to_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            if verbose:
                logger.info(f"Directory: {directory} created.")
        else:
            if verbose:
                logger.info(f"Directory: {directory} already exists.")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file or directory.
    """
    return f"{os.path.getsize(path)/1024} kB"
    # 1:20:00