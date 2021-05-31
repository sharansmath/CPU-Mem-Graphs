import yaml
import os

class ReadConfig():
    def __init__(self):
        # Read YAML file, create a relative path to config.yaml
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../config.yaml")
        with open(path, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        self.data = data_loaded

    def read_element(self, element1, element2="none"):
        # Read an element by name and return the value
        if element2 == "none": return self.data[element1]
        return self.data[element1][element2]
