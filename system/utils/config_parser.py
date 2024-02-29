import json
from system.models.config import ConfigModel


class ConfigParser:
    config_file: str = None
    data: ConfigModel
    raw_data: str

    def __init__(self, config_file: str):
        self.config_file = config_file
        with open(self.config_file, encoding="utf8") as f:
            self.raw_data = json.loads(f.read())
            self.data = ConfigModel(self.raw_data)
