import httplib2
import json
import datetime
import base64
import sys
import os
import getpass
import errno

from urllib2 import urlopen
from json import dumps

from socket import error as socket_error
import socket

apiMethod="https://"
apiVersion="/v22"
apiServer="api.weaved.com"
apiKey="WeavedDemoKey$2015"

#===============================================
if __name__ == '__main__':

    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"

    userName = raw_input("User name:") 
    password = raw_input("Password:")
        
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
        print "Server not found.  Possible connection problem!"
        exit()                                          
#    print (response)
    print "============================================================"
    print (content)
    print

    try: 
        data = json.loads(content)
        if(data["status"] != "true"):
            print "Can't connect to Weaved server!"
            print data["reason"]
            exit()

        token = data["token"]
    except KeyError:
        print "Comnnection failed!"
        exit()
        
    print "Token = " +  token
