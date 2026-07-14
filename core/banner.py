from core.version import APP_NAME, FULL_NAME, VERSION, BUILD


class Banner:

    @staticmethod
    def show():
        print("=" * 60)
        print(f"{APP_NAME:^60}")
        print(f"{FULL_NAME:^60}")
        print("-" * 60)
        print(f"Version : {VERSION}")
        print(f"Build   : {BUILD}")
        print("=" * 60)