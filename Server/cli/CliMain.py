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

   

    '''def input_handler(self, input_str: str):
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
            print(cli.fail + "Unknown command. Type 'help' for a list of commands.")'''
    
    def input_handler(self, input_str: str):
        """Handles user input, executing commands or showing options."""
        if not input_str:
            return

        # Split the command and arguments
        parts = input_str.split(maxsplit=1)
        command = parts[0]
        args = parts[1] if len(parts) > 1 else ""

        if command == "run" and command in CommandFactory.server_command_registry:
            CommandFactory.run_command(self.current_command, args)

        elif command == "help":
            print(cli.success + "Showing available commands...")
            CommandFactory.showHelp()

        elif command == "show" and args == "options":
            if not self.current_command:
                print(cli.fail + "No command selected.")
                return
            CommandFactory.showOptions(self.current_command)

        elif command in CommandFactory.command_registry:
            self.current_command = command

        elif command == "back":
            self.current_command = None

        elif command == "exit":
            print(colored('[-]', 'red') + " Exiting C2 CLI...")
            exit()

        elif command == "set":
            if not self.current_command:
                print(cli.fail + "No command selected to set options for.")
                return
            if args:
                # Here, assuming `set_option` is a method that takes the full 'set' command
                # You might need to adjust based on your actual method implementation
                #set_option(self.current_command, args
                CommandFactory.set_option(self.current_command, args)
                
                
            else:
                print(cli.fail + "Invalid set command format. Use: set <option> <value>")

        elif command not in CommandFactory.command_registry and command not in CommandFactory.server_command_registry:
            print(command)
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
                prompt_text = HTML('<ansigreen>Talon C2</ansigreen> <ansiwhite>[</ansiwhite><ansired>{}</ansired><ansiwhite>] $ ></ansiwhite> '.format(cli.current_command))
            else:
                prompt_text = HTML('<ansigreen>Talon C2</ansigreen> <ansiwhite>$ ></ansiwhite> ')
            # Use prompt_toolkit's session to read input with support for history
            
            user_input = session.prompt(prompt_text)
            cli.input_handler(user_input)
    except KeyboardInterrupt:
        print("\nExiting C2 CLI...")
