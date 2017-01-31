import time
from sense_hat import SenseHat

sense = SenseHat()

temp = sense.get_temperature()
sense.show_message("T:")
time.sleep(1)
sense.show_message(str(int(temp)))
time.sleep(1)
pressure = sense.get_pressure()
sense.show_message("P:")
time.sleep(1)
sense.show_message(str(int(pressure)))
time.sleep(1)
humidity = sense.get_humidity()
sense.show_message("H:")
time.sleep(1)
sense.show_message(str(int(humidity)))
time.sleep(1)
