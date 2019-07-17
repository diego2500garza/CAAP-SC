# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ""
leaderboard = Leaderboard(name, moves)



# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves

	print ("\nGame Over.")
	if (won == True):
		print("you won")
		self.leaderboard.print_board()
	if (won == False):
		print("you lost")


# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name
		global moves
		print ("Welcome to my game! To quit enter :q at any time. You will have three lives. Good luck!") # raise ValueError ('todo')
		name == input("\nLet's play. Enter your name. > ") # raise ValueError ('todo')
		if (name == ":q"):
			exit(1)
		a_map = Map("central_corridor") # raise ValueError ('todo')
		a_game = Engine(a_map)
		games = a_game.play()
		Engine.play(a_game)
		game_over(a_game.won())
play_game()
