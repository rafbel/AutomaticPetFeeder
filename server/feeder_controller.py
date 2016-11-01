# coding = utf-8

import time
# Importa o module PCA9685 do driver do controlador da Adafruit.
import Adafruit_PCA9685

class FeederController:

    # Inicializa o PCA9685 com o endereco padrao (0x40) da Rpi
    pwm = Adafruit_PCA9685.PCA9685()
    
    # Configura o pulso minimo e o maximo
    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096
    servo_med = 500

    def set_servo_pulse(channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        pwm.set_pwm(channel, 0, pulse)

    def _init:
        # Set frequency to 60hz, good for servos.
        pwm.set_pwm_freq(60)

    #Melhor configurações necessárias
    def feedMotion():
        pwm.set_pwm(0,0,servo_max)
        time.sleep(1)
        pwm.set_pwm(0,0,servo_min)
        time.sleep(1)
