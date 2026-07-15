from core.version import *
from ui.shell import Shell

def banner():

    print("=" * 60)
    print(APP_NAME)
    print(FULL_NAME)
    print(f"Version : {VERSION}")
    print(f"Build   : {BUILD}")
    print("=" * 60)


from ui.shell import Shell


def main():

    shell = Shell()
    shell.start()

if __name__ == "__main__":
    main()