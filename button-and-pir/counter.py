#!/usr/bin/python

"""
counter.py - Monitor activity in a space. Support pushbutton sign in
and PIR sensor.
"""

# Import required libraries
import sys
import time
import pigpio
from threading import Thread

import pir

# Uses pigpio. Ensure the daemon is running before running program.
# It can be started with,
#   sudo pigpiod 

# Use board pinout
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
#GPIO.setup(16, GPIO.IN) 

pi = pigpio.pi()

# Set globals
BUTTON_PIN = 16
BUTTON_LED_PIN = 26
PIR_LED_PIN = 18
PIR_PIN = 23
SKIP_UNTIL = 0
SKIP_DURATION = 1.0

PIR_INSTANCE = pir.PirSensor(pi, PIR_LED_PIN)

# Set GPIO modes
# NYI - Try software pull up resistor
pi.set_mode(BUTTON_PIN, pigpio.INPUT)
pi.set_mode(PIR_PIN, pigpio.INPUT)
pi.set_mode(PIR_LED_PIN, pigpio.OUTPUT)
pi.set_mode(BUTTON_LED_PIN, pigpio.OUTPUT)

def flash_button_led():
    pi.write(BUTTON_LED_PIN, 1)
    time.sleep(1)
    pi.write(BUTTON_LED_PIN, 0)

def process_button(gpio, level, tick):
    global SKIP_UNTIL
    tick_diff = 0
    current_time = time.time()
    #print("GPIO: %s, level: %s, tick: %s" % (gpio, level, tick))
    if(level == 1):
        # if rise happens after skip time, log a press and reset
        # the skip time.
        if(current_time > SKIP_UNTIL):
            #t = Thread(target=flash_button_led, args=(i,))
            t = Thread(target=flash_button_led)
            t.start()
            print('')
            print('*** New Press 0 *** GPIO: %s, level: %s, tick: %s' % 
                    (gpio, level, tick))
            SKIP_UNTIL = current_time + SKIP_DURATION
        else:
            # Output caret for rising edge that is skipped
            # NYI - if this is working fine, could probably
            # update callback to do only rising edge.
            print('^', end='')
    else:
        BUTTON_FALL_TICK = tick
        # Ignore all falling edge. Output 'V' to indicate this
        print('V', end='')

#pi.callback(BUTTON_PIN, pigpio.RISING_EDGE, process_button)
pi.callback(BUTTON_PIN, pigpio.EITHER_EDGE, process_button)
pi.callback(PIR_PIN, pigpio.EITHER_EDGE, PIR_INSTANCE.process_edge)

try:
    # Main function
    pi.write(PIR_LED_PIN, 0)
    pi.write(BUTTON_LED_PIN, 0)

    while True:
        pass

except KeyboardInterrupt:
    print("\nProcessing ctrl+c")

except Exception:
    print("\nProcessing unhandled errors and exceptions")

finally:
    print("\nCleaning up")
    pi.write(PIR_LED_PIN, 0)
    pi.write(BUTTON_LED_PIN, 0)
    pi.stop()

# This pi.stop is needed to clean-up pigpio before try.
pi.stop()
