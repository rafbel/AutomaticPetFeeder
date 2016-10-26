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

from socket import *
import sys
import time
from connLib import *
userName = input("User name:") 
password = input("Password:")
buf = 1024
            
token = loginWeaved(userName,password)
print(token)
UID = findDevice("feederPi",token)
print(UID)
proxy,port = getAccess(token,UID)
print(proxy)
print(port)


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
		print ('sending "%s"' % message)
		sock.send(message.encode('utf-8'))

		# Look for the response
		amount_received = 0
		amount_expected = len(message)
		
		while amount_received < amount_expected:
			data = sock.recv(buf)
			amount_received += len(data)
			print (data.decode('utf-8'))
			time.sleep(1)

	finally:
		print( 'closing socket')
		sock.close()
