from MonsterClass import Monster
from PlayerClass import Player
    
class Combat(Monster, Player):
    battle = 0
    sorigin = self.strength
    dorigin = self.defense
    strike = 0
    luck = 0
    limit = 4

    while(battle == 0):
      action = "Attack: 1", "Defend: 2", "Magic: 3", "Flee: 4"
      moveset = "Enchanted Strike: 1", "Heal: 2", "None: 3"
      print "What Command will you like to do?" +str(action)+""
      command = input()
      while command >= 5:
        print "Choice invalid. Please select a correct choice."
        print "What Command will you like to do?" +str(action)+""
        command = input()

      if command == 2:
        self.strength = 0
        self.defense = self.defense * 2

      if command == 3:
        print "Which magic do you want to use" +str(moveset)+""
        strike = input()

        while strike >= limit:
          print "Choice invalid. Please select a correct choice."
          print "Which magic do you want to use" +str(moveset)+""
          strike = input()

        if strike == 1:
          if self.mp >= 6:
            print ""+str(self.owner)+"'s magic is being added to its atk"
            sorigin = self.strength
            self.strength = self.strength + (self.magic - b.magicdefense)
            self.mp = self.mp - 6
          else:
            print ""+str(self.owner)+"'s mp is too low"

        if strike == 2:
            if self.mp >= 4:
              print ""+str(self.owner)+"'s hp is being healed"
              self.hp = self.hp + self.magic
              self.strength = 0
              self.mp = self.mp - 6
            else:
              print ""+str(self.owner)+"'s mp is too low"

      first = self.agility - b.agility
      if first > 0:
        b.hp = b.hp - (self.strength - b.defense)
        print "Attacker Hit"
        print ""+str(b.owner)+"'s Hp = " +str(b.hp)+""
        if b.hp <= 0:
          battle = 1
          print ""+str(b.owner)+" lose"
        else:
          self.hp = self.hp - (b.strength - self.defense)
          print "Defender Hit"
          print ""+str(self.owner)+"'s Hp = " +str(self.hp)+""          
          if self.hp <= 0:
            battle = 1
            print ""+str(self.owner)+" lose"

      else:
        self.hp = self.hp - (b.strength - self.defense)
        print "Defender Hit"
        print ""+str(self.owner)+"'s Hp = " +str(self.hp)+""
        if self.hp <= 0:
          battle = 1
          print ""+str(self.owner)+" lose"
        else:
          b.hp = b.hp - (self.strength - b.defense)
          print "Attacker Hit"
          print ""+str(b.owner)+"'s Hp = " +str(b.hp)+""
          if b.hp <= 0:
            battle = 1
            print ""+str(b.owner)+" lose"
      
      if command == 2:
        self.defense = dorigin
        self.strength = sorigin
      if strike == 1:
        self.strength = sorigin
      if strike == 2:
        self.strength = sorigin

      if b.hp <= 0:
        luck = randint(0, 100)
        if b.owner == "Goblin":
          print "Roll a " +str(luck)+""
          if luck >= b.lootchance:
            print ""+str(self.owner)+" has obtained a " +str(b.loot)+". Increase Strength by 2."
            self.strength = self.strength + 2
          if luck < b.lootchance:
            print ""+str(self.owner)+" failed to find anything"
            
  def __str__(self):
    return Monster.__str__(self)

#####################
### Main
####################
Hero = Player(" Hero", 10, 10, 2, 0, 5, 5, 12)
d1 = Monster(" Goblin", 10, 5, 2, 0, 5 ,5, 12, "Short Sword", 60)
print Hero
print d1



