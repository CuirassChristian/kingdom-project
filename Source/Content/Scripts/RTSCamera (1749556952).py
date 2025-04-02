import cave

class RTSCamera(cave.Component):
	
	cameraSpeed = 0.2
		
	def start(self, scene: cave.Scene):
		self.tf = None 
		self.tf = self.entity.getTransform()
			
	def update(self):
		hasControl = self.entity.properties.get("hasControl", False)
		self.camera_move()
		self.camera_zoom()
		
	def camera_zoom(self):
		events = cave.getEvents()
		#y = events.active(cave.event.getMouseScroll())
		#print (y)
		
	#region camera controls
	def camera_move(self):
		events = cave.getEvents()
		x = events.active(cave.event.KEY_A) - events.active(cave.event.KEY_D)
		z = events.active(cave.event.KEY_W) - events.active(cave.event.KEY_S)
		dir = cave.Vector3(x, 0.0, z)

		cam_move = -dir * self.cameraSpeed
		
		isMoving = dir.length() > 0.0
		if isMoving:
			dir.normalize()
			
		if self.tf is not None:
			self.tf.position += cam_move
	#endregion
	
	def end(self, scene: cave.Scene):
		pass
	