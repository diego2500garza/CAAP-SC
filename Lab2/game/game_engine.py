# This is the engine of the game, basically runs everything

class Engine(object):

	# global variables to keep track of game status and live count
	escaped = False
	lives = 0

	# initializes the map in the game
	def __init__(self, scene_map, lives):
		self.scene_map = scene_map #a_map gets assigned to scene_map, then initializing it to self.scene_map
		self.lives = lives

	# takes current scene, plays it, gets the next scene, and updates the game
	# should also return the number of moves the game takes in total
	def play(self):
		current_scene = self.scene_map.opening_scene() #scene_map refers to map object we created, then calls opening_scene function in map.py
		next_scene_name = ''
		checkpoint = current_scene
		n_moves = 0
		while (next_scene_name != 'finished' and self.lives > 0):
			print ("\n*******************************************************************") #raise ValueError ('todo')
			# print(current_scene)
			print("You have",self.lives,"lives left")
			next_scene_name = current_scene.enter() 
			#calling enter bc of (). Assigns next_scene_name as whatever comes from enter function
			if (next_scene_name == ':q'):
				exit(1)
			elif (next_scene_name == 'death'): #goes through the scene of died (goes through death file)
				checkpoint = current_scene
				n_moves += 1
				current_scene = self.scene_map.next_scene(next_scene_name)
			elif (next_scene_name == 'died'): #gives the outcome of going through death scene
				self.lives -=1
				current_scene = checkpoint
			else:
				n_moves += 1
				current_scene = self.scene_map.next_scene(next_scene_name) #references earlier variable in line11 and uses function next_scene in map.py, puts in next_scene_name
				#goes through and starts loop over again for the next scene
			if (next_scene_name == 'finished'):
				self.escaped = True
		return n_moves


# updates the variable to determine whether player won or failed.
	def won(self):
		if (self.escaped == True):
			return True
		if (self.escaped == False):
			return False
