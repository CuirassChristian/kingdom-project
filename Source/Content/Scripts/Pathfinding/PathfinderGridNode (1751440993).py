import cave

class PathfinderGridNode(cave.Component):
	
	gridSizeX : int = 0
	gridSizeY : int = 0
	gridSpacing : float = 0
	pathfinder_ref = None
	
	def start(self, scene: cave.Scene):
		self.pathNodeObj = self.entity.getChild("PathNode")
		self.pathfinder_ref = self.entity.getRootParent()
		self.pathfinding_script = self.pathfinder_ref.getPy("Pathfinder")
		self.generateGrid()
		pass
		
	def generateGrid(self):
	
		xC : int = 0
		yC : int = 0

		for x in range(self.gridSizeX):
			for y in range(self.gridSizeY):
				self.createNode(x, y)
				yC += 1
			xC += 1
				
		self.pathNodeObj.setActive(False, cave.getScene())
					
	def createNode(self, x, y):
		scene = cave.getScene()
		newNode = scene.copyEntity(self.pathNodeObj)
		newNode.activate(scene)
		tf = newNode.getTransform()
		offset = cave.Vector3(-0.41, 0.05, -0.41)
		pos = offset + cave.Vector3(x / self.gridSizeX ,0,y / self.gridSizeY) 
		pathNode = newNode.getPy("PathNode")
		
		if pathNode is not None:
			self.pathfinding_script.register_pathnode(pathNode)
			pathNode.update_xy(x,y)
		
		if tf is not None:
			tf.position = pos

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	