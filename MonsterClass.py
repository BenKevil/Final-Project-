### Monster Class ###

class Monster(object):

  # Initializes the Monster class, giving various stats 
  def __init__(self, name, hp, mp, atk, pdef, mag, mdef, agi):
    self.hp = hp
    self.mp = mp
    self.strength = atk
    self.defense = pdef
    self.magic = mag
    self.magicdefense = mdef
    self.agility = agi
    self.owner = name
  #Physically prints the stats of each monster introduced
  def __str__(self):
    return "Monster={}, HP={}, HP={}, Strength={}, Defense={}, Magic={}, Magic Defense={}, Agility={}"\
      .format(self.owner, self.hp, self.mp, self.strength, self.defense, self.magic, self.magicdefense, self.agility)





