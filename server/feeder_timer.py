import datetime
import time
from time_functionalities import readFromFile
from feeder_controller import FeederController
#from feeder_tcp_server import feedMotion

#import Adafruit_PCA9685

#This script is responsible for feeding at the correct times

def getCurrentTime():
    dateNow = datetime.datetime.now()
    currentTime = str(dateNow.hour) + str(dateNow.minute)
    currentTime = int(currentTime)

    return currentTime

def checkTime(timeArray):
    currentTime = getCurrentTime()
    #deal with exceptions!

    for timeIndex,timeItem in enumerate(timeArray):
        if (currentTime == timeItem):
            return True
        
    #returns False if it is not the time to feed
    return False
      
feedCon = FeederController()
while True:
    timeArray = readFromFile()
    if (checkTime(timeArray)):
       feedCon.feedMotion()

    time.sleep(60)
        
    
    
    


