import os
import yaml
import json
import joblib

from src import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns it

    Args:
        path_to_yaml (Path): _description_

    Raises:
        value_error : if yaml file is empty 
        e : empty_file
    Returns:
        ConfigBox : ConfigBox(type)
    """
    
    try :
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError("yaml file is empty")
    except Exception as e :
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose = True):
    """create a list of directories

    Args:
        path_to_directories (list): path to create the directories 
        verbose (bool, optional): tp track the process 
    """
    for path in path_to_directories:
        if path !="":
            os.makedirs(path,exist_ok= True)
        if verbose :
            logger.info(f"created directory for {path}")
            
            
@ensure_annotations
def save_json(path:Path,data : dict):
    """save the json data

    Args:
        path (Path): path to save the json data
        data (dict): data to be saved in the json
    """
    with open(path,"w") as f :
        json.dump(data, indent=4)
    logger.info(f"json file saved at path :{path}")
    
    
@ensure_annotations
def load_json(path:Path) -> ConfigBox :
    """to load the json data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f :
        content = json.load(f)
    logger.info(f"json file loaded succesfully")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path:Path, data : Any):
    """
    save the binary files 

    Args:
        path (Path): path the data should be saved
        data (Any): the binary data to be stored
    """
    
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at path : {path}")
    