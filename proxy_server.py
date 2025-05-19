from socket import *
from datetime import datetime

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(1024).decode()  # parse the request to get the destination server IP address
    # Split the string at the colon after "Host"
    ip_address_string = request.split("Host:")[1]
    # Extract the IP address by splitting the string at the newline character
    ip_address = ip_address_string.split("\r\n")[0]
    print("IP address in request:", ip_address, "exact time on:",datetime.now())
    print("Message received is:" + ip_address + "Received on",datetime.now())  # message indicating that IP is received with the time
    try:
        dest_ip = ip_address
        destination_socket = socket(AF_INET, SOCK_STREAM)
        destination_socket.connect((dest_ip, 80))#connecting to the IP address that was chosen by the client
        destination_socket.send(request.encode())
        print("request sent on",datetime.now())#print a message with exact time of the actual request
        response = destination_socket.recv(4096)  # receiving the response from destination
        destination_socket.close()
        connectionSocket.send(response)  # send the response back to the client
        print("response is sent back to the client on",datetime.now())#print a message that the response was sent with the exact time

    except:
        print("error")  # If there was any error from the client side or from the server side, the proxy server
        # should display a message and return an error message to the client
        connectionSocket.send("something went wrong.please try again".encode())
    connectionSocket.close()

# References:
# https://www.geeksforgeeks.org/python-time-module/
# Everything on Moodle
# https://www.internalpointers.com/post/making-http-requests-sockets-python
# https://reqbin.com/Article/HttpGet#:~:text=The%20HTTP%20GET%20request%20method%20is%20used%20to%20request%20a,PUT%2C%20PATCH%20or%20DELETE%20methods.
# https://www.geeksforgeeks.org/extracting-mac-address-using-python/
# https://www.programiz.com/python-programming/datetime/current-datetime
