from core.logger import Logger
from core.manager import ModuleManager


class EdithEngine:

    def __init__(self):
        self.manager = ModuleManager()

    def start(self):

        Logger.info("Initializing EDITH...")

        self.manager.register("Logger")
        self.manager.register("Module Manager")
        self.manager.register("Core Engine")

        print()

        Logger.success("System Status : ONLINE")