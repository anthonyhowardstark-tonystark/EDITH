from core.config import ConfigManager
from core.logger import Logger


class ModuleLoader:

    def __init__(self, manager):
        self.manager = manager
        self.config = ConfigManager()

    def load_modules(self):

        Logger.info("Loading Modules...")

        for module, enabled in self.config.modules.items():

            if enabled:

                self.manager.register(module.capitalize())