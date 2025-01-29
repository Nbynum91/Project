import csv
import random
import os
import sys

class Player:
    """creates the player object with health and damage constants"""
    def __init__(self):
        self.health = 50
        self.damage = 20

    """returns player as str displaying player name and goblins slain from saved_game.csv"""
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

    """runs the check if player is hit by goblin, displaying a message of how much damage or if attack missed"""
    def attacked(self, d, h):
        if h > 0:
            damaged = random.randint(1, d)
            dice = random.randint(1, 4)
            if dice == 1:
                print("Goblin attacked and missed!")
            else:
                print("Goblin did", damaged, "damage!")
                self.health -= damaged

    """checks player health and displays message if below 0 while exiting the game and deleting the saved_game.csv"""
    def death(self):
        if self.health <= 0:
            with open("saved_game.csv", "r") as saved_game:
                reader = csv.DictReader(saved_game)
                for row in reader:
                    print(f"{row["player name"]} has been slain by goblins!")
            os.remove("saved_game.csv")
            sys.exit("Game over")

    """allows player to attempt to run away from goblin"""
    def run(self):
        if self.health > 0:
            with open("saved_game.csv", "r") as saved_game:
                reader = csv.DictReader(saved_game)
                for row in reader:
                    print(f"{row["player name"]} has run away!")
        else:
            with open("saved_game.csv", "r") as saved_game:
                reader = csv.DictReader(saved_game)
                for row in reader:
                    print(f"{row["player name"]} has been slain by goblins while running away!")
            os.remove("saved_game.csv")
            sys.exit("Game Over")

    """prints current health of player"""
    def get_health(self):
        with open("saved_game.csv", "r") as saved_game:
            reader = csv.DictReader(saved_game)
            for row in reader:
                print(f"{row["player name"]} has {self.health} hp")

class Goblin:
    """creates the goblin object with health and damage as constants"""
    def __init__(self):
        self.health = 30
        self.damage = 20

    def __str__(self):
        return (f"Goblin has {self.health} hp")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    """runs the check if goblin is hit by player, displaying a message of how much damage or if attack missed"""
    def attacked(self, d, h):
        if h > 0:
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

    """checks goblin health and displays message if below 0 while appending the saved_game.csv for goblins slain"""
    def death(self):
        if self.health <= 0:
            with open('saved_game.csv') as saved_game:
                reader = csv.DictReader(saved_game)
                for row in reader:
                    player_name = row["player name"]
                    new_goblins_slain = int(row["goblins slain"]) + 1
                with open("saved_game.csv", "w") as saved_game:
                    writer = csv.DictWriter(saved_game, fieldnames=["player name", "goblins slain"])
                    writer.writerow({"player name": "player name", "goblins slain": "goblins slain"})
                    writer.writerow({"player name": player_name,"goblins slain": new_goblins_slain})
            print("Goblin is slain!")
