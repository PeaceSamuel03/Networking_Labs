# Import socket module
from socket import *    


serverName = gethostname()
HOST= gethostbyname(serverName)
print("IP address of the machine:", HOST)
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
    print('Ready to serve...')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024).decode() #message syntax: GET /HTMLfile HTTP/1.1
        #Check that the HTTP request adheres to the correct syntax
        request_type = message.split()[0]
        http_type = message.split()[2]
        if request_type != "GET":
            connectionSocket.send("HTTP/1.1 400 Bad Request\r\n\r\n".encode())
            connectionSocket.close()
        if http_type != "HTTP/1.1":
            connectionSocket.send("HTTP/1.1 505 HTTP Version Not Supported\r\n\r\n".encode())
            connectionSocket.close()
       
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        # Because the extracted path of the HTTP request includes 
        # a character '\', we read the path from the second character 
        with open(filename[1:], 'r') as f:
            # Store the entire content of the requested file in a temporary buffer
            outputdata = f.read()
        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):  
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Close the client connection socket
        connectionSocket.close()

serverSocket.close()  

