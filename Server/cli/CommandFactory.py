from MTLS_Controller import MTLS_Controller

current_command = None
class CommandFactory:
    # Mapping of command strings to command class constructors
    command_registry = {
    "MTLS": {
        "command": MTLSCommand,
        "options": {
            "ip": "value2",
            "port": "value1",
            "port": "value1",
            # Add more options as needed
        },
    },
    
}
    server_command_registry = {
    "Help": {
        "description": "Displays available commands."
    },
    "ShowOptions": {
        "description": "Displays options for the current command."
    },
    "Run": {
        "description": "Runs the specified command."
    },
    "Back": {
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
        
    def showHelp(self):
        print("Available Commands:")
        for command in self.command_registry:
            print(f"- {command}")

    def use_command(self, command_name: str, args: list):
        current_command = command_name
        prompt = f"Talon C2 {command_name}> " 
        
#if __name__ == "__main__":
    