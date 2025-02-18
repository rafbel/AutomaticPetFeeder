import time
from datetime import datetime
import os
from socket import *

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

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

host = ""
port = 5005
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Waiting to receive messages..."
while True:
    data  = UDPSock.recvfrom(buf)
    print "Received message: " + data
    #if data == "exit":
    #    break
    #Sleeps for one second to avoid Rpi crashes
    time.sleep(1)
    if data=="feed":
	pwm.set_pwm(0,0,servo_max)
	time.sleep(1)
	#pwm.set_pwm(0,0,servo_max)
	pwm.set_pwm(0,0,servo_min)
	time.sleep(1)
    
UDPSock.close()
os._exit(0)
