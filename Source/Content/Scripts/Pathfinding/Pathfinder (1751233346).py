import cave

class Pathfinder(cave.Component):

	gridSizeX : int = 0
	gridSizeY : int = 0
	gridSpacing : float = 0.1
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
		self.target = cave.Vector2(0,0)
		self.pathnode_list = []
		self.generateGrid()

		#actual pathfinding stuff
		self.g = 0
		self.h = 0
		self.f = 0

		
	def set_target_pathnode(self, p):
		self.targetNode = p
		self.target = (p.x, p.y)
		
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

	def find_path(self, s:cave.Vector2, e:cave.Vector2):
		self.a_star(self.pathnode_list, s, e)


	def a_star(self, nodelist, start, end):
		print ("finding path: " + str(start) + " -> " + str(end))
		pass

	def generateGrid(self):
	
		for x in range(self.gridSizeX):
			for y in range(self.gridSizeY):
				self.createNode(x, y)
				
	def createNode(self, x, y):
		scene = cave.getScene()
		newNode = self.entity.getScene().addFromTemplate("PathNode")
		newNode.activate(scene)

		tf = newNode.getTransform()
		tf.setParent(self.entity.getTransform(), True)
		tf.scale = cave.Vector3(0.1, 0.1, 0.1)
		
		spacing_factor = 0.25
		pos = cave.Vector3(x * spacing_factor, 0.05, y * spacing_factor)  

		pn = PathNode()
		
		if pn is not None:
			self.register_pathnode(pn)
			pn.setEntity(newNode)

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
				self.ref_unitmanager.give_move_order(self.target)
		
	def end(self, scene: cave.Scene):
		pass
	