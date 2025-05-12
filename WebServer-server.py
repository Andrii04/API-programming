from socket import *
serverPort = 8080;
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind('', serverPort)
serverSocket.listen(1)
while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(1024).decode()
    print("http request: " + request)
    requestEls = request.split()

    if requestEls[0] != "GET":
        print("not a GET request")
        break

    requestedFile = requestEls[1]

    try:
        f = open(requestedFile, 'r')
    except FileNotFoundError:
        connectionSocket.send((requestEls[2] + " 404 Not Found\n\n").encode())

    connectionSocket.send((requestEls[2] + " 200 OK\n\n" + f).encode())
    f.close()
    connectionSocket.close()
