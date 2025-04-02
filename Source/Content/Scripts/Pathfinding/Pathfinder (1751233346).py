import cave

class Pathfinder(cave.Component):

	gridSizeX : int = 0
	gridSizeY : int = 0
	gridSpacing : float = 0.25

	def start(self, scene: cave.Scene):
		self.transf = self.entity.getTransform()
		self.nodeObj = self.entity.getChild("PathfinderGridNode")
		self.generateGrid()

	def generateGrid(self):
	
		for x in range(self.gridSizeX):
	
			for y in range(self.gridSizeY):
				self.createNode(x, y)
				
		self.nodeObj.setActive(False, cave.getScene())
				
	def createNode(self, x, y):
		scene = cave.getScene()
		newNode = scene.copyEntity(self.nodeObj)
		newNode.activate(scene)
		tf = newNode.getTransform()
		pos = cave.Vector3(x,0,y) 
			
		if tf is not None:
			tf.position = pos
	
	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	