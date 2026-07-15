from core.banner import Banner
from core.diagnostics import Diagnostics
from core.engine import EdithEngine
from core.config import ConfigManager

config = ConfigManager()

class Startup:

    @staticmethod
    def boot():

        Banner.show()

        Diagnostics.check()

        print("EDITH is Online.")
        print("Awaiting your command...")