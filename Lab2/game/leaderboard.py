# imports the score class to be used in the leaderboard.
from scores import Score
import random
# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 5
	board = []


	def __init__(self):
		for i in range(self.size):
			here = Score('Player', 999)
			self.board.append(here)


	# prints the leaderboard
	def print_board(self):
		print("Place Name Moves")
		for i in range(self.size):
			print(i+1 ,self.board[i].get_name(), self.board[i].get_score())

	# checks if given score should be in the leaderboard
	def update(self, score): #check if our score belongs (is it bigger than the smallest or smaller than the biggest)
		self.new_score = score.get_score()
		for i in range(self.size):
			if self.new_score <= self.board[i].get_score():
				return True


	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	
	#insert element passed in certain index thru board brackets i brackets, get rid of last element, put leaderboard in big loop
	def insert(self, score):
		for i in range(self.size):
			if self.new_score < self.board[i].get_score():
				self.board[i] = self.board[i+1]
				self.board.insert(i,score)


		# for a in range(len(self.board)):
		# 	if score <= self.board[a]:
		# 		self.board[i].insert(score)

			# self.board.append(self.board[i+1], self.board[i+2])



