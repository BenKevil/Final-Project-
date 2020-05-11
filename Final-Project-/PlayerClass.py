from CombatClass import Combat
from random import *
from time import sleep

class Player(Combat):
  #sets player states
  def __init__(self, name, hp, atk, end, mag, res, agi):
    Combat.__init__(self, name, hp, atk, end, mag, res, agi):

  
Hero = Player("boy", randint(14, 20), randint(4, 7), randint(3, 6), randint(4,7),\
        randint(3, 6), randint(4, 8))
