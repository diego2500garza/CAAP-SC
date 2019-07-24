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

# class Name(Scene):

# 	name = ''

# 	def enter(self):
# 		return self.action()

# 	def action(self):


# 	def exit_scene(self,outcome):
# 		return outcome

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
			return self.exit_scene('guards')
		else:
			print ("The lock buzzes one last time and then you hear a sickening BOOM")
			return self.exit_scene('death')

	def exit_scene(self, outcome):
		return outcome


class Guards(Scene):

	name = "guards"

	def enter(self):
		print("Security guards heard some disturbance, you hear the footsteps get nearer and nearer. You notice it's only 3 guards... What do you do?")
		return self.action()

	def action(self):
		choice = input("\n1) -  shoot them \n2) - punch them \n3) - try reasoning with them\n")
		
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
			print ("You blast all three security guards to death! However, the loud blast alerted others...")
			return self.exit_scene('foot_steps')
		elif int(choice) == 2:
			print ("You try every mixed martial arts move you have under you sleeve, but it's to no luck. They beat you to death.")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print ("What are you doing? They're security guards. You get arrested and killed.")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name) 

	def exit_scene(self,outcome):
		return outcome


class Foot_Steps(Scene):

	name = "footsteps"

	def enter(self):
		print("The blast rings around the surrounding area! Many more guards are coming and you hear their footsteps...30? 50? 10000? 99999999? Nobody knows. What do you do now?")
		return self.action()

	def action(self):
		choice = input("\n1) -  Run away! \n2) - Put on uniform of one of the dead guards! \n3) - Get ready for the ultimate shootout!\n")
		
		if choice == ':q':
			return self.exit_scene(choice) 

		try:
		   choice = int(choice)
		except (1, 2, 3):
		   print("That's not an option!")
		   return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("Your quick animalistic instincts make you run as fast as possible. You go left, then right, then head up to some stairs...")
			return self.exit_scene('hallway')
		elif int(choice) == 2:
			print ("Nice thinking! They will never be able to guess who you are with their uniform on! The many guards approach quickly...")
			return self.exit_scene('others')
		elif int(choice) == 3:
			print("You've seen this in the movie so many times, and you're ready when they arrive, but they're so many! You are able to hide behind a couple crates and take out at least a dozen of them before your thigh gets shot ... then your arm ... then your chest ... you take your last breath knowing you fought bravely to the end")	
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)


	def exit_scene(self,outcome):
		return outcome

#Others pathway
class Others(Scene):

	name = 'others'

	def enter(self):
		print("The other guards arrive quickly. How do you get yourself out of this situation?")
		return self.action()

	def action(self):
		choice = input("\n1) -  Say that an escapee ran away through the hallway up ahead. \n2) - Pretend like nothing happened and try walking away. \n3) - Claim ignorance. You don't know what happened.\n")
		
		if choice == ':q':
			return self.exit_scene(choice) 

		try:
		   choice = int(choice)
		except (1, 2, 3):
		   print("That's not an option!")
		   return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("Smart, the guards keep on the hallway and you successfully distract them as you continue your journey")
			return self.exit_scene('pub_Entrance')
		elif int(choice) == 2:
			print ("what do you expect? They are suspicious and notice your badge doesn't match your appearance. They arrest you and kill you. dummy")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print("They're not dumb. They get suspicious and notice the blood on your uniform. They do not believe you and kill you on the spot.")	
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self,outcome):
		return outcome

# class Pub(Scene):

# 	name = 'pub_Entrance'

# 	def enter(self):
# 		return self.action()

# 	def action(self):


# 	def exit_scene(self,outcome):
# 		return outcome


#Hallway pathway
class Hallway(Scene):

	name = 'hallway'

	def enter(self):
		print("Running as fast as possible, you keep heading down the hallway until it splits into two pathways. There's a sign. Go left for Storage, right for Infirmary. What do you choose?")
		return self.action()

	def action(self):
		choice = input("\n1) -  Storage, maybe you can hide somewhere in there? \n2) - The infimary! There probably isn't anybody in there. \n")
		
		if choice == ':q':
			return self.exit_scene(choice) 

		try:
		   choice = int(choice)
		except (1, 2):
		   print("That's not an option!")
		   return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("Left has always been your lucky hand! The Storage door is only a couple steps away.")
			return self.exit_scene('storage')
		elif int(choice) == 2:
			print ("The Infirmary! Everybody is so focused on invasion that there probably isn't anybody in there.")
			return self.exit_scene('infirmary')

		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self,outcome):
		return outcome

