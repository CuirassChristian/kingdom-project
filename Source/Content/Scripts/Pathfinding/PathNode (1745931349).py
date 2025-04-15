import cave

class PathNode(cave.Component):
	
	obstacle : bool = False
	mesh = None
	highlighted_material = None

	def __init__(self):
		cave.Component.__init__(self)
		pass
	
	def start(self, scene: cave.Scene):
		self.obstacle : bool = False
		self.position = None
		self.x : int = 0
		self.y : int = 0

		self.mesh = self.entity.get("Mesh")

		self.unhighlight()

		self.nodeObject = None
		pass

	def unhighlight(self):
		if self.mesh is not None:
			material = self.mesh.material
			self.mesh.tint = cave.Vector4(3, 3, 3, 0.25)

	def highlight(self):
		if self.mesh is not None:
			material = self.mesh.material
			self.mesh.tint = cave.Vector4(0, 20, 0, 0.5)

	def highlight_path(self):
		if self.mesh is not None:
			material = self.mesh.material
			self.mesh.tint = cave.Vector4(15, 15, 0, 0.5)

	def update_xy(self, x, y):
		self.x = x 
		self.y = y

	def __eq__(self, other):
		return self.position == other.position
		

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	