from core.version import *
from core.engine import EdithEngine
from core.startup import Startup


def banner():

    print("=" * 60)
    print(APP_NAME)
    print(FULL_NAME)
    print(f"Version : {VERSION}")
    print(f"Build   : {BUILD}")
    print("=" * 60)


def main():

    Startup.boot()

    banner()

    engine = EdithEngine()

    engine.start()

    print()
    print("Welcome to EDITH.")


if __name__ == "__main__":
    main()