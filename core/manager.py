from core.logger import Logger


class ModuleManager:

    def __init__(self):
        self.modules = []

    def register(self, module_name):
        self.modules.append(module_name)
        Logger.success(f"{module_name} Loaded")

    def show_modules(self):
        Logger.info("Loaded Modules:")

        for module in self.modules:
            print(f"   • {module}")