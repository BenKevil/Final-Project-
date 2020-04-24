from random import randint
import random
from MonsterClass import Monster
from PlayerClass import Player
    
class Combat(Monster, Player):
    battle = 0
    strike = 0
    luck = 0
    limit = 4
    #Store the original data for player in origin.
    sorigin = Player.strength
    dorigin = Player.defense

    
    #Battle will repeat until varible Battle does not equal 1
    while(battle == 0):
      action = "Attack: 1", "Defend: 2", "Magic: 3", "Flee: 4"
      moveset = "Enchanted Strike: 1", "Heal: 2", "None: 3"
      print "What Command will you like to do?" +str(action)+""
      command = input()
        #When a number greater then 5 is input. Force player to choose again.
      while command >= 5:
        print "Choice invalid. Please select a correct choice."
        print "What Command will you like to do?" +str(action)+""
        command = input()
        #Defend command set strength to 0 and double player's defense
      if command == 2:
        Player.strength = 0
        Player.defense = Player.defense * 2
    #Command 3 allow the user to select a magic to use
      if command == 3:
        print "Which magic do you want to use" +str(moveset)+""
        strike = input()
        #Limit equal to the number of magic the user has. If user input number greater then limit force user to choose another number.
        while strike >= limit:
          print "Choice invalid. Please select a correct choice."
          print "Which magic do you want to use" +str(moveset)+""
          strike = input()
        #Basic magic command. Check if user's current mp is greater then or equal to the require amount. Increase player's strength by player's magic
        if strike == 1:
          if Player.mp >= 6:
            print ""+str(Player.owner)+"'s magic is being added to its atk"
            sorigin = Player.strength
            Player.strength = Player.strength + (Player.magic - Monster.magicdefense)
            Player.mp = Player.mp - 6
          else:
            print ""+str(Player.owner)+"'s mp is too low"
        #Basic magic command. Check if user's current mp is greater then or equal to the require amount. Restore Hp
        if strike == 2:
            if Player.mp >= 4:
              print ""+str(Player.owner)+"'s hp is being healed"
              Player.hp = Player.hp + Player.magic
              Player.strength = 0
              Player.mp = Player.mp - 6
            else:
              print ""+str(Player.owner)+"'s mp is too low"
       #Check to see if the player's agility is greater then monster
      first = Player.agility - Monster.agility
      if first > 0:
        Monster.hp = Monster.hp - (Player.strength - Monster.defense)
        print "Attacker Hit"
        print ""+str(Monster.owner)+"'s Hp = " +str(Monster.hp)+""
        #Will end battle if monster or player die
        if Monster.hp <= 0:
          battle = 1
          print ""+str(Monster.owner)+" lose"
        else:
          Player.hp = Player.hp - (Monster.strength - Player.defense)
          print "Defender Hit"
          print ""+str(Player.owner)+"'s Hp = " +str(Player.hp)+""          
          if Player.hp <= 0:
            battle = 1
            print ""+str(Player.owner)+" lose"

      else:
        Player.hp = Player.hp - (Monster.strength - Player.defense)
        print "Defender Hit"
        print ""+str(Player.owner)+"'s Hp = " +str(Player.hp)+""
        #Will end battle if monster or player die
        if Player.hp <= 0:
          battle = 1
          print ""+str(Player.owner)+" lose"
        else:
          b.hp = Monster.hp - (Player.strength - Monster.defense)
          print "Attacker Hit"
          print ""+str(Monster.owner)+"'s Hp = " +str(Monster.hp)+""
          if b.hp <= 0:
            battle = 1
            print ""+str(Monster.owner)+" lose"
      #Will any enchanted stat to thier original value for the player.
      if command == 2:
        Player.defense = dorigin
        Player.strength = sorigin
      if strike == 1:
        Player.strength = sorigin
      if strike == 2:
        Player.strength = sorigin
        #Monster loot. If luck is greater or equal to the number of the monster's loot chance. Grant players a item.
      if Monster.hp <= 0:
        luck = randint(0, 100)
        if Monster.owner == "Goblin":
          print "Roll a " +str(luck)+""
          if luck >= Monster.lootchance:
            print ""+str(Player.owner)+" has obtained a " +str(b.loot)+". Increase Strength by 2."
            Player.strength = Player.strength + 2
          if luck < Monster.lootchance:
            print ""+str(Player.owner)+" failed to find anything"
            
  def __str__(self):
    return Monster.__str__(self)

#####################
### Main
####################
Hero = Player(" Hero", 10, 10, 2, 0, 5, 5, 12)
d1 = Monster(" Goblin", 10, 5, 2, 0, 5 ,5, 12, "Short Sword", 60)
print Hero
print d1



