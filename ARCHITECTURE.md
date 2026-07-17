# EDITH Architecture

## Application Flow

main.py
    ↓
Shell.start()
    ↓
Startup.boot()
    ↓
EdithEngine.start()
    ↓
Screen.show()
    ↓
Terminal.start()

## Responsibilities

### main.py
Starts the EDITH application.

### shell.py
Coordinates the startup sequence.

### startup.py
Displays the banner and performs startup checks.

### engine.py
Initializes the EDITH core and loads modules.

### screen.py
Displays system information.

### terminal.py
Handles user input and passes commands to the command handler.

### commands.py
Processes user commands and executes the correct action.