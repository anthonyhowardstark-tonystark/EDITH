from datetime import datetime
from core.version import APP_NAME, FULL_NAME, VERSION, BUILD


class Screen:

    @staticmethod
    def show():

        now = datetime.now()

        print("=" * 65)
        print(APP_NAME.center(65))
        print(FULL_NAME.center(65))
        print("=" * 65)

        print(f" Version : {VERSION}")
        print(f" Build   : {BUILD}")
        print(f" Date    : {now.strftime('%d %B %Y')}")
        print(f" Time    : {now.strftime('%I:%M:%S %p')}")
        print(f" Status  : ONLINE")

        print("=" * 65)