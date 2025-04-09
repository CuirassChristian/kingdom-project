import cave

class Pathfinder(cave.Component):

	gridSizeX : int = 0
	gridSizeY : int = 0
	gridSpacing : float = 0.25
	number_of_pathnodes = 0
	unitObj = None
	pathnode_list = []
	targetNode = None
	ref_unitmanager = None
	isInit : bool = False
	
	def __init__(self):
		cave.Component.__init__(self)
		pass
		
	def start(self, scene: cave.Scene):
		self.unit : Unit = None
		self.targetPos : cave.Vector3 = None
		self.unitObj = self.entity.getChild("Unit")
		self.transf = self.entity.getTransform()
		self.nodeObj = self.entity.getChild("PathfinderGridNode")

		self.pathnode_list = []
		self.generateGrid()
		
	def set_target_pathnode(self, p:cave.Vector3):
		self.targetNode = p
		
	def register_rts_cam(self, r):
		print ("registering rts camera")
		comm_player_obj = r.entity
		if comm_player_obj is not None:
			rts_cam = comm_player_obj.getPy("RTSCamera")
			if rts_cam is not None:
				rts_cam.ref_pathfindingscript = self
				print ("we have registered pathfinding to camera")
		
	
	def initialize(self):
		scene = cave.getScene()
		self.um_obj = scene.get("UnitManager")
		if self.um_obj is not None:
			self.ref_unitmanager = self.um_obj.getPy("UnitManager")
			if self.ref_unitmanager is not None:
				print ("we have unit manager in pathfinding")

		self.isInit = True

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
		if self.isInit is False:
			self.initialize()

		events = cave.getEvents()
		scene = cave.getScene()
		if events.active(cave.event.KEY_F):
			print(len(self.pathnode_list))
			
		if events.active(cave.event.MOUSE_LEFT):
			if self.ref_unitmanager is not None:
				self.ref_unitmanager.give_move_order(self.targetNode)
		
	def end(self, scene: cave.Scene):
		pass
	