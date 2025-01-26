import csv
import random

class Goblin:
    def __init__(self):
        self.health = 30
        self.damage = 20

    def __str__(self):
        return (f"Goblin has {self.health} hp")

    @classmethod
    def get(cls):
        damage = random.randint(1, 5)
        return cls(damage)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    def attacked(self, d):
        damaged = random.randint(1, d)
        dice = random.randint(1, 4)
        if dice == 1:
            with open("saved_game.csv", "r") as saved_game:
                reader = csv.DictReader(saved_game)
                for row in reader:
                    print(f"{row["player name"]} attacked and missed!")
        else:
            with open("saved_game.csv", "r") as saved_game:
                reader = csv.DictReader(saved_game)
                for row in reader:
                    print(f"{row["player name"]} did", damaged, "damage!")
            self.health -= damaged






