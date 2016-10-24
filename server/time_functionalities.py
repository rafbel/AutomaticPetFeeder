#Notes:
#Times are defined in the HHMM format, where HH = hours and MM = minutes
#Main functionalities for this module: addTime, removeTime, changeTime
#Supporting functionalities for this module: readFromFile, writeToFile

#Supporting functionalities:
def readFromFile():
    #Abre o arquivo para leitura (recebe todos os horarios de alimentação)
    readFile = open("feed_times.txt",'r')
    
    with readFile as it:
        timeArray = []
        for line in it:
            timeArray.append(int(line))
            
    readFile.close()
    return timeArray

def writeToFile(timeArray):
    #Writes the time array to the file
    writeFile = open("feed_times.txt",'w')

    for timeItem in timeArray:
        writeFile.write("%s\n" % (str(timeItem) + "\n"))
        
    writeFile.close()


#Main functionalities:
def addTime(timeArray,newTime):
    #adds newTime in timeArray. organizes it to be in numeric crescent order
    if not timeArray:
        timeArray.append(newTime)
    else:
        foundInsert = False
        for index,currentTime in enumerate(timeArray):
            if (currentTime > newTime):
                timeArray.insert(index,newTime)
                foundInsert = True
                break
        if not foundInsert:
            timeArray.append(newTime)
            
    writeToFile(timeArray)

    return timeArray

def removeTime(timeArray,rmTime):
    readFromFile
    try:
        timeArray.remove(rmTime)
        writeToFile(timeArray)

    except Exception as excp:
        print ("No element %s found \n" % rmTime)

    return timeArray

def changeTime(timeArray,oldTime,newTime):
    try:
        arrayIndex = timeArray.index(oldTime)
        timeArray[arrayIndex] = newTime
        writeToFile(timeArray)
        
    except Exception as excp:
        print ("No element %s found \n" % oldTime)

    return timeArray
            
            
            
    
     
    
    
