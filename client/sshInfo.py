from socket import error as socket_error
import socket
import pickle

from connLib import *

userName = input("User name:") 
password = input("Password:")

token = loginWeaved(userName,password)
UID = findDevice("sshPi",token)
proxy,port = getAccess(token,UID)

print (str(proxy) + "\n" + str(port))
