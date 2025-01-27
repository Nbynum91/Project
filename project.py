from goblin import Goblin
from player import Player
from tabulate import tabulate
from pyfiglet import Figlet
import csv
import os
import sys

figlet = Figlet()

def main():
    figlet.getFonts()
    figlet.setFont(font="epic")
    msg = "Goblin Slayer"
    print(figlet.renderText(msg))
    function_3()
    function_4()

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
            input_game_command = input(("Input: ").lower()).strip()
            if input_game_command == "new game":
                player_name = input("Player Name: ")
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
            input_game_command = input(("Input: ").lower()).strip()
            if input_game_command == "new game":
                player_name = input("Player Name: ")
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
                function_2(2)
    if menu == 3:
        player = Player()
        while True:
            input_game_command = input(("Input: ").lower()).strip()
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
        input_game_command = input(("Input: ").lower()).strip()
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
    """tries to load saved game or create new save"""
    try:
        with open("saved_game.csv", "r") as saved_game:
            reader = csv.DictReader(saved_game)
            function_2(function_1(2))

    except:
        function_2(function_1(1))


def function_4():
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
        with open("saved_game.csv", "r") as saved_game:
            reader = csv.DictReader(saved_game)
            for row in reader:
                print(f"{row["player name"]} has {player.health} hp")
        print(goblin)
        function_1(4)
        input_game_command = function_2(4)
        if input_game_command == "attack":
            goblin.attacked(player.damage)
            if goblin.health <= 0:
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
                break
            player.attacked(goblin.damage)
            if player.health <= 0:
                with open("saved_game.csv", "r") as saved_game:
                    reader = csv.DictReader(saved_game)
                    for row in reader:
                        print(f"{row["player name"]} has been slain by goblins!")
                os.remove("saved_game.csv")
                sys.exit("Game over")
        elif input_game_command == "run":
            player.attacked(goblin.damage)
            if player.health > 0:
                with open("saved_game.csv", "r") as saved_game:
                    reader = csv.DictReader(saved_game)
                    for row in reader:
                        print(f"{row["player name"]} has run away!")
                break
            else:
                with open("saved_game.csv", "r") as saved_game:
                    reader = csv.DictReader(saved_game)
                    for row in reader:
                        print(f"{row["player name"]} has been slain by goblins while running away!")
                os.remove("saved_game.csv")
                sys.exit("Game Over")

if __name__ == "__main__":
    main()
