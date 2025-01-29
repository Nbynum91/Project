# Goblin Slayer
### Video Demo:
Example URL

### Description:
Goblin Slayer is a text based, turn based game written in python where the user uses the terminal to interact with the game.

### Additional Installation
pip install tabulate

pip install pyfiglet

### How to Use
#### Begin
Start by running project.py. Upon start the user will see in the terminal window a title displaying Goblin Slayer using pyfiglet. Underneath the title the first menu options will be displayed with "input: " below that. The menu will differ depending on if the user has a saved_game.csv from prior usage. The menu will display; New Game, Help, Quit or Continue, New Game, help and Quit.

#### Entering Commands
The user will enter commands displayed by the menu as seen into the "input: ". The commands are not case sensitive. If the user does not enter a command seen in the menu a message will display "InputError: Type command from menu into input as seen". The menu options will change depending on what the user enters but the options "Help" and "Quit" will always be present. Upon typing "help" into the "input: ", the terminal will display a reminder "Type command from menu into input as seen" and redisplay the menu with the "input: " below. If the user enters "quit" into the "input: ", the system will exit reading a message "Game Over".

#### Starting a New Game
Upon starting the program, the user will have the option to enter "New Game". Entering this into the "input: " will then display a new input option displaying "Player Name: ". The user may enter a name into "Player Name: " that they desire. The name must contain only letters, spaces and be no more than twenty-five characters in length. If the user does not meet these requirements a message will display "InputError: Name must contain only letters, spaces and be between one and twenty-five charactes in length". Upon entering an acceptable name the program will create a new csv document titled saved_game containing the user name and goblins slain. The user will then see in the terminal their chosen name and amount of goblins they have slain.

#### Continue
If the user has already created a game a new menu option will be displayed at the start of the program continue. Upon entering Continue into the "input: " the terminal will display a the player name and goblins slain from a previous game.

#### Fight
After choosing "New Game" or "Continue" the user will see a new menu option "Fight". Upon entering fight into the "input: ", the user will enter combat with a goblin where a new player object and goblin object will be created. The terminal will then display the player name and how much they have. Underneath that will display how much health the goblin has. Below that will display two new menu options "Attack" and "Run"

#### Attack
Entering attack into the "input: " will run a check with a 1/4 chance to fail each for the player and goblin to attack eachother as long as they have health above zero. If either fail, a message will display stating they "attacked and missed". Upon success a random number will be chosen between one and twenty as their damage and display in the terminal how much damage they did. This will be applied to the health of who was attacked upon which the player and goblin health will be displayed again with the prior menu below that. When the goblin health reaches zero or below a message will display "Goblin is slain!" and append the saved_game.csv adding to the goblins slain. If the player health reaches zero or below a message will display the player name "has been slain by goblins!" while deleting the saved_game.csv and exiting the system with the message "Game Over".

#### Run
Entering run into the "input: " will allow the goblin to attack the player. If the players health does not reach zero or below the combat will end and the user will returned to the prior menu with the option to fight.
