"""
EDITH Shell

Coordinates the startup of EDITH.
"""

from core.engine import EdithEngine
from core.startup import Startup
from ui.screen import Screen
from ui.terminal import Terminal


class Shell:

    def start(self):

        Startup.boot()

        engine = EdithEngine()
        engine.start()

        Screen.show()

        terminal = Terminal()
        terminal.start()