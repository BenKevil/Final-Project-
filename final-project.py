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
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate dictionary
		self._items[item] = desc

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
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
    origin = 0
    moveset = "Enchanted Strike: 1", "Heal: 2", "None: 3"
    while(battle == 0):
      first = self.agility - b.agility
      print "Which magic do you want to use" +str(moveset)+""
      strike = input()
      if strike == 1:
        if self.mp > 6:
          print ""+str(self.owner)+"'s magic is being added to its atk"
          origin = self.strength
          self.strength = self.strength + (self.magic - b.magicdefense)
          self.mp = self.mp - 6
        else:
          print ""+str(self.owner)+"'s mp is too low"
      if strike == 2:
        print ""+str(self.owner)+"'s hp is being healed"
        self.hp = self.hp + self.magic
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
      
      if strike == 1:
        self.strength = origin
      
      

  def __str__(self):
    return Monster.__str__(self)


#####################
### Main
####################


Hero = Fiends("Hero", 10, 10, 2, 0, 10 ,5, 13)
d1 = Fiends("Knight", 10, 5, 2, 0, 5 ,5, 12)
f1 = Fiends("Slime", 4, 2, 2, 0, 5 ,5, 12)
print Hero
print d1
print f1
Hero.Combat(d1)
Hero.Combat(f1)
