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

	def __init__(self):
		cave.Component.__init__(self)
		pass
	
	def start(self, scene: cave.Scene):
		self.targetPos : cave.Vector3 = None
		self.hasMoveOrder = False
		self.distance_speed : Float = 0
		self.unit_collision = self.entity.get("RigidBodyComponent")
		if self.unit_collision is not None:
			print("we have collision")

		# intializing transform for movement later
		self.target_tf = cave.Transform()
		self.cur_tf = cave.Transform()

		self.cur_x = 0
		self.cur_y = 0

		self.moveSpeed = 1
		self.unitManager = scene.get("UnitManager")
		self.tf = self.entity.getTransform()
		self.cur_pos : cave.Vector3 = self.tf.position
		if self.unitManager is not None:
			self.ref_unitManager = self.unitManager.getPy("UnitManager")
			self.ref_unitManager.add_unit(self)
			
	def moveTo (self, pos: cave.Vector3):
		print ("received move order to " + str(pos))
		self.cur_pos : cave.Vector3 = self.tf.position
		self.targetPos = pos
		base_time_per_unit_distance = 0.1
		distance_to_target = (self.targetPos - self.cur_pos).length()
		desired_time_to_reach = distance_to_target * base_time_per_unit_distance

		self.distance_speed = distance_to_target / desired_time_to_reach
		self.distance_speed = min(self.distance_speed, self.moveSpeed)
		self.cur_tf.setPosition(self.cur_pos)
		self.target_tf.setPosition(self.targetPos)
		self.hasMoveOrder = True

		pass

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
			if distance_to_target < 0.13:
				self.hasMoveOrder = False
				print("move order finished")
			#print (distance)

	def update(self):
		#self.check_collisions()

		if self.hasMoveOrder is True:
			self.do_move()
		
	
		
	def end(self, scene: cave.Scene):
		pass
	