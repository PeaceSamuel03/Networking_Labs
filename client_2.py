# from the socket module import all
from socket import *
#import socket, time
from pathlib import Path

# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
serverName = gethostname()
HOST= input("Enter IP address:")#socket.gethostbyname(serverName)#accept ip address on command line
serverPort = input("Enter port  number:")
clientSocket = socket(AF_INET, SOCK_STREAM)
'''<INSERT CALL TO CREATE THE SOCKET>'''

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
server_address = (HOST, serverPort)  
'''<INSERT PARAMETERS>'''
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
clientSocket.connect((serverName, serverPort))
'''<INSERT CALL TO CONNECT TO SERVER>'''
while True:
    try:
        
        # Send HTTP request
        message = input("enter message:")

        #'This is the message from the client to the server.'
        print('sending "%s"' % message)
        # Data is transmitted to the server with sendall()
        # encode() function returns bytes object
        #sock -> clientSocket
        clientSocket.sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            # Data is read from the connection with recv()
            # decode() function returns string object
            #sock -> clientSocket
            data = clientSocket.recv(16).decode()
            amount_received += len(data)
        print('received "%s"' % data)

    finally:
        print('closing socket')
        '''<INSERT CALL TO CLOSE SOCKET>'''
        #sock -> clientSocket
        #clientSocket.close()
clientSocket.close()