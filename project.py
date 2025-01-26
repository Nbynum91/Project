from goblin import Goblin
from player import Player
from tabulate import tabulate
from pyfiglet import Figlet
import csv
import os

figlet = Figlet()

def main():
    figlet.getFonts()
    figlet.setFont(font="epic")
    msg = "Goblin Slayer"
    print(figlet.renderText(msg))
    function_1()
    function_2()

def function_1():
    try:
        with open("saved_game.csv", "r") as saved_game:
            reader = csv.DictReader(saved_game)
        while True:
            with open("menu.csv", "r") as menu:
                reader = csv.reader(menu)
                for row in reader:
                    if reader.line_num == 2:
                        print(tabulate([row], tablefmt="double_grid"))
                        input_game_command = input("Input: ").lower()
                        if input_game_command == "new game":
                            player_name = input("Player Name: ")
                            with open("saved_game.csv", "w") as saved_game:
                                writer = csv.DictWriter(saved_game, fieldnames=["player name", "goblins slain"])
                                writer.writerow({"player name": "player name", "goblins slain": "goblins slain"})
                                writer.writerow({"player name": player_name, "goblins slain": "0"})

                            return False
                        elif input_game_command == "continue":

                            return False
                        elif input_game_command == "help":
                            print("Type command in input as seen")
                        elif input_game_command == "quit":
                            print("Game Over")
                            return False
                        else:
                            print("Error: Type command in input as seen")
    except:
        while True:
            with open("menu.csv", "r") as menu:
                reader = csv.reader(menu)
                for row in reader:
                    if reader.line_num == 1:
                        print(tabulate([row], tablefmt="double_grid"))
                        input_game_command = input("Input: ").lower()
                        if input_game_command == "new game":
                            player_name = input("Player Name: ")
                            with open("saved_game.csv", "w") as saved_game:
                                writer = csv.DictWriter(saved_game, fieldnames=["player name", "goblins slain"])
                                writer.writerow({"player name": "player name", "goblins slain": "goblins slain"})
                                writer.writerow({"player name": player_name, "goblins slain": "0"})

                            return False
                        elif input_game_command == "help":
                            print("Type command in input as seen")
                        elif input_game_command == "quit":
                            print("Game Over")
                            return False
                        else:
                            print("Error: Type command in input as seen")

def function_2():
    """runs player decisions to enter combat or quit"""
    player = Player()
    while True:
        print(player)
        with open("menu.csv", "r") as menu:
            reader = csv.reader(menu)
            for row in reader:
                if reader.line_num == 3:
                    print(tabulate([row], tablefmt="double_grid"))
        input_game_command = input("Input: ").lower()
        if input_game_command == "fight":
            result = function_n()
            if result == "dead":
                print("Game Over")
                return False
        elif input_game_command == "help":
            print("Type command in input as seen")
        elif input_game_command == "quit":
            print("Game Over")
            return False
        else:
            print("Error: Type command in input as seen")

def function_n():
    """runs combat mode with goblins"""
    player = Player()
    goblin = Goblin()
    while goblin.health > 0 and player.health > 0:
        with open("saved_game.csv", "r") as saved_game:
            reader = csv.DictReader(saved_game)
            for row in reader:
                print(f"{row["player name"]} has {player.health} hp")
        print(goblin)
        with open("menu.csv", "r") as menu:
            reader = csv.reader(menu)
            for row in reader:
                if reader.line_num == 4:
                    print(tabulate([row], tablefmt="double_grid"))
        input_game_command = input("Input: ").lower()
        if input_game_command == "attack":
            goblin.attacked(player.damage)
            player.attacked(goblin.damage)
            if player.health <= 0:
                with open("saved_game.csv", "r") as saved_game:
                    reader = csv.DictReader(saved_game)
                    for row in reader:
                        print(f"{row["player name"]} has been slain by goblins!")
                os.remove("saved_game.csv")
                break
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
                
        elif input_game_command == "help":
            print("Type command in input as seen")
        else:
            print("Error: Type command in input as seen")
    if player.health <= 0:
        return "dead"

if __name__ == "__main__":
    main()
