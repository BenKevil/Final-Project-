from CombatClass import Combat
from random import *
from time import sleep

class Player(Combat):
  #sets player states
  def __init__(self, name, hp, atk, end, mag, res, agi):
    Combat.__init__(self, name, hp, atk, end, mag, res, agi)
    self.inventory = []
    
  def victory(loot, exp):
    print "You won! /n You gained {} exp and the enemy dropped a {}".format(exp,/
                                                                            loot)
    self.inventory.append(loot)

  def defeated():
    print "{} never return from their quest."
    sleep(2)
    print "/n Game Over"
    
  def __battle__(self, other):
    combat = True
    while (combat):
      if (self.hp == 0):
        defeated()
      elif (other.hp == 0):
        victory(other.loot, other.exp)
      else:
        battletype = raw_input("Physical or Magical? ")
        battletype = battletype.lower()
        try:
          if (battletype == "physical"):
            dealt = damage(self.atk, other.end)
            print ("The {} took {} {} damage.").format(other.name,/
                                                       dealt, battletype)
          else:
            dealt = damage(self.mag, other.res)
            print ("The {} took {} {} damage.").format(other.name,/
                                                       dealt, battletype)
          enemy = randint(0, 1)
          if (other.hp == 0):
            combat = False
            victory(other.loot, other.exp)
            break
          elif (enemy == 0):
            received = damage(other.atk, self.end)
            print ("{} took {} physical damage.").format(self.name, received)
          else:
            received = damage(other.mag, self.res)
            print ("{} took {} physical damage.").format(self.name, received)

        except (other.agi > self.agi):
          enemy = randint(0, 1)
          if (enemy == 0):
            received = damage(other.atk, self.end)
            print ("{} took {} physical damage.").format(self.name, received)
          else:
            received = damage(other.mag, self.res)
            print ("{} took {} physical damage.").format(self.name, received)
          if (self.hp == 0):
            combat = False
            defeated()
            break
          elif (battletype == "physical"):
            dealt = damage(self.atk, other.end)
            print ("The {} took {} {} damage.").format(other.name,/
                                                       dealt, battletype)
          else:
            dealt = damage(self.mag, other.res)
            print ("The {} took {} {} damage.").format(other.name,/
                                                       dealt, battletype)
  
Hero = Player("boy", randint(14, 20), randint(4, 7), randint(3, 6), randint(4,7),\
        randint(3, 6), randint(4, 8))
