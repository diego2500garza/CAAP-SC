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
name = ''
leaderboard = Leaderboard()


# for any function, we are getting the RETURN VALUEEE


# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	print ("\nGame Over\n")
	print("Moves taken:", moves,"\n\n")
	print("nice")
	if won == True:
		print("Congratulations! You won!\n\n")
		if leaderboard.update(score) == True:
			leaderboard.insert(score)
	else:
		print("You lost!\n\n")
	leaderboard.print_board()
	name = ""
	moves = 0

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name 
		global moves 
		print ("Welcome to my game! To quit enter :q at any time. Good luck!") # raise ValueError ('todo')
		print("How many lives would you like?")
		lives = input("Easy - 7-10 lives\nMedium - 3-6 lives\nHard - 1-2 lives\n")
		if lives == ':q':
			exit(1)
		try:
			lives = int(lives)
		except ValueError:
			exit(1)
		name = input("\nLet's play. Enter your name. > ") # raise ValueError ('todo')
		if (name == ":q"):
			exit(1)
		a_map = Map('central_corridor') #calls __init__ function
		a_game = Engine(a_map, lives) #calls __init__ function
		moves = a_game.play()
		game_over(a_game.won())
play_game()