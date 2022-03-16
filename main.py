# import socket module
from socket import *
import sys  # In order to terminate the program
"""
Author: ILYAS NAYLE 
CLASS: CMPE 472_02 - Computer Networks 
Programming Assignment I: Web Server
"""

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverPort = 6789
# serverSocket.bind(('10.10.203.147',serverPort))
#serverSocket.listen(1)


'''***Prepare a server socket***'''

# Fill in start
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f"The web server is up on the port {serverSocket}")
# Fill in end

while True:
    # Establish the connection
    print("Ready to serve...")
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    # Fill in end

    try:
        # Fill in start
        message = connectionSocket.recv(1024)
        print ("message: \n", message)
        filename = message.split()[1]
       # print(filename, "||", filename[1:])
        # Fill in end
        f = open(filename[1:])
        outputData = f.read()
        print("outputDdata:", outputData)
        # print(outputData)
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(b'\nHTTP/1.1 200 OK\n\n')
       # connectionSocket.send(outputData)
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()


    except IOError:
        # Send response message for file not found
        # Fill in start

        connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n".encode())
        connectionSocket.send("\r\n\r\n <html><head></head><body><h1>404 Not Found<h1></body></html>\r\n".encode())
        # Fill in end

        # Close client socket
        # Fill in start
        #connectionSocket.close()
    # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data