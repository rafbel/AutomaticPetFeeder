import httplib2
import json
import datetime
import base64
import sys
import os
import getpass
import errno

from urllib.request import urlopen
from json import dumps

from socket import error as socket_error
import socket
import sys
import time
from weavedConn import getConnDetails


proxy,port = getConnDetails("feederPi")


#Checks for thrown exceptions
if (proxy == "KeyError"):
    print ("Key Error exception!")
elif (proxy == "ServerNotFound"):
    print ("Server not found.  Possible connection problem!")
elif (proxy == "ServerError"):
    print ("Can't connect to Weaved server!")
elif (proxy == "OutputError"):
    print ("Output port is not enabled for this type of connection")
else:
      
    # 
      
	try:	
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((proxy, port))
		# Send data
		message = 'feed.'
		print >>sys.stderr, 'sending "%s"' % message
		sock.send(message.encode('utf-8'))

		# Look for the response
		amount_received = 0
		amount_expected = len(message)
		
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print >>sys.stderr, 'received "%s"' % data
			time.sleep(1)

	finally:
		print >>sys.stderr, 'closing socket'
		sock.close()
