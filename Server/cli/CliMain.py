from typing import Callable, Dict, Optional
from MTLS_Server import MTLS_Server
from CommandFactory import CommandFactory

class C2CLI:
    def __init__(self):
        self.commands: Dict[str, Callable] = {}
        self.current_command: Optional[str] = None
        self.register_commands()

   

    def input_handler(self, input_str: str):
        """Handles user input, executing commands or showing options."""
        if not input_str:
            return

        input_parts = input_str.split()
        command, args = input_parts[0], input_parts[1:]
        CommandFactory.use_command(command, args)

        

    def show_help(self, args):
        """Shows available commands."""
        print("Available Commands:")
        CommandFactory.showHelp()

    def show_options(self, args):
        """Shows options for the current command."""
        if not self.current_command or self.current_command not in self.command_options:
            print("No command selected or no options available for the current command.")
            return
        
        options = self.command_options[self.current_command]
        print(f"Options for {self.current_command}:")
        for option, value in options.items():
            print(f"- {option}: {value}")

# Main loop to run the CLI
if __name__ == "__main__":
    cli = C2CLI()
    CommandFactory = CommandFactory()
    try:
        while True:
            prompt = f"Talon C2 {cli.current_command}> " if cli.current_command else "Talon C2> "
            user_input = input(prompt)
            cli.input_handler(user_input)
    except KeyboardInterrupt:
        print("\nExiting C2 CLI...")
