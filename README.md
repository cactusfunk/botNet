# botNet
All of the code from Chapter 4 of Ethical Hacking: A Hands on Introduction to Breaking In. Chapter 4 is titled: Crafting TCP Shells and Botnets  


In this chapter, we are taught about sockets and process communication. It explains how TCP handshakes work the type/way packets are exchanged between the client and the server. We then are taught about what a TCP reverse shell is. It is explained that since a lot of firewalls allow outgoing connections only, the solution as an attacker is to install a reverse shell on the victim machine that connects to the command and control server outside the network. Once this connection is made, you can send commands to the victim which are then executed.  It then gives us a diagram that shows how this works/is going to work as we work in the chapter. You can view it as 'diagram.png'.  

We then were taught how to use nmap to scan for open ports. We learned about some different scan types and flags for nmap, as well as the pros and cons of them. On the metasploitable server, we located an open tcp port 21 which has a vulnerable version of vsftpd (2.3.4) running. This is what we are going to exploit to gain access to the metasploitable machine so that we can load our reverse shell onto it. It is a backdoor that starts a shell running on port 6200 which we connect to and download reverseShell.py onto the victim machine.
