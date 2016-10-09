#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use board pinout
GPIO.setmode(GPIO.BCM)

# Set globals
MY_GLOBAL = 2048

try:
    # Main function

except KeyboardInterrupt:
    print("\nProcessing ctrl+c")

except:
    print("\nProcessing unhandled errors and exceptions")

finally:
    print("\nCleaning up")
    GPIO.cleanup()

