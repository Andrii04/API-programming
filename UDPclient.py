from socket import *

serverName = "hostname"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) #AF_INET means the underlying network is using IPv4, SOCK_DGRAM means the socket uses UDP as its transport protocol, this line indicates that the process's door has been created (the process's socket)
message = input("input lowercase sentence:") #message to send to server
clientSocket.sendto(message.encode(), (serverName, serverPort)) #.encode() transforms String -> byte since sockets only accept byte as data. this line also implicitly tells clientSocket to receive data from the server specified
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #buffer, size 2048 usually works for most tasks
print(modifiedMessage.decode()) #turns byte back into String and prints the modified message from the server
clientSocket.close() #closing the socket since communication should end here, process then terminates
