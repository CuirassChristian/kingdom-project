import cave
import math

class Unit(cave.Component):
	
	name = ""
	moveSpeed : float = 2

	targetPos : cave.Vector3 = None
	unitManager = None
	ref_unitManager = None
	tf : cave.Transform = None
	target_tf : cave.Transform = None
	cur_tf : cave.Transform = None
	cur_pos : cave.Vector3 = None
	hasMoveOrder : bool = False
	unit_collision = None
	next_node = None
	node_path_count : int = 0
	pathlist = []
	idle_pathnode = None

	unit_walk_range = 5
	
	def __init__(self):
		cave.Component.__init__(self)
		pass
	
	def start(self, scene: cave.Scene):
		self.targetPos : cave.Vector3 = None
		self.hasMoveOrder = False
		self.distance_speed : Float = 0
		self.next_node = None
		self.node_path_count : int = 0

		self.hlt_graphic = self.entity.getChild("highlight", True)
		self.sel_graphic = self.entity.getChild("select", True)
		self.toggle_highlight(False)
		self.toggle_select(False)

		self.unit_walk_range = 5

		self.pathlist = []
		self.idle_pathnode = None
		self.unit_collision = self.entity.get("RigidBodyComponent")
		if self.unit_collision is not None:
			print("we have collision")

		# intializing transform for movement later
		self.target_tf = cave.Transform()
		self.cur_tf = cave.Transform()

		self.cur_x = 0
		self.cur_y = 0

		self.pathlist = None

		self.moveSpeed = 5
		self.unitManager = scene.get("UnitManager")
		self.tf = self.entity.getTransform()
		self.cur_pos : cave.Vector3 = self.tf.position

		if self.unitManager is not None:
			self.ref_unitManager = self.unitManager.getPy("UnitManager")
			self.ref_unitManager.add_unit(self)

		#self.ref_unitManager.get_nearby_tiles(cave.Vector2(x,y), self.unit_walk_range)
			

	def toggle_highlight (self, active : bool):
		self.hlt_graphic.setActive(active, cave.getScene())
		pass

	def toggle_select (self, active : bool):
		self.sel_graphic.setActive(active, cave.getScene())
		pass

	def moveTo(self, pathlist):

		self.node_path_count = 0
		self.pathlist = pathlist
		
		if len(self.pathlist) == 0:
			print("no path to follow")
			return

		if len(self.pathlist) == 1:
			print("path too short")
			return
			
		firstnode = pathlist[0]
		self.next_node = pathlist[1]

		self.ref_unitManager.on_move_finished(self)

		for p in pathlist:
			p.getPy("PathNode").highlight_path()

		if firstnode is not None:
			print("we have the first node")
			
			# Mark the first node as occupied
			firstnode.getProperties()["occupied"] = True
			
			pn = firstnode.getPy("PathNode")
			
			if pn is not None:
				print("we have the py")
				if self.next_node is not None:
					self.targetPos = self.next_node.getTransform().position
					self.cur_pos = firstnode.getTransform().position

					self.move()
		
		pass

	def node_reached(self):
		self.idle_pathnode = self.pathlist[self.node_path_count]
		self.idle_pathnode.getPy("PathNode").highlight()
		# Mark the node as unoccupied when reached
		self.idle_pathnode.getProperties()["occupied"] = False
	
	
		self.entity.getProperties()["x"] = self.idle_pathnode.getProperties()["x"]
		self.entity.getProperties()["y"] = self.idle_pathnode.getProperties()["y"]
		self.hasMoveOrder == False

		x = self.entity.getProperties()["x"]
		y = self.entity.getProperties()["y"]

		print("reached goal - next node is " + str(self.node_path_count))

		path_len = len(self.pathlist)
		if self.node_path_count >= path_len - 1:
			print("path is completed")
			self.ref_unitManager.on_move_finished(self)
			return
		else:
	
			if self.node_path_count + 1 > len(self.pathlist) - 1:
				print("no available next nodes")
				self.ref_unitManager.on_move_finished(self)
				return
				
			self.node_path_count += 1
			self.next_node.getPy("PathNode").highlight()

			print("moving to next node")
			if self.pathlist[self.node_path_count]:
				self.next_node = self.pathlist[self.node_path_count]

				self.targetPos = self.next_node.getTransform().position
				self.cur_pos = self.pathlist[self.node_path_count - 1].getTransform().position
			
				self.move()
				self.next_node.getPy("PathNode").highlight()
			else:
				print ("no node")
		
	def move(self):
		base_time_per_unit_distance = 0.05
		distance_to_target = (self.targetPos - self.cur_pos).length()
		desired_time_to_reach = distance_to_target * base_time_per_unit_distance
	
		self.distance_speed = distance_to_target / desired_time_to_reach
		self.distance_speed = min(self.distance_speed, self.moveSpeed)
		self.cur_tf.setPosition(self.cur_pos)
		self.target_tf.setPosition(self.targetPos)
		self.hasMoveOrder = True

	def check_collisions(self):
		collisions = self.unit_collision.getCollisionsWith("Unit")
		pathnode_collisions = self.unit_collision.getCollisionsWith("Pathnode")

		if len(pathnode_collisions) > 0:
			print("pn")
			
		if len(collisions) > 0:
			for x in collisions:
				tf = x.entity.getTransform()
				if tf is not None:
					dist = (self.cur_pos - tf.position).length()
					if dist < 0.15:
						pass

	def do_move(self):
		dt = cave.getDeltaTime()
		speed : float = self.moveSpeed * dt
		self.cur_pos = self.tf.position

		if self.targetPos is not None:
			self.tf.lookAtPositionSmooth(self.targetPos, 0.5, cave.Vector3(0,1,0))
			self.cur_tf.lerp(self.target_tf, (self.distance_speed * dt))

			distance_to_target = (self.targetPos - self.cur_pos).length()

			self.tf.position = self.cur_tf.position
			if distance_to_target < 0.1:
				self.hasMoveOrder = False
				print("move order finished")
				self.node_reached()
			#print (distance)

	def update(self):
		#self.check_collisions()

		if self.hasMoveOrder is True:
			self.do_move()
		
	
		
	def end(self, scene: cave.Scene):
		pass
	