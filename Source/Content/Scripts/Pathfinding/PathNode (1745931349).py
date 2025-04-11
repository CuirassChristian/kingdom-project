import cave

class PathNode(cave.Component):
	
	obstacle : bool = False

	def __init__(self):
		cave.Component.__init__(self)
		pass
	
	def start(self, scene: cave.Scene):
		self.obstacle : bool = False
		self.position = None
		self.x : int = 0
		self.y : int = 0
		self.nodeObject = None
		pass

	def update_xy(self, x, y):
		self.x = x 
		self.y = y

	def __eq__(self, other):
		return self.position == other.position
		

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	