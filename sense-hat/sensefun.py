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
        self.__current_letter = 0
        self.__current_state = self.__letters[self.__current_letter]

    def count_letter_blocks(self):
        """ Return number of letter blocks in the current letter
        
        It counts the number of elements that don't match the background
        colour. The current letter is stored in self.__current_state].
        """
    
        count = 0
        for e in self.__current_state:
            if e != GyroClear.b:
                count +=1
        print('Count is {0}'.format(count))
        return count


    def show_letter(self, letter):
        self.__sense.show_letter(letter)
        time.sleep(2)

    def clear_display(self):
        self.__sense.clear()

    def display_letters(self):
        for letter in range(len(self.__letters)):
            self.__sense.set_pixels(self.__letters[letter])
            time.sleep(2)

    def display_current_board(self):
        self.__sense.set_pixels(self.__current_state)


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

    def next_letter(self):
        """ Move the game to the next level

        Returns False when there are no move letters.
        """
        next_level = True

        if self.__current_letter >= (len(self.__letters) - 1):
            next_level = False
        else:
            self.__current_letter += 1
            self.__current_state = self.__letters[self.__current_letter]

        return next_level

    def getArrayIndex(self, x, y):
        """ Return index in list relative to logical 8x8 matrix """
        index = y * 8 + x
        print('Index: {0}'.format(index))
        return index

    def move_eraser(self):
        """ Move the eraser based on pitch and roll from the Gyro

        This is the brains of the game. It using values from the Gyro to move
        the eraser around the board. If it finds a block that is not the
        background colour, then appropriate updates are made.

        Return True of a block was erased.
        """

        block_erased = False
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
        print('old_index is {0} from {1},{2}'.format(old_index, old_x, old_y))
        new_index = self.getArrayIndex(self.__eraser_row, self.__eraser_col)
        print('new_index is {0} from {1},{2}'.format(new_index,
            self.__eraser_row, self.__eraser_col))
        # If new index is not background colour, then we have found a new block
        # to erase.
        if self.__current_state[new_index] != GyroClear.b:
            block_erased = True
            # Update current state to make this index background colour.
            self.__current_state[new_index] = GyroClear.b

        # Update the pixels on the sense hat display
        self.__sense.set_pixel(old_x, old_y, GyroClear.b)
        self.__sense.set_pixel(self.__eraser_row, self.__eraser_col, GyroClear.e)

        return block_erased

    def play_game(self):
        self.display_current_board()
        count = game.count_letter_blocks()
        while count > 0:
            erased = self.move_eraser()
            if erased:
                count -= 1
            time.sleep(0.25)
            print('count is {0}'.format(count))
        self.__sense.show_message('Enter secret message here',
            text_colour=GyroClear.f,
            back_colour=GyroClear.b)

if __name__ == "__main__":
    game = GyroClear()
    game.clear_display()
    #game.display_current_readings()
    #game.display_letters()
    #game.show_letter('a')
    #game.show_letter('s')
    #game.show_letter('p')
    game.clear_display()
    game.play_game()
    game.clear_display()
