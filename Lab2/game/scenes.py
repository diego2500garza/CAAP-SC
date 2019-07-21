# imports random madule form library
from random import randint
from death import Death

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class CentralCorridor(Scene):
	
	name = 'central_corridor'

	def enter(self): #
		print ("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
		return self.action() #Enter calls action
		
		
	def action(self):
		print ("What will you do?")
		choice = input("\n1) - shoot \n2) - hit \n3) - insult\n")
		
		if choice == ':q':
			return self.exit_scene(choice) #Action calls exit_scene
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except (1, 2, 3):
		   print("That's not an option!")
		   return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("Quick on the draw you yank out your blaster and fire it at the Gothon.")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Like a world class boxer you dodge, weave, slip and slide right")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Lucky for you they made you learn Gothon insults in the academy.")
			return self.exit_scene('laser_weapon_armory') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name) 

	def exit_scene(self, outcome): #Little Caesers gives us our pizza
		return outcome

class LaserWeaponArmory(Scene):
	
	name = "armory"

	def enter(self):
		print ("You do a dive roll into the Weapon Armory, crouch and scan the room")
		return self.action()

	def action(self):
		print ("There's a keypad lock on the box")
		code = [1, 2, 3]
		guesses = 0
		# loop to check three random integers, one at a time
		for i in (0,1,2):
			print ("Enter digit %d." % (i+1))
			guess = input("[keypad]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			   guess = int(guess)
			except ValueError:
			   print("That's not an int!")
			   return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <10:
				print ("BZZZZEDDD!")
				guesses += 1
				guess =input("[keypad]> ")
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)
				except ValueError:
				   print("That's not an int!")
				   guess = -1
		
		if guesses < 10:
			print ("The container clicks open and the seal breaks, letting gas out.")
			return self.exit_scene('finished')
		else:
			print ("The lock buzzes one last time and then you hear a sickening")
			return self.exit_scene('death') # raise ValueError ('todo')

	def exit_scene(self, outcome):
		return outcome