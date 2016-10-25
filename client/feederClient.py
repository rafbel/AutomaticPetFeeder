from socket import error as socket_error
import socket

from connLib import getConnDetails

userName = input("User name:") 
password = input("Password:")
            
proxy,port = getConnDetails("feederPi",userName,password)

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
      
    # Send message via TCP connection
    message = "feed"
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((proxy, port))
    sock.send(message.encode('utf-8'))
    
    sock.close()
    
