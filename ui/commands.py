import os
from datetime import datetime

from core.version import VERSION, BUILD


class CommandHandler:

    def execute(self, command):

        command = command.lower().strip()

        if command == "help":
            self.help()

        elif command == "version":
            print(f"\nEDITH Version {VERSION}")
            print(f"Build {BUILD}\n")

        elif command == "status":
            print("\nSystem Status : ONLINE\n")

        elif command == "time":
            current_time = datetime.now()

            print("\nCurrent Time")
            print(current_time.strftime("%I:%M:%S %p"))
            print()

        elif command == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        elif command == "about":
            print("""
Executive Digital Intelligence & Task Handler

Developer : Raizul Haque Areeb Ahamed

Language : Python

Architecture : Modular AI Operating System
""")

        elif command == "exit":
            return False

        else:
            print("\nUnknown command.")
            print("Type 'help' to view available commands.\n")

        return True

    def help(self):

        print("""
Available Commands

help
about
version
status
time
clear
exit
""")