import csv
import random

class Player:
    def __init__(self):
        self.health = 50
        self.damage = 20

    def __str__(self):
        with open("saved_game.csv", "r") as saved_game:
            reader = csv.DictReader(saved_game)
            for row in reader:
                return (f"{row["player name"]} has slain {row["goblins slain"]} goblins")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    def attacked(self, d):
        damaged = random.randint(1, d)
        dice = random.randint(1, 4)
        if dice == 1:
            print("Goblin attacked and missed!")
        else:
            print("Goblin did", damaged, "damage!")
            self.health -= damaged




"""  and slain {row["goblins slain"]} goblins"""


