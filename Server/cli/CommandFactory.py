from MTLS_Controller import MTLS_Controller
import pandas as pd
from OptionsTable import OptionsTable
current_command = None
class CommandFactory:

    # Create a table instance
    MTLSTable = OptionsTable(title="MTLS Server Options",
                        column_names=["Option", "Current Setting", "Required", "Description"])

    # Add rows
    MTLSTable.add_row("ip", "", "Not Required", "IP address to bind the server to. Defaults to")
    MTLSTable.add_row("port", "", "Required", "Port to bind the server to.")
    MTLSTable.add_row("private key", "path/to/key", "Required", "Path to the private key file.")
    MTLSTable.add_row("public key", "path/to/pubkey", "Required", "Path to the public key file.")

    # Modify a row (e.g., update the current setting for 'ip')
    

    
    # Mapping of command strings to command class constructors
    command_registry = {
    "MTLS": {
        "description": "Start an mTLS server.",
        "options": {
            "ip": "Not Required",
            "port": "Required",
            "private key": "Required",
            "public key": "Required"
            # Add more options as needed
        },
        "location": {
            "ip": 0,
            "port": 1,
            "private key": 2,
            "public key": 3
            # Add more options as needed
        },
        "Table": MTLSTable
        },
    }
    

    server_command_registry = {
    "help": {
        "description": "Displays available commands."
    },
    "show options": {
        "description": "Displays options for the current command."
    },
    "run": {
        "description": "Runs the specified command."
    },
    "back": {
        "description": "Exits the current command context."
    }

        
    }

    @staticmethod
    def create_command(command_name: str):
        command_class = CommandFactory.command_registry.get(command_name)
        if command_class:
            return command_class()  # Dynamically create an instance of the command class
        else:
            print("Unknown command:", command_name)
            return None
    def set_Command(table : OptionsTable,command : str, option :str, setting : str):

        CommandFactory.table.modify_row(CommandFactory.command_registry[command]["location"][option], setting)
    @staticmethod    
    def showHelp():
        print("Available Commands:")
        for command in CommandFactory.command_registry:
            print(f"- {command}")
            print(f"  - {CommandFactory.command_registry[command]['description']}")
        print("Server Commands:")
        for command in CommandFactory.server_command_registry:
            print(f"- {command}")
            print(f"  - {CommandFactory.server_command_registry[command]['description']}")
    
    @staticmethod
    def use_command(command_name: str, args: list, current_command: str):
        CLIMain.current_command = command_name
        print("use Command Hit")
    @staticmethod
    def showOptions(current_command: str):
        if not current_command or current_command not in CommandFactory.command_registry:
            print("No command selected or no options available for the current command.")
            return
        table = CommandFactory.command_registry[current_command]["Table"]
        table.display()
        #options = CommandFactory.command_registry[current_command]["options"]
        #print(f"Options for {current_command}:")
        #for option, value in options.items():
         #   print(f"- {option}: {value}")
        

#if __name__ == "__main__":
    