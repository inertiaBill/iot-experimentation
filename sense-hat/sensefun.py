""" Sense hat screen clearing game.
"""

import time
from sense_hat import SenseHat

class GyroClear(object):
    #Initialize class variables here
    b = (0, 0, 255) # blue
    c = (0, 0, 0) # clear
    e = (0, 255, 0) # eraser colour (green)

    def __init__(self):
        super(GyroClear, self).__init__()
        self.__sense = SenseHat()
        self.__eraser_row = 0
        self.__eraser_col = 0
        self.__a = [
                GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c,
                GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b,
                GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b,
                ]
        self.__s = [
                GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c,
                GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.c, GyroClear.c,
                ]
        self.__p = [
                GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.b, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.b, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c,
                GyroClear.c, GyroClear.b, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c, GyroClear.c,
                ]

    def show_letter(self, letter):
        self.__sense.show_letter(letter)
        time.sleep(2)

    def clear_display(self):
        self.__sense.clear()

    def display_letters(self):
        time.sleep(1)
        self.__sense.set_pixels(self.__a)
        time.sleep(2)
        self.__sense.set_pixels(self.__s)
        time.sleep(2)
        self.__sense.set_pixels(self.__p)
        time.sleep(2)

    def display_current_readings(self):
        temp = self.__sense.get_temperature()
        self.__sense.show_message("Th: ")
        self.__sense.show_message(str(int(temp)))
        temp = self.__sense.get_temperature_from_pressure()
        self.__sense.show_message("Tp: ")
        self.__sense.show_message(str(int(temp)))
        pressure = self.__sense.get_pressure()
        self.__sense.show_message("P: ")
        self.__sense.show_message(str(int(pressure)))
        humidity = self.__sense.get_humidity()
        self.__sense.show_message("H: ")
        self.__sense.show_message(str(int(humidity)))

    def getArrayIndex(self, x, y):
        # NYI confirm this equation
        index = y * 8 + x - 1

    def reposition_eraser(self):
        old_x = self.__eraser_row 
        old_y = self.__eraser_col
        pitch = self.__sense.get_orientation()['pitch']
        roll = self.__sense.get_orientation()['roll']

        if 1 < pitch < 179 and self.__eraser_row != 0:
            self.__eraser_row -= 1
        elif 359 > pitch > 179 and x != 7 :
            self.__eraser_row += 1
        if 1 < roll < 179 and y != 7:
            self.__eraser_col += 1
        elif 359 > roll > 179 and y != 0 :
            self.__eraser_col -= 1

        old_index = self.getArrayIndex(old_x, old_y)
        new_index = self.getArrayIndex(self.__eraser_row,
                self.__eraser_col)

    def play_game(self, max_moves):
        count = 0
        while count < 10:
            self.repostion_eraser()
            sleep(0.25)
            count += 1

if __name__ == "__main__":
    game = GyroClear()
    #game.display_current_readings()
    #game.display_letters()
    #game.show_letter('a')
    #game.show_letter('s')
    #game.show_letter('p')
    #game.clear_display()
    game.move_eraser(10)
