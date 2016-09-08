import time
from datetime import datetime

# Importa o module PCA9685 do driver do controlador da Adafruit.
import Adafruit_PCA9685

# Inicializa o PCA9685 com o endereco padrao (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Configura o pulso minimo e o maximo
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

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

#Move o motor indefinitivamente
print ('Press Ctrl-C to quit...')
while True:
    #time_start = datetime.now()
    # Move servo on channel O between extremes.
    # Horario	
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    # Anti-horario
    #if (time_start.minute == 55)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)
