from PlayerClass import Player
from MonsterClass import Monster
from random import randint

Gob = Monster("Goblin", 9, 6, 4, 5, 4, 7, "knife", 50)
Hero = Player("boy", randint(14, 20), 10, 3, 12,\
        3, randint(4, 8))

Hero.battle(Gob)
