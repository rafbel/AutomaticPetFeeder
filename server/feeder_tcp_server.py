import time
from datetime import datetime
import os
from socket import *
import pickle
from time_functionalities import addTime, removeTime, changeTime,readFromFile

# Importa o module PCA9685 do driver do controlador da Adafruit.
import Adafruit_PCA9685

# Inicializa o PCA9685 com o endereco padrao (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Configura o pulso minimo e o maximo
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_med = 500
# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

#Funcao que determina se o horario atual = horario de alimentacao
def checkFeedTime(feeding_time):
	time_now = datetime.now()
	if (datetime.now().minute == feeding_time.minute):
		return True
	return False

def feedMotion():
    pwm.set_pwm(0,0,servo_max)
    time.sleep(1)
    pwm.set_pwm(0,0,servo_min)
    time.sleep(1)

    
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

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
                
            if data=="feed":
                #feedMotion()
                conn.send((True).encode('utf-8'))
            #if connection is terminated, closes socket connection and makes it available for a new one
            elif data == "exit":
                break
                
            elif data[0] == "add_time":
                timeArray = addTime(timeArray,int(data[1]))
                conn.send(pickle.dumps(timeArray))

            elif data[0] == "remove_time":
                timeArray = removeTime(timeArray,int(data[1]))
                conn.send(pickle.dumps(timeArray))

            elif data[0] == "change_time":
                #data[1] = old time ; data[2] = new time
                timeArray = changeTime(timeArray,int(data[1]),int(data[2]))
                conn.send(pickle.dumps(timeArray))
        timePassed++
    
sock.close()
os._exit(0)
