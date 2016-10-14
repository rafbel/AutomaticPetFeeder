# Save as client.py 
# Message Sender
import os
from socket import *
host = "proxy14.yoics.net" # set to IP address of target computer
port = 38176
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("Enter message to send or type 'exit': ")
    UDPSock.sendto(data.encode(), addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)