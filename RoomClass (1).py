### Room Class ###
from Tkinter import *
from CombatClass import *
from random import randint
from time import sleep
global hero
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
                Mon = Monster("Monster", 50)
                # first, the room name
                s = "You begin to enter the room, when suddenly a monster! \n"
                hero.battle(Mon)
                # next, the exits from the room
                s += "You can feintly make out two doors,\nwhat should you do?:\n"
                for exit in self.exits.keys():
                        s += exit + " "

                return s

class ExitRoom(Room):
       def __str__(self):
                Mon = Monster("Fiend", 1000, 3)
                # first, the room name
                s = "You enter the room, seeing a locked gate. \n"
                hero.battle(Mon)
                s += "You can feintly make out three doors one of which is locked,\nwhat should you do?:\n"
                for exit in self.exits.keys():
                        s += exit + " "

                return s

class VictoryRoom(Room):
       def __str__(self):
                # first, the room name
                s = "You step outside of the dungeon, finally free. \n"
                # next, the exits from the room
                s += "You have won!\n"

                return s

class HallRoom(Room):
        def __str__(self):
                # first, the room name
                s = "You make your way along the corridor,when a monster appears! \n"

                hero.battle(Mon)
                # next, the exits from the room
                s += "There are only two ways to go, which direction do you go?:\n"
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
                r1 = StartingRoom("StartRoom", "FBeginingRoom.gif")
                r2 = HallRoom("GoblinRoom", "FinalGhastRoom.gif")
                r3 = HallRoom("SkeletonRoom", "FinalKnightRoom.gif")
                r4 = HallRoom("SpiderRoom", "FinalLichRoom.gif")
                r5 = HallRoom("SpiderRoom", "FinalNecroRoom.gif")
                r6 = MonsterRoom("SpiderRoom", "FinalSpiderRoom.gif")
                r7 = MonsterRoom("SpiderRoom", "FinalZombieRoom.gif")
                r8 = MonsterRoom("SpiderRoom", "FinalBoss.gif")
                r9 = ExitRoom("SpiderRoom", "LockedDoor.gif")
                r10 = VictoryRoom("SpiderRoom", "FinalEscapeRoom.gif")
                

                
                #add any items and exits to each room
 
                # ROOM 1
                #r1 exits
                r1.addExit("south", r4)
                r1.addExit("west",r3)
                r1.addExit("north", r2)
                r1.addExit("east", r5)


                # ROOM 2
                #r2 exits
                r2.addExit("west", r6)
                r2.addExit("east",r7)

                # ROOM 3
                #r3 exits
                r3.addExit("north", r7)
                r3.addExit("south", r9)
                

                # ROOM 4
                #r4 exits
                r4.addExit("west", r8)
                r4.addExit("east", r9)

                # ROOM 5
                #r5 exits
                r5.addExit("north", r6)
                r5.addExit("south", r8)

                # ROOM 6
                #r6 exits
                r6.addExit("south", r5)
                r6.addExit("east", r2)

                # ROOM 7
                #r7 exits
                r7.addExit("west", r2)
                r7.addExit("south", r3)

                #Need locked exit here
                
                # ROOM 8
                #r8 exits
                r8.addExit("north", r5)
                r8.addExit("east", r4)
                
                # ROOM 9
                #r9 exits
                r9.addExit("north", r3)
                r9.addExit("west", r4)
                
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
                Game.image = Label(self, width = WIDTH/2, image = img)
                Game.image.pack(side=LEFT, fill = Y)
                Game.image.pack_propagate(False) #dont let img change widget size

                #setp text output on right of display
                text_frame = Frame(self, width=WIDTH/2)
                Game.text = Text(text_frame, bg="black",fg = "Green", state= DISABLED)
                Game.text.pack(fill=Y,expand=1)
                text_frame.pack(side=RIGHT,fill=Y)
                text_frame.pack_propagate(False) #dont let img change widget size
		

        # sets the current room image
        def setRoomImage(self):
                if(Game.currentRoom ==None):
                        Game.img = PhotoImage(file="skull.gif")
                else:
                        Game.img= PhotoImage(file=Game.currentRoom.image)

                Game.image.config(image=Game.img)
                Game.image.image=Game.img
                

        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
                #clear the previuous text
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0",END)

                #if dead, say so, set text to __str__
                if(Game.currentRoom == None):
                        Game.text.insert(END, "You are dead. You may quit. \m")
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
                        #call the updates
                        self.setStatus(response)
                        self.setRoomImage()
                        Game.player_input.delete(0,END)

