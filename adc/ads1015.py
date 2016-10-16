#!/usr/bin/python
# Import required libraries
import sys
import time
import Adafruit_ADS1x15
# RPi.GPIO is currently not being used, but will leave to make
# use later easy.
import RPi.GPIO as GPIO

# Use board pinout
GPIO.setmode(GPIO.BCM)

# Set globals
# Gain of 1 for measuing +/-4.096V.  Use this for 3.3V.
# See datasheet for more details.
GAIN = 1
# Smallest sampling rate.  Should be most energy efficient
# according to data sheet.
DATA_RATE = 128

try:
    # Main function

    # I'm using the ADS1015.
    adc = Adafruit_ADS1x15.ADS1015()

    print('Reading values, press Ctrl-C to quit...')
    while True:
        # Read the specified ADC channel using,
        # - Previously specified gain.
        # - value.
        # Change numbered 0 - 3.
        value = adc.read_adc(1, gain=GAIN, data_rate=DATA_RATE)
        # Print the ADC values.
        print('Value:  ', value)
        # Pause for half a second.
        time.sleep(0.5)


except KeyboardInterrupt:
    print("\nProcessing ctrl+c")

except:
    print("\nProcessing unhandled errors and exceptions")

finally:
    print("\nCleaning up")
    GPIO.cleanup()

