""" PirSensor class for encapsulating the interaction with proximity
sensor.
"""

import time

REPORT_FREQUENCY = 10 * 60      # FREQ = minutes * 60 sec / minute

class PirSensor(object):
    # Initialize class variables here

    def __init__(self, gpio_obj, led_pin):
        # Initialize instance variables here
        # Prefix with two underscores for private.
        self.__start_rise = 0.0
        self.__number_of_rises = 0
        self.__seconds_at_high = 0.0
        self.__next_report = 0.0
        self.__led_pin = led_pin
        self.__gpio = gpio_obj

    def process_edge(self, gpio, level, tick):
        time_last_sense = 0.0
        current_time = time.time()
        time_since_rise = 0.0

        if level:
            if self.__next_report == 0.0:
                self.__next_report = current_time + REPORT_FREQUENCY
                print('Setting initial report time - %20.2f' %
                        (self.__next_report))
            self.__gpio.write(self.__led_pin, 1)
            print('PirSensor rising')
            self.__start_rise = time.time()
            self.__number_of_rises += 1
            self.__start_rise = current_time
        else:
            self.__gpio.write(self.__led_pin, 0)
            print('PirSensor falling')
            if self.__start_rise > 0.0:
                time_since_rise = current_time - self.__start_rise
                self.__seconds_at_high = self.__seconds_at_high \
                        + time_since_rise
                print('Time at high is %6.2f' % time_since_rise)

        print('Next report at %s' % (time.asctime(
            time.localtime(self.__next_report))))
        print('Current time   %s' % (time.asctime(
            time.localtime(current_time))))
        if current_time > self.__next_report:
            # Print summary and set time of next report
            print('***** Summary *****')
            print('%2u detections for total of %6.2f secconds.'
                    % (self.__number_of_rises,
                        self.__seconds_at_high))
            self.__number_of_rises = 0
            self.__seconds_at_high = 0.0
            self.__next_report = current_time + REPORT_FREQUENCY



