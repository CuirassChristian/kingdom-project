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

		self.highlighted_unit = None

		if self.ref_pathfindingscript is not None:
			self.ref_pathfindingscript.register_rts_cam(self)

		if self.clickdrag_rect is not None:
			self.clickdrag_rect.scale = cave.UIVector(0,0)
			self.clickdrag_rect.position = cave.UIVector(0,0)

		self.um_obj = scene.get("UnitManager")
		if self.um_obj is not None:
			self.ref_unitmanager = self.um_obj.getPy("UnitManager")
			if self.ref_unitmanager is not None:
				print ("we have unit manager in pathfinding")

	def update(self):
		self.camera_move()
		self.camera_zoom()

		self.check_clicks()
		self.camera_raycast()
		self.draw_clickdrag()

	def check_clicks(self):
		events = cave.getEvents()

		if events.active(cave.event.MOUSE_LEFT):
			if self.highlighted_unit is not None:
				self.ref_unitmanager.select_unit(self.highlighted_unit)


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
		mask.enable(8)
		result = scene.rayCast(origin, ray_target, mask)
		scene.addDebugLine(origin, ray_target, cave.Vector3(0,0,0))
	
		if result.hit:

			# checking for tiles
			pn : PathNode = None
			pn = result.entity.getPy("PathNode")

			world_position = result.entity.getTransform().worldPosition
			point_position = result.position

			tf = self.mouse_world_pos_obj.getTransform()
			tf.position = world_position

			if self.ref_pathfindingscript is not None:
				newx : int = 0
				newy : int = 0
				props = result.entity.getProperties()
		
				newx = props.get("x")
				newy = props.get("y")

				#print(str(newx) + " " + str(newy))
				self.ref_pathfindingscript.set_target_pathnode(cave.Vector2(newx, newy))
			
			self.coordText.setText("pathnode: " + str(round(newx, 2))
			+ ", " + str(round(newy, 2)))

			#checking for units
			un : Unit = None
			un = result.entity.getPy("Unit")

			if un is not None:
				print("we found a unit")
				self.highlighted_unit = un
				self.ref_unitmanager.highlight_unit(un)
			else:
				self.ref_unitmanager.unhighlight()
	
				
	
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
	