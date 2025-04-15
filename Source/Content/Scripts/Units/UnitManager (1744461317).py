import cave

class UnitManager(cave.Component):

	unit_list : []
	selected_unit_list : []
	hovered_unit_list : [] = []

	def __init__(self):
		cave.Component.__init__(self)
		self.unit_list = []
		self.selected_unit_list = []
		print ("Unit Manager Initialized")

	def add_unit(self, u):
		print ("Adding unit")
		if u not in self.unit_list:
			self.unit_list.append(u)

	def select_unit(self, u):
		print ("selecting unit")
		if u not in self.selected_unit_list:
			self.selected_unit_list.append(u)
			self.get_nearby_tiles(u.entity, 5)

	def unselect_units(self):
		self.selected_unit_list = []

	def remove_unit(self, u):
		print ("Removing Unit")
		self.unit_list.remove(u)

	def get_nearby_tiles(self, s, range):
		print ("finding nearby tiles in range")
		newx = s.getProperties()["x"]
		newy = s.getProperties()["y"]
		self.ref_pathfindingscript.find_neighbours_in_range(cave.Vector2(newx,newy), range)

	def give_move_order(self, end:cave.Vector2, eP):
		print ("giving move order")
		for x in self.selected_unit_list:
	
			if x is not None:
				props = x.entity.getProperties()
				newx = props.get("x")
				newy = props.get("y")

				if newx == end.x:
					if newy == end.y:
						# catch order to same tile to fix bugs
						print ("cannot send move order to tile we're already on")
						return

				path = self.ref_pathfindingscript.find_path(cave.Vector2(newx,newy), end, eP)
				if path is not None:
					print ("unit manager has a path")
					x.moveTo(path)
					self.waiting_for_move = True
					for n in path:
						#print (n)
						pass
				else:
					print("The path is null")
					self.select_unit(x)

		
		self.selected_unit_list = []
	
	def highlight_unit(self, unit):
		if unit not in self.hovered_unit_list:
			self.hovered_unit_list.append(unit)

		for u in self.hovered_unit_list:
			u.toggle_highlight(True)

	def shortcut_select(self, unit):
		self.hovered_unit_list = []
		self.selected_unit_list = []
		self.highlight_unit = None
		self.ref_pathfindingscript.reset_all_nodes()

		self.select_unit(unit)

	def unhighlight(self):
		for u in self.hovered_unit_list:
			u.toggle_highlight(False)

		self.hovered_unit_list = []

	def start(self, scene: cave.Scene):
		self.ref_pathfindingscript = scene.get("Pathfinding").getPy("Pathfinder")
		self.hovered_unit_list = []
		self.all_units = []
		self.unit_list = []
		self.last_moved_unit = None
		self.waiting_for_move : bool = False
		pass

	def on_move_finished(self, unit):
		print("Unit Manager: Unit finished moving - " + str(unit))
		self.last_moved_unit = unit
		self.waiting_for_move = False

		if self.last_moved_unit is not None:
			self.select_unit(self.last_moved_unit)

	def update(self):
		events = cave.getEvents()
		scene = cave.getScene()
		if events.active(cave.event.KEY_F):
			print(len(self.pathnode_list))
	

		if events.pressed(cave.event.MOUSE_LEFT):
			if self.waiting_for_move is True:
				print("We are still waiting for a move")
				return

			if self.ref_pathfindingscript.target is None:
				print("No target for move order")
				return

			target = self.ref_pathfindingscript.target

			if len(self.selected_unit_list) > 0:
				self.give_move_order(target,target)
			else:
				target = None
				print("Unit Manager: No Units Selected to move!" )

		self.unit_shortcuts(events)

	
	def unit_shortcuts(self, events):
		if self.waiting_for_move is True:
			return

		if events.pressed(cave.event.KEY_1):
			if self.unit_list[0] is not None:
				self.shortcut_select(self.unit_list[0])

		if events.pressed(cave.event.KEY_2):
			if self.unit_list[1] is not None:
				self.shortcut_select(self.unit_list[1])

		if events.pressed(cave.event.KEY_3):
			if self.unit_list[2] is not None:
				self.shortcut_select(self.unit_list[2])

		if events.pressed(cave.event.KEY_4):
			if self.unit_list[3] is not None:
				self.shortcut_select(self.unit_list[3])

		if events.pressed(cave.event.KEY_5):
			if self.unit_list[4] is not None:
				self.shortcut_select(self.unit_list[4])

		if events.pressed(cave.event.KEY_6):
			if self.unit_list[5] is not None:
				self.shortcut_select(self.unit_list[5])

		if events.pressed(cave.event.KEY_7):
			if self.unit_list[6] is not None:
				self.shortcut_select(self.unit_list[6])

		if events.pressed(cave.event.KEY_8):
			if self.unit_list[7] is not None:
				self.shortcut_select(self.unit_list[7])
		
	def end(self, scene: cave.Scene):
		pass
	