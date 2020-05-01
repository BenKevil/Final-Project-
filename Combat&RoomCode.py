### Room Class ###
from Tkinter import *
from random import randint
import random
#from PlayerClass import Player
#from MonsterClass import Monster
#from CombatClass import Combat

#Monster Class
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
    
#Where all combantant info is stored for combat class
class Fiends(Monster):
  def __init__(self, name, hp, mp, strength, defense, magic, magicdefense, agility, loot, lootchance):
    Monster.__init__(self, name, hp, mp, strength, defense, magic, magicdefense, agility, loot, lootchance)
    self.hp = hp
    self.mp = mp
    self.strength = strength
    self.defense = defense
    self.magic = magic
    self.magicdefense = magicdefense
    self.agility = agility
    self.loot = loot
    self.lootchance = lootchance
#Abriged version of the Combat Class
  def Combat(self, b):
    global text
    battle = 0
    sorigin = self.strength
    dorigin = self.defense
    strike = 0
    luck = 0
    limit = 4
    #Check to see who go first.
    first = self.agility - b.agility
    text = "A "+str(b.owner)+" Appear!!\n"
    while(battle == 0):
      if first > 0:
        b.hp = b.hp - (self.strength - b.defense)
        text += "Attacker Hit\n"
        text += ""+str(b.owner)+"'s Hp = " +str(b.hp)+"\n"
        if b.hp <= 0:
          text += ""+str(b.owner)+" lose\n"
          battle = 1
        else:
          self.hp = self.hp - (b.strength - self.defense)
          text += "Defender Hit\n"
          text += ""+str(self.owner)+"'s Hp = " +str(self.hp)+"\n"        
          if self.hp <= 0:
            text += ""+str(self.owner)+" lose\n"
            battle = 1

      else:
        self.hp = self.hp - (b.strength - self.defense)
        text += "Defender Hit\n"
        text += ""+str(self.owner)+"'s Hp = " +str(self.hp)+"\n"
        if self.hp <= 0:
          text += ""+str(self.owner)+" lose\n"
          battle = 1
        else:
          b.hp = b.hp - (self.strength - b.defense)
          text += "Attacker Hit\n"
          text += ""+str(b.owner)+"'s Hp = " +str(b.hp)+"\n"
          if b.hp <= 0:
            text += ""+str(b.owner)+" lose\n"
            battle = 1

      if b.hp <= 0:
        luck = randint(0, 100)
        if b.owner == "Knight":
          text += "Roll a " +str(luck)+"\n"
          if luck >= b.lootchance:
            text += ""+str(self.owner)+" has obtained a " +str(b.loot)+". Increase Strength by 2.\n"
            self.strength = self.strength + 2
          if luck < b.lootchance:
            text += ""+str(self.owner)+" failed to find anything"
            
  def __str__(self):
    return Monster.__str__(self)

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room(object):
	# the constructor
	def __init__(self, name, image):
		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits = {}
		self.items = {}
		self.grabbables = []

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

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
class StartingRoom(Room):
        def __str__(self):
                # first, the room name
                s = "You are in complete darkness, you cannot see.\n"
                # next, the exits from the room
                s += "You can feintly make out two doors,\nwhich way should you go?:\n"
                for exit in self.exits.keys():
                        s += exit + " "

                return s
class MonsterRoom(Room):
       def __str__(self):
                # first, the room name
                s = "You begin to enter the room, when suddenly a goblin! \n"
                # next, the exits from the room
                s += "You can feintly make out two doors,\nwhich way should you go?:\n"
                for exit in self.exits.keys():
                        s += exit + " "

                return s



# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
        # the constructor
        def __init__(self, parent):
        # call the constructor in the superclass
                Frame.__init__(self, parent)

        # creates the rooms
        def createRooms(self):
                # Initalizes the rooms
                r1 = StartingRoom("StartRoom", "StartingRoom.gif")
                r2 = MonsterRoom("GoblinRoom", "GoblinRoom.gif")
                r3 = MonsterRoom("SkeletonRoom", "DungeonRoom2.gif")
                r4 = MonsterRoom("SpiderRoom", "DungeonRoom4.gif")
                

                
                #add any items and exits to each room
 
                # ROOM 1
                #r1 exits
                r1.addExit("south", r3)
                r1.addExit("west",r2)
                #r1 grabbables
                r1.addGrabbable("torch")


                # ROOM 2
                #r2 exits
                r2.addExit("south", r4)
                r2.addExit("east",r1)
                #r2 items
               

                # ROOM 3
                #r3 exits
                r3.addExit("north", r1)
                r3.addExit("west", r4)
                #r3 grabbables
                r3.addGrabbable("book")
                #r3 items
                

                # ROOM 4
                #r4 exits
                r4.addExit("north", r2)
                r4.addExit("east", r3)
                
                #r4 items
                

                #r4 grabbables
                r4.addGrabbable("sheets")
               

                #Sets the default room to r1
                Game.currentRoom = r1

                #Initalize the player's iventory
                Game.inventory = []
                
               
	# sets up the GUI
        def setupGUI(self):
                #organize and pack the GUI
                self.pack(fill=BOTH, expand=1)

                #setup player input (bottom)
                Game.player_input = Entry(self, bg = "black", fg = "Green")
                Game.player_input.bind("<Return>", self.process)
                Game.player_input.pack(side=BOTTOM,fill=X)
                Game.player_input.focus()


                #setup the imagine on the left of the display
                img = None
                Game.image = Label(self, width = 400, image = img)
                Game.image.pack(side=LEFT, fill = Y)
                Game.image.pack_propagate(False) #dont let img change widget size

                #setp text output on right of display
                text_frame = Frame(self, width=400)
                Game.text = Text(text_frame, bg="black",fg = "Green", state= DISABLED)
                Game.text.pack(fill=Y,expand=1)
                text_frame.pack(side=RIGHT,fill=Y)
                text_frame.pack_propagate(False) #dont let img change widget size
		

        # sets the current room image
        #Need to change this back to where the image are stored.
        def setRoomImage(self):
                if(Game.currentRoom ==None):
                        Game.img = PhotoImage(file="skull.gif")
                else:
                        Game.img = PhotoImage(file=Game.currentRoom.image)

                Game.image.config(image=Game.img)
                Game.image.image=Game.img
                

        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
                #clear the previuous text
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0",END)

                #if dead, say so, set text to __str__
                if(Game.currentRoom == None):
                        Game.text.insert(END, "You fall from the balcony, you are dead. You may quit. \m")
                else:
                        Game.text.insert(END,str(Game.currentRoom)+ \
                                         "\nYou are carrying: " +str(Game.inventory)+
                                         "\n\n" + status)
                        Game.text.config(state=DISABLED)
                        

        # plays the game
        def play(self):
                # add the rooms to the game
                self.createRooms()
                # configure the GUI
                self.setupGUI()
                # set the current room
                self.setRoomImage()
                # set the current status
                self.setStatus("")

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
                        #Added fight function. Trigger Combat verus goblin once user type "fight"
                        elif (verb == "fight"):
                            Hero = Fiends("Hero", 50, 50, 10, 10, 10 ,10, 10, "", 0)
                            d1 = Fiends("Goblin", 20, 15, 5, 0, 0, 0, 5, "Short Sword", 60)
                            Hero.Combat(d1)
                            response = text

                        #call the updates
                        self.setStatus(response)
                        self.setRoomImage()
                        Game.player_input.delete(0,END)


# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()                       
