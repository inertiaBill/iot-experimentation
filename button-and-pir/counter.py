#!/usr/bin/python

"""
counter.py - Monitor activity in a space. Support pushbutton sign in
and PIR sensor.
"""

# Import required libraries
import sys
import time
import pigpio

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
LED_PIN = 18
PIR_PIN = 23
SKIP_UNTIL = 0
SKIP_DURATION = 1.0

# Set GPIO modes
# NYI - Try software pull up resistor
pi.set_mode(BUTTON_PIN, pigpio.INPUT)
pi.set_mode(PIR_PIN, pigpio.INPUT)
pi.set_mode(LED_PIN, pigpio.OUTPUT)

def process_button(gpio, level, tick):
    global SKIP_UNTIL
    tick_diff = 0
    current_time = time.time()
    #print("GPIO: %s, level: %s, tick: %s" % (gpio, level, tick))
    if(level == 1):
        # if rise happens after skip time, log a press and reset
        # the skip time.
        if(current_time > SKIP_UNTIL):
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

def process_pir_detect(gpio, level, tick):
    print('')
    print("pir_detect - GPIO: %s, level: %s, tick: %s" % (gpio, level, tick))
    if(gpio == PIR_PIN):
        print("PIR rising")
        pi.write(LED_PIN, 1)
        
def process_pir_no_detect(gpio, level, tick):
    print('')
    print("pir_no_detect - GPIO: %s, level: %s, tick: %s" % (gpio, level, tick))
    if(gpio == PIR_PIN):
        print("PIR falling")
        pi.write(LED_PIN, 0)
        
#pi.callback(BUTTON_PIN, pigpio.RISING_EDGE, process_button)
pi.callback(BUTTON_PIN, pigpio.EITHER_EDGE, process_button)
pi.callback(PIR_PIN, pigpio.RISING_EDGE, process_pir_detect)
pi.callback(PIR_PIN, pigpio.FALLING_EDGE, process_pir_no_detect)

try:
    # Main function
    pi.write(LED_PIN, 0)

    while True:
        pass

except KeyboardInterrupt:
    print("\nProcessing ctrl+c")

except:
    print("\nProcessing unhandled errors and exceptions")

finally:
    print("\nCleaning up")
    pi.stop()

pi.stop()
