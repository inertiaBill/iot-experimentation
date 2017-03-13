#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use board pinout
GPIO.setmode(GPIO.BCM)

# Set globals
BUZZER_CONTROL = 23

GPIO.setup(BUZZER_CONTROL, GPIO.OUT) 

def beep_sequence():
    for i in range(0, 3):
        GPIO.output(BUZZER_CONTROL, True)
        time.sleep(.5)
        GPIO.output(BUZZER_CONTROL, False)
        time.sleep(.5)

try:
    # Main function
    for i in range(0, 4):
        beep_sequence()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProcessing ctrl+c")

except:
    print("\nProcessing unhandled errors and exceptions")

finally:
    print("\nCleaning up")
    GPIO.cleanup()

