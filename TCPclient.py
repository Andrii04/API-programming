from socket import *

serverName = "servername"
serverPort = 12000 # "welcoming socket"'s port, which is the server's socket at which all clients go knock to start a connection (a new socket specifically for that client)
clientSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM means it's a TCP socket
#note that the operating system decides the port number of the client Socket, so we don't have to specify it
clientSocket.connect(serverName, serverPort) #here three-way-handshake is performed (invisible to us) to estabòlish TCP connection to the server, this line initiaties the "knock on the welcoming door" of the server, the server responds by creating a new door for this specific client. (a new socket) and therefore a TCP connection between the client and server is established
sentence = input("Input lowercase sentence:")
clientSocket.send(sentence.encode()) #different from UDP where we use sendto, since here the specific TCP connection is already established and ongoing, so we just drop the bytes in it and it goes where it's supposed to go by itself, not needed to specify the destination address
modifiedSentence = clientSocket.recv(2048)
clientSocket.close()