class Player(Combat):
        #sets player states
        def __init__(self, name):
                Combat.__init__(self, name, 17, randint(5, 8),\
                randint(4, 6), randint(5, 8), randint(4, 6), randint(3, 9))
                self.maxhp = 17

        def damage(self, offensive, defensive):
                result = offensive - defensive
                print result
                if (result > 0):
                        return result
                else:
                        return 1

        def battle(self, other):
                #clear the previuous text
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0",END)
                combat = True
                while (combat):
                        if (self.hp == 0):
                                Game.currentRoom = None
                                combat = False
                        elif (other.hp == 0):
                                self.hp = self.maxhp
                                combat = False
                        else:
                                Game.text.insert(END, "Physical or Magical?")
                                battletype = Game.player_input.get()
                                battletype = battletype.lower()
                                if (self.agi > other.agi):
                                        if (battletype == "physical"):
                                                #clear the previuous text
                                                Game.text.config(state=NORMAL)
                                                Game.text.delete("1.0",END)
                                                dealt = self.damage(self.atk, other.end)
                                                Game.text.insert(END, ("The {} took {} {} damage.".format(other.name, dealt, battletype)))
                                                sleep(0.1)
                                                other.hp -= dealt
                                        else:
                                                #clear the previuous text
                                                Game.text.config(state=NORMAL)
                                                Game.text.delete("1.0",END)
                                                dealt = self.damage(self.mag, other.res)
                                                Game.text.insert(END, ("The {} took {} {} damage.".format(other.name, dealt, battletype)))
                                                sleep(0.1)
                                                other.hp -= dealt
                                                enemy = randint(0, 1)
                                        if (other.hp == 0):
                                                self.hp = self.maxhp
                                                combat = False
                                                break
                                        elif (enemy == 0):
                                                #clear the previuous text
                                                Game.text.config(state=NORMAL)
                                                Game.text.delete("1.0",END)
                                                received = self.damage(other.atk, self.end)
                                                Game.text.insert(END, ("{} took {} physical damage.".format(self.name, received)))
                                                sleep(0.1)
                                                self.hp -= received
                                        else:
                                                #clear the previuous text
                                                Game.text.config(state=NORMAL)
                                                Game.text.delete("1.0",END)
                                                received = self.damage(other.mag, self.res)
                                                Game.text.insert(END, ("{} took {} physical damage.".format(self.name, received)))
                                                sleep(0.1)
                                                self.hp -= received

                                else:
                                        enemy = randint(0, 1)
                                        if (enemy == 0):
                                                #clear the previuous text
                                                Game.text.config(state=NORMAL)
                                                Game.text.delete("1.0",END)
                                                received = self.damage(other.atk, self.end)
                                                Game.text.insert(END, ("{} took {} physical damage.".format(self.name, received)))
                                                sleep(0.1)
                                                self.hp -= received
                                        else:
                                                #clear the previuous text
                                                Game.text.config(state=NORMAL)
                                                Game.text.delete("1.0",END)
                                                received = self.damage(other.mag, self.res)
                                                Game.text.insert(END, ("{} took {} physical damage.".format(self.name, received)))
                                                sleep(0.1)
                                                self.hp -= received
                                        if (self.hp == 0):
                                                combat = False
                                                Game.currentRoom = None
                                                break
                                        elif (battletype == "physical"):
                                                #clear the previuous text
                                                Game.text.config(state=NORMAL)
                                                Game.text.delete("1.0",END)
                                                dealt = self.damage(self.atk, other.end)
                                                Game.text.insert(END, ("The {} took {} {} damage.".format(other.name, dealt, battletype)))
                                                sleep(0.1)
                                                other.hp -= dealt
                                        else:
                                                #clear the previuous text
                                                Game.text.config(state=NORMAL)
                                                Game.text.delete("1.0",END)
                                                dealt = self.damage(self.mag, other.res)
                                                Game.text.insert(END, ("The {} took {} {} damage.".format(other.name, dealt, battletype)))
                                                sleep(0.1)
                                                other.hp -= dealt

class Monster(Combat):
        def __init__(self, name, exp, boost = 0):
                Combat.__init__(self, name, randint(6, 9)+boost, randint(4, 6)+boost,\
                                randint(3, 5)+boost, randint(6, 9)+boost, randint(4, 6)+boost,\
                                randint(3, 10)+boost)
                self.exp = exp
                
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600
hero = Player("Hero")
                        
                                                
                                                
                                
                                
                                

                                        
            


