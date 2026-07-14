from unittest import loader

from core.logger import Logger
from core.manager import ModuleManager
from core.module_loader import ModuleLoader


class EdithEngine:

    def __init__(self):
        self.manager = ModuleManager()

    def start(self):

        Logger.info("Initializing EDITH...")

        self.manager.register("Logger")
        self.manager.register("Module Manager")
        self.manager.register("Core Engine")

        loader = ModuleLoader(self.manager)

        loader.load_modules()

        print()

        Logger.success("System Status : ONLINE")