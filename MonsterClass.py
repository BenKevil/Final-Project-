from CombatClass import Combat

class Monster(Combat):
  def __init__(self, name, hp, atk, end, mag, res, agi, loot, exp):
    Combat.__init__(self, name, hp, atk, end, mag, res, agi)
    self.loot = loot
    self.exp = exp
      

