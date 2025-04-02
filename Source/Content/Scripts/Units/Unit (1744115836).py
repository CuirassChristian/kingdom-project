import cave

class Unit(cave.Component):

	name = ""
	moveSpeed = 5

	def start(self, scene: cave.Scene):
		
		pass
			
	def moveTo (self, pos: cave.Vector3):
		pass

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	