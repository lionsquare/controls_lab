#!/usr/bin/python3

import time
import wiringpi

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.1


