from Adafruit_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO


pwm = PWM(0x40)
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)


pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
GPIO.setmode(GPIO.BCM)



while(True):
	print 'hi'
	pwm.setPWM(0,0,100)
	time.sleep(10)
	pwm.setPWM(0,0,370)
	pwm.setPwm(0,0,370)
	time.sleep(10)
	pwm.setPWM(0,0,400)
        time.sleep(10)