class Storage(Scene):

	name = 'storage'

	def enter(self):
		print("Alrighty, you're at the storage door, but something is stopping you from getting in! It's asking for some kind of code.")

		return self.action()

	def action(self):
		print ("There's a keypad lock on the door")
		code = []
		for i in range(3):
			number = random.randint(1,10)
			code.append(number)
		guesses = 0
		# loop to check three random integers, one at a time
		for i in (3):
			print ("Enter digit %d." % (i+1))
			guess = input("[keypad]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			   guess = int(guess)
			except 0 != guess//2:
			   print("That's not an int!")
			   return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <5:
				print ("The guards are getting closer!")
				guesses += 1
				guess =input("[keypad]> ")
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)

		
		if guesses < 5:
			print ("The Storage door opened! Nice!")
			return self.exit_scene('box')
		else:
			print ("You took too long. The guards find you and ray gun your butt to death.")
			return self.exit_scene('death')

	def exit_scene(self,outcome):
		return outcome

class Box(Scene):

	name = 'box'

	def enter(self):
		print("The room is deathly quiet. There's a bunch of boxes around the room. All the guards are approaching the room...")
		return self.action()

	def action(self):
		choice = input("\n1) -  Throw a rock to distract them. \n2) - Shoot!!! \n3) - Get in a box and stay quiet. Shhhh..\n")
		
		if choice == ':q':
			return self.exit_scene(choice) 

		try:
		   choice = int(choice)
		except (1, 2, 3):
		   print("That's not an option!")
		   return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("You are really dumb. They see you throw it and shoot you instantly.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("Heck yeah! You kill the two guards that enter, but then more come in. You have no more ammo anymore and they shoot you to death.")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print("The guards don't look inside the boxes and they go away to the Infirmary.")	
			return self.exit_scene('escape')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self,outcome):
		return outcome


class Escape(Scene):

	name = 'escape'

	def enter(self):
		print("A long time passes (30 minutes? an hour? 2 hours? who knows.) and you take a nap. You get out of the box and start looking for an exit.")
		return self.action()

	def action(self):
		print ("You look around for an exit. You walk what must be 2 miles to the back of the Storage facility. You find 3 large, different doors with greek letter labels. What do you pick?")
		choice = input("\n1) -  Alpha \n2) - Beta \n3) - Gamma\n")
		
		if choice == ':q':
			return self.exit_scene(choice) 

		try:
		   choice = int(choice)
		except (1, 2, 3):
		   print("That's not an option!")
		   return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("You enter the war room and see top generals discussing war plans. They see you and shoot you.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("The room is full of nukes and the door sets off an alarm. Accidentally, one goes off and the entire ship is blown up.")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print("Exit!")	
			return self.exit_scene('exit')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)


	def exit_scene(self,outcome):
		return outcome

class Infirmary(Scene):

	name = 'infirmary'

	def enter(self):
		print("Welp, that didn't plan out. There's lots of aliens around. What do you do?")
		return self.action()

	def action(self):
		choice = input("\n1) -  Fake an injury. Maybe they'll help you? \n2) - Shoot up in the air. Maybe they don't have a gun to shoot back and they'll get scared? \n3) - Revolution! This always works in the movies. Maybe they'll revolutionize?\n")
		
		if choice == ':q':
			return self.exit_scene(choice) 

		try:
		   choice = int(choice)
		except (1, 2, 3):
		   print("That's not an option!")
		   return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("Yeah, they don't help you. They all jump you and punch you to death.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("They all get scared. They don't have guns!")
			return self.exit_scene('ask')
		elif int(choice) == 3:
			print("Yeah, no. They all (even the injured ones) take offense and jump you.")	
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self,outcome):
		return outcome

class Ask(Scene):

	name = 'ask'

	def enter(self):
		print("They're all scared! You want to ask them something. What should you do?")
		return self.action()

	def action(self):
		choice = input("\n1) -  Ask for exit and start leaving fast \n2) - Ask for the exit. Once they give it, grab a hostage and shoot in the air to keep them scared. You leave slowly \n3) - These people have killed your people. Ask for their main commander on the ship to kill them.\n")

		if choice == ':q':
			return self.exit_scene(choice) 

		try:
		   choice = int(choice)
		except (1, 2, 3):
		   print("That's not an option!")
		   return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("Haha! You run fast to the exit, but as you reach for the door, you get shot in the back.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("The aliens are too scared to ask for help. You get to the exit and walk in with your hostage.")
			return self.exit_scene('boarding')
		elif int(choice) == 3:
			print("You head towards the main room to kill their leader, but he is well guarded. You try to shoot him, but a guard shoots you first.")	
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self,outcome):
		return outcome

class Boarding(Scene):

	name = 'boarding'

	def enter(self):
		print("")
		return self.action()

	def action(self):


	def exit_scene(self,outcome):
		return outcome



