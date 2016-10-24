#!/usr/bin/env python
 
import socket
 

TCP_IP = 'proxy9.yoics.net'
TCP_PORT = 38352
BUFFER_SIZE = 1024
MESSAGE = "feed"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
s.close()