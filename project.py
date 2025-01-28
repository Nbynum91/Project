from character import Player, Goblin
from tabulate import tabulate
from pyfiglet import Figlet
import os
import csv
import sys
import re

figlet = Figlet()

def main():
    figlet.getFonts()
    figlet.setFont(font="epic")
    msg = "Goblin Slayer"
    print(figlet.renderText(msg))
    function_4()
    function_5()

def function_1(number):
    if 0 < number < 5:
        with open("menu.csv", "r") as menu:
            reader = csv.reader(menu)
            for row in reader:
                if reader.line_num == number:
                    print(tabulate([row], tablefmt="double_grid"))
        return number
    else:
        raise ValueError

def function_2(menu):
    """runs input system for menu"""
    if menu == 1:
        while True:
            input_game_command = input("Input: ").lower()
            if input_game_command == "new game":
                player_name = function_3()
                with open("saved_game.csv", "w") as saved_game:
                    writer = csv.DictWriter(saved_game, fieldnames=["player name", "goblins slain"])
                    writer.writerow({"player name": "player name", "goblins slain": "goblins slain"})
                    writer.writerow({"player name": player_name, "goblins slain": "0"})
                break
            elif input_game_command == "help":
                print("Type command from menu into input as seen")
                function_1(1)
            elif input_game_command == "quit":
                sys.exit("Game Over")
            else:
                print("InputError: Type command from menu into input as seen")
                function_1(1)
    if menu == 2:
        while True:
            input_game_command = input("Input: ").lower()
            if input_game_command == "new game":
                player_name = function_3()
                with open("saved_game.csv", "w") as saved_game:
                    writer = csv.DictWriter(saved_game, fieldnames=["player name", "goblins slain"])
                    writer.writerow({"player name": "player name", "goblins slain": "goblins slain"})
                    writer.writerow({"player name": player_name, "goblins slain": "0"})
                break
            elif input_game_command == "continue":
                break
            elif input_game_command == "help":
                print("Type command from menu into input as seen")
                function_1(2)
            elif input_game_command == "quit":
                sys.exit("Game Over")
            else:
                print("InputError: Type command from menu into input as seen")
                function_1(2)
    if menu == 3:
        player = Player()
        while True:
            input_game_command = input("Input: ").lower()
            if input_game_command == "fight":
                function_n()
                print(player)
                function_1(3)
            elif input_game_command == "help":
                print("Type command from menu into input as seen")
                function_1(3)
            elif input_game_command == "quit":
                sys.exit("Game Over")
            else:
                print("InputError: Type command from menu into input as seen")
                function_1(3)

    if menu == 4:
        input_game_command = input("Input: ").lower()
        if input_game_command == "attack":
            return "attack"
        elif input_game_command == "run":
            return "run"
        elif input_game_command == "help":
            print("Type command from menu into input as seen")
        elif input_game_command == "quit":
            sys.exit("Game over")
        else:
            print("InputError: Type command from menu into input as seen")

def function_3():
    while True:
        player_name = input("Player Name: ").strip()
        test = re.search(r"^[a-z ]{1,25}$", player_name, re.IGNORECASE)
        if test:
            return player_name
        else:
            print("InputError: Name must contain only letters, spaces and be between one and twenty-five charactes in length")

def function_4():
    """tries to load saved game or create new save"""
    file_path = "saved_game.csv"
    if os.path.exists(file_path):
        function_2(function_1(2))
    else:
        function_2(function_1(1))



def function_5():
    """runs player decisions to enter combat or quit while displaying goblins slain"""
    player = Player()
    while True:
        print(player)
        function_2(function_1(3))


def function_n():
    """runs combat between goblin and player"""
    player = Player()
    goblin = Goblin()
    while goblin.health > 0 and player.health > 0:
        player.get_health()
        print(goblin)
        function_1(4)
        input_game_command = function_2(4)
        if input_game_command == "attack":
            goblin.attacked(player.damage, player.health)
            goblin.death()
            player.attacked(goblin.damage, goblin.health)
            player.death()

        elif input_game_command == "run":
            player.attacked(goblin.damage, goblin.health)
            player.run()
            break


if __name__ == "__main__":
    main()



