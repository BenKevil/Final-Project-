from MonsterClass import Monster



class Combat(Monster):


    battle = 0
    sorigin = 0
    dorigin = 0
    strike = 0

    while(battle == 0):
        action = "Attack: 1", "Defend: 2", "Magic: 3", "Flee: 4"
        moveset = "Attack: 1", "Heal: 2", "None: 3"
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

#####################
### Main
####################


Hero = Fiends("Hero", 10, 10, 2, 0, 10 ,5, 13)
d1 = Fiends("Knight", 10, 5, 2, 0, 5 ,5, 12)
print Hero
print d1

Hero.Combat(d1)
