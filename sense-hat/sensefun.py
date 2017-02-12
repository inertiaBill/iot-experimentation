""" Sense hat screen clearing game.
"""

import time
from sense_hat import SenseHat

class GyroClear(object):
    #Initialize class variables here
    b = (255, 255, 0) # background - gold
    f = (0, 0, 255) # foreground - blue
    c = (0, 0, 0) # clear
    e = (0, 255, 0) # eraser colour (green)
    a = [
            b, b, b, f, f, b, b, b,
            b, b, b, f, f, b, b, b,
            b, b, f, b, b, f, b, b,
            b, b, f, b, b, f, b, b,
            b, f, f, f, f, f, f, b,
            b, f, b, b, b, b, f, b,
            f, b, b, b, b, b, b, f,
            f, b, b, b, b, b, b, f,
            ]
    s = [
            b, b, f, f, f, f, b, b,
            b, f, b, b, b, b, f, b,
            b, f, b, b, b, b, b, b,
            b, b, f, f, f, b, b, b,
            b, b, b, f, f, f, b, b,
            b, b, b, b, b, b, f, b,
            b, f, b, b, b, b, f, b,
            b, b, f, f, f, f, b, b,
            ]
    p = [
            b, f, f, f, f, f, b, b,
            b, f, b, b, b, b, f, b,
            b, f, b, b, b, b, f, b,
            b, f, b, b, b, b, f, b,
            b, f, f, f, f, f, b, b,
            b, f, b, b, b, b, b, b,
            b, f, b, b, b, b, b, b,
            b, f, b, b, b, b, b, b,
            ]

    def __init__(self):
        super(GyroClear, self).__init__()
        self.__sense = SenseHat()
        self.__eraser_row = 0
        self.__eraser_col = 0
        self.__letters = [GyroClear.a, GyroClear.s, GyroClear.p]


    def show_letter(self, letter):
        self.__sense.show_letter(letter)
        time.sleep(2)

    def clear_display(self):
        self.__sense.clear()

    def display_letters(self):
        for letter in range(len(self.__letters)):
            self.__sense.set_pixels(self.__letters[letter])
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
        # NYI - this looked okay, but not fully vetted
        index = y * 8 + x
        print('Index: %d', index)

    def move_eraser(self):
        old_x = self.__eraser_row 
        old_y = self.__eraser_col
        pitch = self.__sense.get_orientation()['pitch']
        roll = self.__sense.get_orientation()['roll']

        if 1 < pitch < 179 and self.__eraser_row != 0:
            self.__eraser_row -= 1
        elif 359 > pitch > 179 and self.__eraser_row != 7 :
            self.__eraser_row += 1
        if 1 < roll < 179 and self.__eraser_col != 7:
            self.__eraser_col += 1
        elif 359 > roll > 179 and self.__eraser_col != 0 :
            self.__eraser_col -= 1

        old_index = self.getArrayIndex(old_x, old_y)
        new_index = self.getArrayIndex(self.__eraser_row,
                self.__eraser_col)

        self.__sense.set_pixel(old_x, old_y, GyroClear.c)
        self.__sense.set_pixel(self.__eraser_row, self.__eraser_col, GyroClear.e)

    def play_game(self, max_moves):
        count = 0
        while count < max_moves:
            self.move_eraser()
            time.sleep(0.5)
            count += 1

if __name__ == "__main__":
    game = GyroClear()
    game.clear_display()
    #game.display_current_readings()
    game.display_letters()
    #game.show_letter('a')
    #game.show_letter('s')
    #game.show_letter('p')
    game.clear_display()
    #game.play_game(100)
    game.clear_display()
