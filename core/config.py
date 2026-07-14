import json
from pathlib import Path


class ConfigManager:
    """
    Loads and provides access to EDITH configuration files.
    """

    def __init__(self):
        self.config_path = Path("config")
        self.settings = self._load("settings.json")
        self.modules = self._load("modules.json")
        self.personality = self._load("personality.json")
        self.startup = self._load("startup.json")

    def _load(self, filename):
        file_path = self.config_path / filename

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"[ERROR] Missing configuration file: {filename}")
            return {}
        except json.JSONDecodeError:
            print(f"[ERROR] Invalid JSON in: {filename}")
            return {}

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def is_module_enabled(self, module_name):
        return self.modules.get(module_name, False)

    def get_personality(self):
        return self.personality

    def get_startup(self):
        return self.startup