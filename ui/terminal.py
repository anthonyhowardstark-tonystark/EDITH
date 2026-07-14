from ui.commands import CommandHandler


class Terminal:

    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):

        running = True

        while running:

            command = input("EDITH > ")

            running = self.command_handler.execute(command)