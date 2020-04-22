#### Player Class #####

class Player(object):
    def __init__(self, name, hp, mp, atk, pdef, mag, mdef, agi):
        self.hp = hp
        self.mp = mp
        self.strength = atk
        self.defense = pdef
        self.magic = mag
        self.magicdefense = mdef
        self.agility = agi
        self.owner = name
    
