import json
from pathlib import Path

BASE_PATH = Path.cwd().joinpath('webdriver', 'TestCases')

class JsonParser:    
    # Get json file content with "name" as the key
    # Return whole content if no "name" specified
    def read_json(self, file_name, name = None):
        path = BASE_PATH.joinpath(file_name)
        with open(path, 'r') as file:
            data = json.load(file)
            if not name:
                return data
            else:
                return data[name]