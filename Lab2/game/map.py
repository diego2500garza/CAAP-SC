# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter, 
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	#key is strings, value is function
	scenes = {'central_corridor' : S.CentralCorridor(), #class names bc they're capitalized. calling class name __init__. String keys are assigned to the scene object. They're scene objects because () calling the constructorn function inside class
				'laser_weapon_armory' : S.LaserWeaponArmory(),
				'death' : Death()
				# raise ValueError ('todo')
				}
	
	# initializes to a starting scene
	def __init__(self, start_scene): #this is the constructor
		self.start_scene = start_scene
	
	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name):
		return self.scenes.get(scene_name) #sending in scene_name, self.start_scene is assigned as scene_name SAME VALUE THO
		#self.scenes in this line gets
	
	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene) # Dominos calling Papa Johns, start_scene is order