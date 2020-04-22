#### Game Class ####
from Tkinter import *

from RoomClass import Game


# create the window
window = Tk()
window.title("Dungeon Crawler")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
