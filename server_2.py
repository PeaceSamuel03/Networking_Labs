# from the socket module import all
from socket import *
import socket, time
from pathlib import Path

'''<INSERT CODE TO IMPORT SOCKET MODULE>'''

# Create a TCP server socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP
serverName = socket.gethostname()
HOST= socket.gethostbyname(serverName)
serverPort = int(input("Enter the port number:"))#enter in command line port number 
serverSocket = socket.socket(AF_INET, SOCK_STREAM)
'''<INSERT CALL TO CREATE THE SOCKET>'''

# set values for host 'localhost' - meaning this machine and port number 10000
server_address = (HOST, serverPort)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# print out the IP address of the machine the server is running on
print("IP address of the machine:", HOST)
# Bind the socket to the host and port
serverSocket.bind((HOST,serverPort))
'''<INSERT CODE TO BIND SERVER ADDRESS TO SOCKET>'''

# Listen for one incoming connections to the server
serverSocket.listen(1)
'''<INSERT CODE TO TELL SERVER TO LISTEN FOR ONE INCOMING CONNECTION>'''

# we want the server to run all the time, so set up a forever true while loop
while True:

    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = serverSocket.accept()
    '''<INSERT CODE TO ACCEPT THE CONNECTION REQUEST FROM THE CLIENT>'''
    
    try:
        print('connection from', client_address)

         # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            if data:
                print('received "%s"' % data)
                print('sending data back to the client')
                # encode() function returns bytes object
                connection.sendall(data.encode())
                
                message = input("Enter message:")
                connection.sendall(message.encode())
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()
        '''<INSERT CODE TO CLOSE THE CONNECTION>'''

# now close the socket
serverSocket.close()
'''<INSERT CODE TO CLOSE THE SOCKET>'''
