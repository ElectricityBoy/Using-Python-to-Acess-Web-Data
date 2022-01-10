#A socket is one endpoint of a two-way communication link between two programs running on the network. 
# A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.
import socket
#Importing the socket library

mysock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
#By default, the port number for a web server is 80. That port is the port that the server "listens to" or expects to receive from a Web client

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()