import platform


class Diagnostics:

    @staticmethod
    def check():

        print("\nRunning System Diagnostics...\n")

        print(f"Operating System : {platform.system()}")
        print(f"Release          : {platform.release()}")
        print(f"Machine          : {platform.machine()}")
        print(f"Processor        : {platform.processor()}")

        print("\nSystem Check Complete.\n")