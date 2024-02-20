import sys
sys.path.append('/home/half/Desktop/honor/Server/cli')
from MTLS_Server import MTLS_Server

class C2CLI:
    def __init__(self):
        self.commands = {}
        self.register_command("help", self.show_help)

    def start_mtls_server(self, args):
        """Start an mTLS server command."""
        if len(args) != 2:
            print("Usage: start_mtls_server [HOST] [PORT]")
            return
        
        host, port = args[0], int(args[1])
        # Initialize the MTLS_Server with paths to your certificates
        mtls_server = MTLS_Server('path/to/ca.crt', 'path/to/server.crt', 'path/to/server.key')
        mtls_server.start_server(host, port)


    def register_command(self, command, callback):
        """Register a command and its callback function."""
        self.commands[command] = callback

    def input_handler(self, input_str):
        """Parse input and execute the corresponding command."""
        if not input_str:
            return  # Do nothing if the input is empty

        input_parts = input_str.split()
        command = input_parts[0]
        args = input_parts[1:]
        if command in self.commands:
            self.commands[command](args)
        else:
            print("Unknown command. Type 'help' for a list of commands.")

    def show_help(self, args):
        """Display available commands."""
        print("Available Commands:")
        for command in self.commands:
            print(f"- {command}")

    # Example command method
    def add_command_example(self, args):
        """Example of adding a new command."""
        print(f"Executing example command with args: {args}")

# Usage Example
if __name__ == "__main__":
    cli = C2CLI()
    cli.register_command("example", cli.add_command_example)
    cli.register_command("Start MTLS", cli.add_command_example)

    while True:
        try:
            user_input = input("Talon C2> ")
            cli.input_handler(user_input)
        except KeyboardInterrupt:
            print("\nExiting C2 CLI...")
            break
