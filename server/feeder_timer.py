import datetime
import time
from time_functionalities import readFromFile
#from feeder_tcp_server import feedMotion

#import Adafruit_PCA9685

#This script is responsible for feeding at the correct times

def getCurrentTime():
    dateNow = datetime.datetime.now()
    currentTime = str(dateNow.hour) + str(dateNow.minute)
    currentTime = int(currentTime)

    return currentTime

def checkTime(feeding_time):
    currentTime = getCurrentTime()
    
    if (currentTime == feeding_time):
        return True

    return False

def getNewIndex(timeArray):
    currentTime = getCurrentTime()
    #deal with exceptions!

    for timeIndex,timeItem in enumerate(timeArray):
        if (currentTime <= timeItem):
            return timeIndex
        
    #returns index = 0 if all the indexes have been run through the day
    return 0
      
while True:
    timeArray = readFromFile()
    timeIndex = getNewIndex(timeArray)
    print(timeArray[timeIndex])
    
    if (checkTime(timeArray[timeIndex])):
        print ("TIME TO FEED ",timeArray[timeIndex])
        #feedMotion()

    time.sleep(60)
        
    
    
    


