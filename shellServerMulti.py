import socketserver
import argparse
import sys

class BotHandler(socketserver.BaseRequestHandler):
    def setup(self):
        """Setup function to initialize any state before handling requests."""
        self.commands_file = self.server.commands_file

    def handle(self):
        """Handle function called whenever data is received from a client."""
        try:
            # Receive data from the client
            self.data = self.request.recv(1024).strip()
            print(f"Bot with IP {self.client_address[0]} sent:")
            print(self.data.decode("utf-8"))

            # Open the commands file and send each command to the client
            with open(self.commands_file, 'r') as f:
                for command in f:
                    command = command.strip()
                    if command:  # Avoid sending empty lines
                        self.request.sendall(command.encode())
                        response = self.request.recv(1024).decode()
                        print(f"Response from bot: {response}")
        except Exception as e:
            print(f"Error handling client {self.client_address}: {e}")

class CustomTCPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, commands_file):
        super().__init__(server_address, RequestHandlerClass)
        self.commands_file = commands_file

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Bot server to send commands to connected bots.")
    parser.add_argument("file", help="Path to the commands file.")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind the server (default: 0.0.0.0).")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind the server (default: 8000).")
    args = parser.parse_args()

    # Ensure the commands file exists
    try:
		
        with open(args.file, 'r') as _:
            pass
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Unable to read file '{args.file}': {e}")
        sys.exit(1)

    # Start the server
    HOST, PORT = args.host, args.port
    try:
        with CustomTCPServer((HOST, PORT), BotHandler, args.file) as server:
            print(f"Server running on {HOST}:{PORT}, using commands file: {args.file}")
            server.serve_forever()
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)
