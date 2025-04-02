import cave

class PathfinderGridNode(cave.Component):
	
	gridSizeX : int = 0
	gridSizeY : int = 0
	gridSpacing : float = 0
	
	def start(self, scene: cave.Scene):
		self.pathNodeObj = self.entity.getChild("PathNode")
		self.pathfinder_ref = None
		self.pathfinder_ref = self.entity.getRootParent()
		self.generateGrid()
		pass
		
	def generateGrid(self):
	
		for x in range(self.gridSizeX):
			for y in range(self.gridSizeY):
				self.createNode(x, y)
				
		self.pathNodeObj.setActive(False, cave.getScene())
					
	def createNode(self, x, y):
		scene = cave.getScene()	
		newNode = scene.copyEntity(self.pathNodeObj)
		newNode.activate(scene)
		tf = newNode.getTransform()
		offset = cave.Vector3(-0.41, 0.05, -0.41)
		pos = offset + cave.Vector3(x / self.gridSizeX ,0,y / self.gridSizeY) 
		pathNode : PathNode = None
		pathNode = newNode.getPy("PathNode")
		if self.pathfinder_ref is not None:
			print ("We have pathfinder ref")
		
		if pathNode is not None:
			pathNode.x = x
			pathNode.y = y
			#pathNode.setPathfinderReg(pathfinder_ref.getPy("Pathfinder"))
		
		if tf is not None:
			tf.position = pos

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	