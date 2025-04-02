import cave

class PathNode(cave.Component):
	x = 0
	y = 0
	ref_pathfinder : Pathfinder = None
	
	def start(self, scene: cave.Scene):
		pass

	def setPathfinderRef(path:Pathfinder):
		self.ref_pathfinder = path
		if ref is not None:
			print("Pathnode registered to pathfinder")
		pass

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	