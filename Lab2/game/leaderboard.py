# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self, name, score):
		self.board.append([Score(name), Score(score)])

	# prints the leaderboard
	def print_board(self):
		for i in range(self.size):
			print("place, name, moves")
			print ((i+1), board(2*i), board((2*i)+1))

	# checks if given score should be in the leaderboard
	def update(self, score):
		raise ValueError ('todo')

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score, i):
		raise ValueError ('todo')
