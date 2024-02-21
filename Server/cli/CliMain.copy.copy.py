from MTLS_Server import MTLS_Server

class C2CLI:
    def __init__(self):
        self.commands = {}
        self.current_command = None  # Track the current command context
        self.command_options = {
            "MTLS": {"HOST": None, "PORT": None}
        }
        self.register_command("help", self.show_help)
        self.register_command("show options", self.show_options)
        self.register_command("MTLS", self.start_mtls_server)

    def start_mtls_server(self, args):
        """Start an mTLS server command."""
        if self.current_command != "MTLS":
            self.current_command = "MTLS"
            print("Switched to Start MTLS command context. Type 'show options' to see available options.")
            return

        if len(args) == 2:
            host, port = args[0], int(args[1])
            # Initialize the MTLS_Server with paths to your certificates
            mtls_server = MTLS_Server('path/to/ca.crt', 'path/to/server.crt', 'path/to/server.key')
            mtls_server.start_server(host, port)
        else:
            print("Usage: [HOST] [PORT]")

    def register_command(self, command, callback):
        """Register a command and its callback function."""
        self.commands[command] = callback

    def input_handler(self, input_str):
        """Parse input and execute the corresponding command or switch context."""
        if not input_str:
            return  # Do nothing if the input is empty

        if input_str == "show options" and self.current_command:
            self.commands[input_str](None)  # Pass None as args for 'show options'
            return

        input_parts = input_str.split()
        command = input_parts[0]
        args = input_parts[1:]
        if command in self.commands:
            self.commands[command](args)
            if command != "show options":
                self.current_command = command  # Update the current command context
        else:
            print("Unknown command. Type 'help' for a list of commands.")

    def show_help(self, args):
        """Display available commands."""
        print("Available Commands:")
        for command in self.commands:
            print(f"- {command}")

    def show_options(self, args):
        """Display options for the current command."""
        if self.current_command and self.current_command in self.command_options:
            print(f"Options for {self.current_command}:")
            for option, value in self.command_options[self.current_command].items():
                print(f"- {option}: {value}")
        else:
            print("No command selected or no options available for the current command.")

# Usage Example
if __name__ == "__main__":
    cli = C2CLI()

    while True:
        try:
            prompt = f"Talon C2 {cli.current_command}> " if cli.current_command else "Talon C2> "
            user_input = input(prompt)
            cli.input_handler(user_input)
        except KeyboardInterrupt:
            print("\nExiting C2 CLI...")
            break
