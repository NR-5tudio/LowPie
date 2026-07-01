import json
from typing import Any, Dict, Union
import os

def Save(data: Dict[Any, Any], file_path: str) -> None:
    """
    Save dictionary data to a JSON file.
    
    Args:
        data: Dictionary to be saved as JSON
        file_path: Path to the output JSON file
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Failed to save JSON: {str(e)}")
        print("done..")

def Exists(path):
    return os.path.exists(path)

def Load(file_path: str) -> Dict[Any, Any]:
    """
    Load JSON data from a file into a dictionary.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Dictionary containing the loaded data
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load JSON: {str(e)}")

