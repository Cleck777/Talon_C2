from typing import Callable, Dict, Optional
from CommandFactory import CommandFactory
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML, ANSI
from termcolor import colored


class C2CLI:
    
    pr = colored('Talon C2', 'green') 
    success = colored('[+] ', 'green')
    fail = colored('[-] ', 'red')
    CommandFactory = CommandFactory()
    def __init__(self):
        self.commands: Dict[str, Callable] = {}
        self.current_command: Optional[str] = None

   

    def input_handler(self, input_str: str):
        """Handles user input, executing commands or showing options."""
        if not input_str:
            return

        #command, *args = input_str.split(maxsplit=1)
        command = input_str
        
        if command == "run" and command in CommandFactory.server_command_registry:
            CommandFactory.run_command(command, args)
        
        if command == "help":
            print(cli.success + "Showing available commands...")
            CommandFactory.showHelp()
        if command == "show options":
            if not self.current_command:
                print(cli.fail + "No command selected.")
                return
            CommandFactory.showOptions(self.current_command)
        if command in CommandFactory.command_registry:
            self.current_command = command
        if command == "back":
            self.current_command = None
        if command == "exit":
            print(colored('[-]', 'red') + " Exiting C2 CLI...")
            exit()
        if command not in CommandFactory.command_registry and command not in CommandFactory.server_command_registry:
            print(cli.fail + "Unknown command. Type 'help' for a list of commands.")
        



            
        

        

    def show_help(self, args):
        """Shows available commands."""
        print(cli.success + "Showing available commands.")
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
    def switch_command_context(self, command: str):
        """Switches the current command context."""
        self.current_command = command

# Main loop to run the CLI
if __name__ == "__main__":
    cli = C2CLI()
    session = PromptSession(history=InMemoryHistory())
    try:
        while True:
            if cli.current_command:
                prompt_text = HTML('<ansigreen>Talon C2</ansigreen> <ansiwhite>[{}] Current command $ ></ansiwhite> '.format(cli.current_command))
            else:
                prompt_text = HTML('<ansigreen>Talon C2</ansigreen> <ansiwhite>$ ></ansiwhite> ')
            # Use prompt_toolkit's session to read input with support for history
            
            user_input = session.prompt(prompt_text)
            cli.input_handler(user_input)
    except KeyboardInterrupt:
        print("\nExiting C2 CLI...")
