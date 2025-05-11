from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort)) #serverSocket is welcoming socket
serverSocket.listen(1) #waiting for clients to knock at welcoming door (serverSocket), parameter specifies the maximum number of queued connections
print("The server is ready to receive!")
while True:
    connectionSocket, addr = serverSocket.accept() #accepts client knocking on welcoming door, and creates a new socket for that specific client: connectionSocket, and now a TCP connection is established between connectionSocket and clientSocket.
    sentence = connectionSocket.recv(1024).decode()
    sentence += "\nSentence modified!"
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close() #we close the specific connection after we're done with the client, but the server still continues to accept other clients
    

