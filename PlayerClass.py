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
    def __str__(self):
        return "Player: HP= {}, MP= {}".format(self.hp, self.mp)


    def status():
        # A command that would tell the player their stats
        pass

    def inventory():
        #Initalize the player's iventory
                Player.inventory = []

    
    
