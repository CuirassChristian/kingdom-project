import cave

class Pathfinder(cave.Component):

	gridSizeX : int = 0
	gridSizeY : int = 0
	gridSpacing : float = 0.25
	number_of_pathnodes = 0
	
	pathnode_list = []

	def __init__(self):
		cave.Component.__init__(self)
		pass
		
	def start(self, scene: cave.Scene):
		self.transf = self.entity.getTransform()
		self.nodeObj = self.entity.getChild("PathfinderGridNode")
		self.pathnode_list = []
		self.generateGrid()
		
	def register_pathnode(self, p):
		self.pathnode_list.append(p)
		self.number_of_pathnodes = len(self.pathnode_list)
		#print(len(self.pathnode_list))

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
		if events.active(cave.event.KEY_F):
			print(len(self.pathnode_list))
		
	def end(self, scene: cave.Scene):
		pass
	