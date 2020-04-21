########################
# Final Project code ###
########################

class Room(object):
    # getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def objects(self):
		return self._objects

	@objects.setter
	def objects(self, value):
		self._objects = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addobject(self, item, desc):
		# append the item and description to the appropriate dictionary
		self._objects[objects] = desc

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def additem(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delitem(self, item):
		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s


<<<<<<< HEAD
##class Monster(object):
##  def __init__(self, name, hp, mp, atk, pdef, mag, mdef, agi):
##    self.hp = hp
##    self.mp = mp
##    self.strength = atk
##    self.defense = pdef
##    self.magic = mag
##    self.magicdefense = mdef
##    self.agility = agi
##    self.owner = name
##  def __str__(self):
##    return "Monster={}, HP={}, HP={}, Strength={}, Defense={}, Magic={}, Magic Defense={}, Agility={}"\
##      .format(self.owner, self.hp, self.mp, self.strength, self.defense, self.magic, self.magicdefense, self.agility)
##
##class Fiends(Monster):
##  def __init__(self, name, hp, mp, atk, pdef, mag, mdef, agi):
##    Monster.__init__(self, name, hp, mp, atk, pdef, mag, mdef, agi)
##    self.hp = hp
##    self.mp = mp
##    self.strength = atk
##    self.defense = pdef
##    self.magic = mag
##    self.magicdefense = mdef
##    self.agility = agi
##
##  def Combat(self, b):
##    battle = 0
##    origin = 0
##    moveset = "Attack: 1", "Heal: 2", "None: 3"
##    while(battle == 0):
##      first = self.agility - b.agility
##      print "Which magic do you want to use" +str(moveset)+""
##      strike = input()
##      if strike == 1:
##        if self.mp > 6:
##          print ""+str(self.owner)+"'s magic is being added to its atk"
##          origin = self.strength
##          self.strength = self.strength + (self.magic - b.magicdefense)
##          self.mp = self.mp - 6
##        else:
##          print ""+str(self.owner)+"'s mp is too low"
##      if strike == 2:
##        print ""+str(self.owner)+"'s hp is being healed"
##        self.hp = self.hp + self.magic
##      if first > 0:
##        b.hp = b.hp - (self.strength - b.defense)
##        print "Attacker Hit"
##        print ""+str(b.owner)+"'s Hp = " +str(b.hp)+""
##        if b.hp <= 0:
##          battle = 1
##          print ""+str(b.owner)+" lose"
##        else:
##          self.hp = self.hp - (b.strength - self.defense)
##          print "Defender Hit"
##          print ""+str(self.owner)+"'s Hp = " +str(self.hp)+""          
##          if self.hp <= 0:
##            battle = 1
##            print ""+str(self.owner)+" lose"
##
##      else:
##        self.hp = self.hp - (b.strength - self.defense)
##        print "Defender Hit"
##        print ""+str(self.owner)+"'s Hp = " +str(self.hp)+""
##        if self.hp <= 0:
##          battle = 1
##          print ""+str(self.owner)+" lose"
##        else:
##          b.hp = b.hp - (self.strength - b.defense)
##          print "Attacker Hit"
##          print ""+str(b.owner)+"'s Hp = " +str(b.hp)+""
##          if b.hp <= 0:
##            battle = 1
##            print ""+str(b.owner)+" lose"
##      
##      if strike == 1:
##        self.strength = origin
##      
##      
##
##  def __str__(self):
##    return Monster.__str__(self)

class Game(object):
        def __init__(self):
                pass

        def createRooms(self):
                r1 = Room()
                r2 = Room()
                r3 = Room()

                #r1 exits
                r1.addExit("north", r2)
                r1.addExit("west",h3)
                #r1 grabbables
                r1.addItem("key")
                #r1 items
                r1.addobjects("clock","A clock is seen ticking away, however it seems to move at a rate far faster than normal time would allow.")
                r1.addobjects("dinning-table", "The table is decorated with various silverwear and plates. A key is seen under the serving tray.")
                r1.addobjects("chandelier", "A golden chandelier hangs in the center of the room. Casting a dim light onto the rest of the space.")

                #Sets the default room to r1
                Game.currentRoom = r1
=======
class Monster(object):
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
    return "Monster={}, HP={}, HP={}, Strength={}, Defense={}, Magic={}, Magic Defense={}, Agility={}"\
      .format(self.owner, self.hp, self.mp, self.strength, self.defense, self.magic, self.magicdefense, self.agility)

class Fiends(Monster):
  def __init__(self, name, hp, mp, atk, pdef, mag, mdef, agi):
    Monster.__init__(self, name, hp, mp, atk, pdef, mag, mdef, agi)
    self.hp = hp
    self.mp = mp
    self.strength = atk
    self.defense = pdef
    self.magic = mag
    self.magicdefense = mdef
    self.agility = agi

  def Combat(self, b):
    battle = 0
    sorigin = 0
    dorigin = 0
    strike = 0
    while(battle == 0):
      action = "Attack: 1", "Defend: 2", "Magic: 3", "Flee: 4"
      moveset = "Enchanted Strike: 1", "Heal: 2", "None: 3"
      print "What Command will you like to do?" +str(action)+""
      command = input()
      if command == 2:
        sorigin = self.strength
        dorigin = self.defense
        self.strength = 0
        self.defense = self.defense * 2

      if command == 3:
        print "Which magic do you want to use" +str(moveset)+""
        strike = input()
        if strike == 1:
          if self.mp > 6:
            print ""+str(self.owner)+"'s magic is being added to its atk"
            sorigin = self.strength
            self.strength = self.strength + (self.magic - b.magicdefense)
            self.mp = self.mp - 6
          else:
            print ""+str(self.owner)+"'s mp is too low"
          if strike == 2:
            print ""+str(self.owner)+"'s hp is being healed"
            self.hp = self.hp + self.magic

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

  def __str__(self):
    return Monster.__str__(self)
>>>>>>> 6529730cfb7b742311f5ac40039e8ea7d5905d12

                #Initalize the player's iventory
                Game.inventory = []

        def setStatus(self, status):
                #if dead, say so, set text to __str__
                if(Game.currentRoom == None):
                        print "You fall from the balcony, you are dead. You may quit."
                else:
                        print "You are carrying: " +str(Game.inventory) + (status)

        # plays the game
        def play(self):
                # add the rooms to the game
                self.createRooms()

        # processes the player's input
        def process(self, event):
                #set a default response
                response = "I dont understand. Try noun verb. Valib verbs are go, look, and take."
                #get the command line input from the GUI
                action = Game.player_input.get()
                action = action.lower()
                
                #handle exits
                if (action == "quit" or action == "exit"):
                        exit(0)
                        
                
                #handle end of game
                if (Game.currentRoom == None):
                        Game.player_input.delete(0,END)
                        return
                #handle verbs and nouns
                words = action.split()
                if(len(words) == 2):
                        verb = words[0]
                        noun = words[1]

                        #process go
                        if(verb == "go"):
                                #default response
                                response = "Invalid exit."

                                #check the currentRoom exits

                                if (noun in Game.currentRoom.exits):
                                        #if valid, update
                                        Game.currentRoom = Game.currentRoom.exits[noun]
                                        #notify user
                                        response = "Room changed."
                        #Process look
                        elif(verb == "look"):
                                #default response
                                response = "I dont see it."

                                if (noun in Game.currentRoom.items):
                                        response = Game.currentRoom.items[noun]

                        #process take
                        elif (verb == "take"):
                                #default response
                                response = "I dont see that item."

                                #check current rooms grabbables
                                for grabbable in Game.currentRoom.grabbables:
                                        if(noun == grabbable):
                                                #add to inventory
                                                Game.inventory.append(grabbable)
                                                #set the response
                                                response = "{} grabbed.".format(grabbable)
                                                #remove from room
                                                Game.currentRoom.delGrabbable(grabbable)
                                                #exit the loop
                                                break
                
        
#####################
### Main
####################

# create the game
g = Game()
# play the game
g.play()


##Hero = Fiends("Hero", 10, 10, 2, 0, 10 ,5, 13)
##d1 = Fiends("Knight", 10, 5, 2, 0, 5 ,5, 12)
##f1 = Fiends("Slime", 4, 2, 2, 0, 5 ,5, 12)
##print Hero
##print d1
##print f1
##Hero.Combat(d1)
##Hero.Combat(f1)
