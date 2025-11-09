from ensure import ensure_annotations
from box import ConfigBox
import yaml
import sys
import os
from pathlib import Path
from typing import Any
from src.dsproject import logger
import json
import joblib
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Returns:
        ConfigBox: ConfigBox object containing the yaml file data
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """Creates a list of directories

    Args:
        path_to_directories (list): List of directory paths to be created
        verbose (bool, optional): Whether to log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations

def save_json(path:Path,data:dict):
    """Saves a dictionary as a json file

    Args:
        path (Path): Path to the json file
        data (dict): Dictionary to be saved
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations

def load_json(path:Path) -> ConfigBox:
    """Loads a json file and returns its content as a ConfigBox object
    Args:
        path (Path): Path to the json file

    Returns:
        ConfigBox: data as class attributes instead of dictionary
    """
    with open(path,'r') as f:
        data = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return data

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: data loaded from binary file
    """
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded from: {path}")
    return data