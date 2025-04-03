import cave
import cave.math

class RTSCamera(cave.Component):
	
	cameraSpeed = 0.2
	cameraZoomSpeed = 0.35
		
	def start(self, scene: cave.Scene):
		self.tf = None 
		self.tf = self.entity.getTransform()
			
	def update(self):
		hasControl = self.entity.properties.get("hasControl", False)
		self.camera_move()
		self.camera_zoom()
		self.camera_raycast()
		
	def camera_zoom(self):
		events = cave.getEvents()
		sens : float = 0.25
		y = events.getMouseScroll() * sens
		dir = cave.Vector3(0, y, 0)
		cam_move = -dir * self.cameraZoomSpeed
	
		if self.tf is not None:
			if y > 0:
				if self.tf.position.y > 1:
					self.tf.position += cam_move
			if y < 0:
				if self.tf.position.y < 5:
					self.tf.position += cam_move
		
	def camera_raycast(self):
		events = cave.getEvents()
		scene = cave.getScene()
		window = cave.getWindow()
		cam = scene.getCamera()
		origin = cam.getWorldPosition()
		mask = cave.BitMask(False)
		mask.enable(7)
		
		# get mouse pos for cam raycast
		mouse_pos = window.getMousePosition(False)
		target = origin + cam.getForwardVector(True) * -1000
	
		result = scene.rayCast(origin, target, mask)
		scene.addDebugLine(origin, target, cave.Vector3(0,0,64))
		
		if result.hit:
			print(result.hit)
		pass
		
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
	