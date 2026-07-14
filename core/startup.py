from core.banner import Banner
from core.diagnostics import Diagnostics
from core.engine import EdithEngine
from core.config import ConfigManager

config = ConfigManager()

class Startup:

    @staticmethod
    def boot():

        Banner.show()

        engine = EdithEngine()
        engine.start()

        Diagnostics.check()

        print("EDITH is Online.")
        print("Awaiting your command...")

if config.get_startup().get("show_banner", True):
    Banner.show()