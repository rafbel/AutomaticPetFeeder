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


def loginWeaved(userName,password):
        apiMethod="https://"
        apiVersion="/v22"
        apiServer="api.weaved.com"
        apiKey="WeavedDemoKey$2015"

        #===============================================
        #Login



        httplib2.debuglevel     = 0
        http                    = httplib2.Http()
        content_type_header     = "application/json"
        #userName = input("User name:") 
        #password = input("Password:")
            
        loginURL = apiMethod + apiServer + apiVersion + "/api/user/login"

        loginHeaders = {
                    'Content-Type': content_type_header,
                    'apikey': apiKey
                }
        try:        
            response, content = http.request( loginURL + "/" + userName + "/" + password,
                                              'GET',
                                              headers=loginHeaders)
        except:
            #print ("Server not found.  Possible connection problem!")
            return ("ServerNotFound"),("ServerNotFound")                                          
        #print ("============================================================")
        #print (content)

        try: 
            data = json.loads(content.decode('utf-8'))
            if(data["status"] != "true"):
                #print ("Can't connect to Weaved server!")
                #print (data["reason"])
                return "ServerError","ServerError"

            token = data["token"]
        except KeyError:
            print ("Connection failed!")
            return ("KeyError"),("KeyError")
            
        print ("Token = " +  token)
        return token
def findDevice(deviceName,token):
        apiMethod="https://"
        apiVersion="/v22"
        apiServer="api.weaved.com"
        apiKey="WeavedDemoKey$2015"
        httplib2.debuglevel     = 0
        http                    = httplib2.Http()
        content_type_header     = "application/json"
        #===============================================
        # Procura por dispositivo/serviço TCP de alimentação
            
        deviceListURL = apiMethod + apiServer + apiVersion + "/api/device/list/all"


        deviceListHeaders = {
                    'Content-Type': content_type_header,
                    'apikey': apiKey,
                    # token do login
                    'token': token,
                }


        response, content = http.request( deviceListURL,
                                            'GET',
                                            headers=deviceListHeaders)
        #print ("============================================================")                                 
        #print (content)
        data = json.loads(content.decode('utf-8'))
        for counter in range(len(data["devices"])):
            if (data["devices"][counter]["devicealias"] == deviceName):
                deviceUID = data["devices"][counter]["deviceaddress"]
                print ("Device UID " + deviceUID)
                return deviceUID

        return "Nothing"

        
        
        #Checar a não existencia do serviço no futuro
        
#===============================================
#Conecta ao dispositivo
def getAccess(token,deviceUID):
        apiMethod="https://"
        apiVersion="/v22"
        apiServer="api.weaved.com"
        apiKey="WeavedDemoKey$2015"
        httplib2.debuglevel     = 0
        http                    = httplib2.Http()
        content_type_header     = "application/json"
        
        #Pega o IP publico do sender (em bytes, depois sera decodificado para uma string)
        my_ip = urlopen('http://ip.42.pl/raw').read().decode('utf-8')
        proxyConnectURL = apiMethod + apiServer + apiVersion + "/api/device/connect"

        proxyHeaders = {
                    'Content-Type': content_type_header,
                    'apikey': apiKey,
                    'token': token
                }

        proxyBody = {
                    'deviceaddress': deviceUID,
                    'hostip': my_ip,
                    'wait': "true"
                }
        response, content = http.request( proxyConnectURL,
                                              'POST',
                                              headers=proxyHeaders,
                                              body=dumps(proxyBody),
                                           )
        try:
            data = json.loads(content.decode('utf-8'))["connection"]["proxy"]
            proxy_limits = 5 + data[5:].index(':')
            proxy = data[:proxy_limits]
            proxy = proxy[7:]
            print ("Proxy: " + proxy)
            port_limits = data[5:].index(':') + 6 - len(data)
            port = int(data[port_limits:])
            print("Port: " + str(port))
            return proxy,port
        except KeyError:
            #print ("Key Error exception!")
            #print (content)
            return ("KeyError"),("KeyError")

        return 0,0
		
    

            
