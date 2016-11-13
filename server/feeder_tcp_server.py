import time
from datetime import datetime
import os
from socket import *
import pickle
from time_functionalities import addTime, removeTime, changeTime,readFromFile

#read from time table:
timeArray = readFromFile()

host = ''
port = 5005
address = (host,port)
buf = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(address)
sock.listen(1)
while True:
    print ("Waiting to receive messages...")
    conn,addr = sock.accept()
    print ('Connection address:',addr)
    timePassed = 0
    firstConn = True
    
    while (timePassed <= 600):
        if (firstConn):
            firstConn = False
            conn.send(pickle.dumps(timeArray))

        #----------
        (data,address)  = conn.recvfrom(buf)
        print ("Received message: " +  data)
        data = data.split()
        #Sleeps for one second to avoid Rpi crashes
        time.sleep(1)

        if data:
                
            if data[0]=="feed":
                #feedMotion()
                conn.send(("ok").encode("utf-8"))
		print ("Sent!")
            #if connection is terminated, closes socket connection and makes it available for a new one
            elif data == "exit":
                break
                
            elif data[0] == "add_time":
                timeArray = addTime(timeArray,int(data[1]))[:]
                conn.send(pickle.dumps(timeArray))

            elif data[0] == "remove_time":
                timeArray = removeTime(timeArray,int(data[1]))
                conn.send(pickle.dumps(timeArray))

            elif data[0] == "change_time":
                #data[1] = old time ; data[2] = new time
                timeArray = changeTime(timeArray,int(data[1]),int(data[2]))
                conn.send(pickle.dumps(timeArray))
        timePassed+= 1
    
sock.close()
os._exit(0)
