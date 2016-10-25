from connLib import getConnDetails


userName = input("User name:") 
password = input("Password:")
            
proxy,port = getConnDetails("feederPi",userName,password)
print (proxy + "\n" + port)
