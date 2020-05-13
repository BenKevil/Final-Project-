from CombatClass import Combat
from time import sleep
from random import randint

class Player(Combat):
  #sets player states
  def __init__(self, name, hp, atk, end, mag, res, agi):
    Combat.__init__(self, name, hp, atk, end, mag, res, agi)
    self.inventory = []
    
  def victory(self, loot, exp):
    print ("You won! \nYou gained {} exp and the enemy dropped a {}").format(exp, loot)
    self.inventory.append(loot)
    print self.inventory
    input("press enter")

  def defeated(self):
    print "{} never return from their quest."
    sleep(2)
    print "/n Game Over"
    input("press enter")

  def damage(self, x, y):
    result = x - y
    print result
    if (result > 0):
      return result
    else:
      return 1
    
  def battle(self, other):
    combat = True
    while (combat):
      if (self.hp == 0):
        combat = False
        self.defeated()
      elif (other.hp == 0):
        combat = False
        self.victory(other.loot, other.exp)
      else:
        battletype = raw_input("Physical or Magical? ")
        battletype = battletype.lower()
        if (self.agi > other.agi):
          if (battletype == "physical"):
            dealt = self.damage(self.atk, other.end)
            print ("The {} took {} {} damage.").format(other.name, dealt, battletype)
            sleep(0.1)
            other.hp -= dealt
          else:
            dealt = self.damage(self.mag, other.res)
            print ("The {} took {} {} damage.").format(other.name, dealt, battletype)
            sleep(0.1)
            other.hp -= dealt
          enemy = randint(0, 1)
          if (other.hp == 0):
            combat = False
            self.victory(other.loot, other.exp)
            break
          elif (enemy == 0):
            received = self.damage(other.atk, self.end)
            print ("{} took {} physical damage.").format(self.name, received)
            sleep(0.1)
            self.hp -= received
          else:
            received = self.damage(other.mag, self.res)
            print ("{} took {} physical damage.").format(self.name, received)
            sleep(0.1)
            self.hp -= received

        else:
          enemy = randint(0, 1)
          if (enemy == 0):
            received = self.damage(other.atk, self.end)
            print ("{} took {} physical damage.").format(self.name, received)
            sleep(0.1)
            self.hp -= received
          else:
            received = self.damage(other.mag, self.res)
            print ("{} took {} physical damage.").format(self.name, received)
            sleep(0.1)
            self.hp -= received
          if (self.hp == 0):
            combat = False
            self.defeated()
            break
          elif (battletype == "physical"):
            dealt = self.damage(self.atk, other.end)
            print ("The {} took {} {} damage.").format(other.name, dealt, battletype)
            sleep(0.1)
            other.hp -= dealt
          else:
            dealt = self.damage(self.mag, other.res)
            print ("The {} took {} {} damage.").format(other.name, dealt, battletype)
            sleep(0.1)
            other.hp -= dealt

