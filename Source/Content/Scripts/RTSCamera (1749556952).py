import cave
import cave.math

class RTSCamera(cave.Component):
	
	cameraSpeed = 0.2
	cameraZoomSpeed = 0.35
	cam = None
	ref_pathfindingscript = None
	clickdrag_rect = None
	mouse_world_pos_obj = None

	def __init__(self):
		cave.Component.__init__(self)
		
	def start(self, scene: cave.Scene):
		self.tf = None 
		self.tf = self.entity.getTransform()
		self.ref_pathfindingscript = None
		self.clickdrag_rect : cave.UIElementComponent = scene.get("ClickDrag").get("UI Element")
		self.coordText : cave.UIElementComponent = scene.get("PathNodeCoord").get("UI Element")
		self.ref_pathfindingscript = scene.get("Pathfinding").getPy("Pathfinder")
		self.mouse_world_pos_obj = self.entity.getScene().addFromTemplate("WorldMousePosObj")

		if self.ref_pathfindingscript is not None:
			self.ref_pathfindingscript.register_rts_cam(self)

		if self.clickdrag_rect is not None:
			self.clickdrag_rect.scale = cave.UIVector(0,0)
			self.clickdrag_rect.position = cave.UIVector(0,0)

	def update(self):
		self.camera_move()
		self.camera_zoom()
		self.camera_raycast()
		self.draw_clickdrag()

	def draw_clickdrag (self):
		window = cave.getWindow()
		events = cave.getEvents()
		window_size = window.getWindowSize()
		mouse_pos = window.getMousePosition(True)

		self.clickdrag_rect.position = cave.UIVector(mouse_pos.x, -mouse_pos.y)
		self.clickdrag_rect.scale = cave.UIVector(1,1)

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
				if self.tf.position.y < 7:
					self.tf.position += cam_move
		
	def camera_raycast(self):
		events = cave.getEvents()
		scene = cave.getScene()
		window = cave.getWindow()
		cam = scene.getCamera()
		origin = cam.getWorldPosition()
	
		# get mouse pos for cam raycast
		mouse_pos = window.getMousePosition(True)
		target = cam.getScreenRay(mouse_pos.x, mouse_pos.y)
		
		length = 200
		ray_target = target * length

		mask = cave.BitMask(False)
		mask.enable(7)
		result = scene.rayCast(origin, ray_target, mask)
		scene.addDebugLine(origin, ray_target, cave.Vector3(0,0,0))
	
		if result.hit:
			pn : PathNode = None
			pn = result.entity.getPy("PathNode")

			world_position = result.entity.getTransform().worldPosition
			point_position = result.position

			tf = self.mouse_world_pos_obj.getTransform()
			tf.position = world_position

			if self.ref_pathfindingscript is not None:
				print("setting target")
				self.ref_pathfindingscript.set_target_pathnode(world_position)
			
			self.coordText.setText("pathnode: " + str(round(world_position.x, 2))
			+ ", " + str(round(world_position.z, 2)))
	
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
	