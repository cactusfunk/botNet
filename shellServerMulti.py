import socketserver
import sys

#extend BaseRequestHandler into BotHandler, with a custom handle function
#Whenever a client connects to the server, create an internal thread and instantiate one BotHandler instance per connection
class BotHandler(socketserver.BaseRequestHandler):
	print(sys.argv) 
	#function called whever BotHandler receives data from a client
	def handle(self):
		#strip the spaces from the ends of the data received and set to a variable
		self.data = self.request.recv(1024).strip()
		#print the clients IP address and port number
		print("Bot with IP {} sent:".format(self.client_address[0]))
		print(self.data)
		#send the client all the information converted to uppercase
		#commenting this out as instead of this I want so send the command from the commands.sh file: self.request.sendall(self.data.upper())
		
		#open file using the path from sys.argv array
		with open(sys.argv[1], 'r') as f:
			#loop that converts each command in the file to a command and sends it to the client
			for command in f:
				command = command.strip()
				self.request.sendall(command.encode())
				message = message = self.request.recv(1024).decode()
				print(message)
						
if __name__ == "__main__":
	HOST, PORT = "", 8000
	tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)
	try:
		tcpServer.serve_forever()
	except:
		print("There was an error")
