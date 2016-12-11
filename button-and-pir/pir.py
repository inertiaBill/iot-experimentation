""" PirSensor class for encapsulating the interaction with proximity
sensor. """

class PirSensor(object):
    # Initialize class variables here

    def __init__(self):
        # Initialize instance variables here
        # Prefix with two underscores for private.
        __start_rise = 0
        __end_rise = 0

    def process_edge(self, gpio, level, tick):
        if level:
            print("PirSensor rising")
        else:
            print("PirSensor falling")

