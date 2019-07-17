class Score(object):
	name = 'player'
	score = 0

	# initializes score and players name
	def __init__(self, name, score):
		self.name = name
		self.score = score

	# returns the name associated with score
	def get_name(name):
		return self.name

	# returns score of player
	def get_score(score):
		return self.score
