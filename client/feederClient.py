from socket import error as socket_error
import socket
import pickle
import time

from connLib import *

userName = input("User name:") 
password = input("Password:")

token = loginWeaved(userName,password)
UID = findDevice("feederPi",token)
proxy,port = getAccess(token,UID)

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

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((proxy, port))
    buf = 1024
    TIMEOUT = 100
    first_conn = True
    
    while (True):
        timeoutCheck = 0

        if (first_conn == True):
            first_conn = False
            timeArray = pickle.loads(sock.recv(buf))
            while (not timeArray):
                if (timeoutCheck >= 600):
                        print("Connection timeout. Please try again later")
                        break
                time.sleep(1)
                timeoutCheck += 1
                timeArray = pickle.loads(sock.recv(buf))
            if (timeoutCheck >= 600):
                        break
               
            print(repr(timeArray))
        print("Menu: \n1- Feed Now \n2- Add Feeding Time \n3- Remove Feeding Time \n4- Change Feeding Time \n5 - Exit\n")
        # Send message via TCP connection
        choice = input("Your choice: ")
        if (choice == "1"):
            message = "feed"
            sock.send(message.encode('utf-8'))
            timeoutCheck = 0
            data = sock.recv(buf).decode('utf-8')
            while not data:
                if (timeoutCheck >= TIMEOUT):
                    print("Connection timeout. Please try again later")
                    break
                time.sleep(1)
                timeoutCheck += 1
                data = sock.recv(buf).decode('utf-8')
                print ("Waiting")
            print (data)
            
            
        elif (int(choice) >=2 and int(choice)<= 4):  
            if (choice == "2"):
                message = "add_time"
            elif (choice == "3"):
                message = "remove_time"
            elif (choice == "4"):
                message = "change_time"
            
            sock.send(message.encode('utf-8'))
            timeArray = pickle.loads(sock.recv(buf))
            while (not timeArray):
                 if (timeoutCheck >= TIMEOUT):
                    print("Connection timeout. Please try again later")
                    break
                 timeoutCheck += 1
                 time.sleep(1)
                 timeArray = pickle.loads(sock.recv(buf))
                 print(repr(timeArray))
               
        elif (choice == "5"):
            message = "exit"
            sock.send(message.encode('utf-8'))
            break
        else:
            print("Not a valid option, please try again")
        time.sleep(1)
    
    sock.close()
    
