import cave

class Unit(cave.Component):

	name = ""
	moveSpeed = 5
	targetPos : cave.Vector3 = None

	def __init__(self):
		cave.Component.__init__(self)
		pass
	
	def start(self, scene: cave.Scene):
		targetPos : cave.Vector3 = None
		pass
			
	def moveTo (self, pos: cave.Vector3):
		targetPos = pos
		pass

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	