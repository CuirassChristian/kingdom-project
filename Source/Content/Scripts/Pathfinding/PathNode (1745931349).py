import cave

class PathNode(cave.Component):
	x = 0
	y = 0
	
	obstacle : bool = False

	def __init__(self):
		cave.Component.__init__(self)
		pass
	
	def start(self, scene: cave.Scene):
		self.ref_Pathfinding = None
		self.obstacle : bool = False
		pass

	def setPathfinderRef(self, e:cave.Entity):
		if e is not None:
			print("set")
			self.ref_Pathfinding = e.getPy("Pathfinder")
		

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	