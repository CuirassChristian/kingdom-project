import cave
import math
import random

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
		self.target = cave.Vector2(p.x, p.y)
		
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

	def find_path(self, s, e: cave.Vector2, eP):
		startnode = None
		endnode = None
		path = None
		available_pathnode_list = []
		scene = cave.getScene()

		# use dictionary for faster lookup
		pathnode_dict = {}

		for p in self.pathnode_list:
			props = p.getProperties()
			# checking occupancy
			obstacle = props.get("obstacle")
			occupied = props.get("occupied", False)  
			
			if not obstacle and not occupied: 
				available_pathnode_list.append(p)
				nX = props.get("x")
				nY = props.get("y")
				pathnode_dict[(nX, nY)] = p 

		startnode = pathnode_dict.get((s.x, s.y))
		endnode = pathnode_dict.get((e.x, e.y))

		if startnode is not None and endnode is not None:
			path = self.a_star(available_pathnode_list, startnode, endnode, eP)

		if path is not None:
			completed_path = []
			for pa in path:
				completed_node = pathnode_dict.get((pa[0], pa[1]))
				if completed_node:
					completed_path.append(completed_node)

			return completed_path

		return None

	def heuristic(self, node_a, node_b):
		x1 = node_a.getProperties()["x"]
		y1 = node_a.getProperties()["y"]
		x2 = node_b.getProperties()["x"]
		y2 = node_b.getProperties()["y"]

		return abs(x1 - x2) + abs(y1 - y2)

	def a_star(self, nodelist, start, end, endNode):
		props = start.getProperties()
		nX = props.get("x")
		nY = props.get("y")

		props = end.getProperties()
		eX = props.get("x")
		eY = props.get("y")
		start_str = (str(nX) + " " + str(nY))
		end_str = (str(eX) + " " + str(eY))
		#print("finding path: " + start_str + " -> " + end_str)

		openlist = []
		closedlist = []

		openlist.append(start)
		for node in nodelist:
			node.getProperties()["g"] = float('inf') 
			node.getProperties()["h"] = 0
			node.getProperties()["f"] = float('inf')
			node.getProperties()["parent"] = None  

		start.getProperties()["g"] = 0
		start.getProperties()["f"] = self.heuristic(start, end)

		while openlist:
			current_node = min(openlist, key=lambda node: node.getProperties()["f"])

			if current_node == end:
				path = []
				while current_node:
					path.append((current_node.getProperties()["x"], current_node.getProperties()["y"]))
					current_node = current_node.getProperties().get("parent")
				#print(f"Constructed Path: {path}")
				return path[::-1]  # Return reversed path

			openlist.remove(current_node)
			closedlist.append(current_node)

			neighbors = self.get_neighbors(current_node, nodelist)

			for neighbor in neighbors:
				if neighbor in closedlist:
					continue  # Ignore already evaluated neighbors

				# Calculate g, h, and f for the neighbor
				neighbor_g = current_node.getProperties()["g"] + 1
				neighbor_h = self.heuristic(neighbor, end)
				neighbor_f = neighbor_g + neighbor_h

				if neighbor in openlist:
					if neighbor_g < neighbor.getProperties()["g"]:
						neighbor.getProperties()["g"] = neighbor_g
						neighbor.getProperties()["f"] = neighbor_f
						neighbor.getProperties()["parent"] = current_node
				else:
					neighbor.getProperties()["g"] = neighbor_g
					neighbor.getProperties()["h"] = neighbor_h
					neighbor.getProperties()["f"] = neighbor_f
					neighbor.getProperties()["parent"] = current_node 
					openlist.append(neighbor)

		return []

	def get_neighbors(self, current_node, nodelist):
		neighbors = []
		x, y = current_node.getProperties()["x"], current_node.getProperties()["y"]
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), 
					(-1, -1), (-1, 1), (1, -1), (1, 1)]:
			neighbor_pos = (x + dx, y + dy)

			neighbor_node = next((node for node in nodelist if (node.getProperties()["x"], node.getProperties()["y"]) == neighbor_pos), None)
			if neighbor_node:
				neighbors.append(neighbor_node)

		#print(f"Current Node: {x}, {y}, Neighbors Found: {len(neighbors)}")
		return neighbors


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

		props = newNode.getProperties()
		props["x"] = x
		props["y"] = y
		rand = random.random()

		if rand > 0.9:
			props["obstacle"] = True
			newNode.setActive(False, scene)

		self.register_pathnode(newNode)
		
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
				self.ref_unitmanager.give_move_order(self.target, self.target)
		
	def end(self, scene: cave.Scene):
		pass
	