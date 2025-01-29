from character import Player, Goblin
from tabulate import tabulate
from pyfiglet import Figlet
import os
import csv
import sys
import re

figlet = Figlet()

def main():
    """prints title and runs function_4 and function_5"""
    figlet.getFonts()
    figlet.setFont(font="epic")
    msg = "Goblin Slayer"
    print(figlet.renderText(msg))
    function_4()
    function_5()

def function_1(number):
    """displays menu system based on row number from csv"""
    if 0 < int(number) < 5:
        with open("menu.csv", "r") as menu:
            reader = csv.reader(menu)
            for row in reader:
                if reader.line_num == number:
                    print(tabulate([row], tablefmt="double_grid"))
                    list = row
        return list
    else:
        raise ValueError

def function_2(list, input_game_command):
    """runs input system based on what menu is loaded"""
    while True:
        if input_game_command.title() not in list:
            return "InputError: Type command from menu into input as seen"
        elif input_game_command.title() == "Help":
            return "Type command from menu into input as seen"
        elif input_game_command.title() == "Quit":
            sys.exit("Game Over")
        else:
            return input_game_command.capitalize()

def function_3(player_name):
    """checks input from player_name to be acceptable format"""
    while True:
        test = re.search(r"^[a-z ]{1,25}$", player_name, re.IGNORECASE)
        if test:
            return player_name
        else:
            print("InputError: Name must contain only letters, spaces and be between one and twenty-five charactes in length")
            player_name = input("Player Name: ").strip()

def function_4():
    """allows new game or continue from save based off saved_game.csv availability"""
    file_path = "saved_game.csv"
    if os.path.exists(file_path):
        while True:
            input_game_command = function_2(function_1(2), input("input: "))
            if input_game_command == "New game":
                player_name = function_3(input("Player Name: ").strip())
                with open("saved_game.csv", "w") as saved_game:
                    writer = csv.DictWriter(saved_game, fieldnames=["player name", "goblins slain"])
                    writer.writerow({"player name": "player name", "goblins slain": "goblins slain"})
                    writer.writerow({"player name": player_name, "goblins slain": "0"})
                break
            elif input_game_command == "Continue":
                break
            else:
                print(input_game_command)
    else:
        while True:
            input_game_command = function_2(function_1(1), input("input: "))
            if input_game_command == "New game":
                player_name = function_3(input("Player Name: ").strip())
                with open("saved_game.csv", "w") as saved_game:
                    writer = csv.DictWriter(saved_game, fieldnames=["player name", "goblins slain"])
                    writer.writerow({"player name": "player name", "goblins slain": "goblins slain"})
                    writer.writerow({"player name": player_name, "goblins slain": "0"})
                break
            else:
                print(input_game_command)

def function_5():
    """runs player decisions to enter combat or quit while displaying goblins slain from object/class player"""
    player = Player()
    while True:
        print(player)
        input_game_command = function_2(function_1(3), input("input: "))
        if input_game_command == "Fight":
            function_6()
        else:
            print(input_game_command)

def function_6():
    """runs combat between goblin and player using their object/class"""
    player = Player()
    goblin = Goblin()
    while goblin.health > 0 and player.health > 0:
        player.get_health()
        print(goblin)
        input_game_command = function_2(function_1(4), input("input: "))
        if input_game_command == "Attack":
            goblin.attacked(player.damage, player.health)
            goblin.death()
            player.attacked(goblin.damage, goblin.health)
            player.death()
        elif input_game_command == "Run":
            player.attacked(goblin.damage, goblin.health)
            player.run()
            break
        else:
            print(input_game_command)

if __name__ == "__main__":
    main()
