from datetime import datetime
from socket import *
import uuid
import time
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
ip_address = input('Enter an IP address of the destination server:')  # take as input the website IP you want to access
request = "GET / HTTP/1.1\r\nHost:" + ip_address + "\r\n\r\n"
clientSocket.sendall(request.encode())  # send the request to the proxy server
a = time.time()
print("on",datetime.now(),"Message sent is:", request)  # print a message with the request details and the exact time sent
response = clientSocket.recv(4096)  # receive the reply back from the proxy server and display it to the user with
# the exact
# time received
b = time.time()
print("on",datetime.now(),"The Response from server is :", response.decode())
print("Round trip time:",b-a)#calculation  of round trip time
print("Mac address is:", hex(uuid.getnode()))#Mac Address Displayed
