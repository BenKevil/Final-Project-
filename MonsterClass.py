### Monster Class ###

class Monster(object):
  def __init__(self, name, hp, mp, strength, defense, magic, magicdefense, agility, loot, lootchance):
    self.hp = hp
    self.mp = mp
    self.strength = strength
    self.defense = defense
    self.magic = magic
    self.magicdefense = magicdefense
    self.agility = agility
    self.loot = loot
    self.lootchance = lootchance
    self.owner = name
  def __str__(self):
    return "Monster={}, HP={}, HP={}, Strength={}, Defense={}, Magic={}, Magic Defense={}, Agility={}"\
      .format(self.owner, self.hp, self.mp, self.strength, self.defense, self.magic, self.magicdefense, self.agility)



class SmallMonster(Monster):
  # A monster archtype that is small, would usually have high agility, low hp, etc
  pass


class MediumMonster(Monster):
  # A monster of medium size, average stats all around
  pass

class LargeMonster(Monster):
  # A monster of large size, low speed but high hp
  pass


class MagicMonster(Monster):
  # A monster that primarily uses magic attacks
  pass



