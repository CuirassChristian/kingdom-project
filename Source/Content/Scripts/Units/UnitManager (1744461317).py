import cave

class UnitManager(cave.Component):

	unit_list : []
	selected_unit_list : []
	hovered_unit_list : []

	def __init__(self):
		cave.Component.__init__(self)
		self.unit_list = []
		self.selected_unit_list = []
		print ("Unit Manager Initialized")

	def add_unit(self, u):
		print ("Adding unit")
		self.unit_list.append(u)
		self.select_unit(u)

	def select_unit(self, u):
		print ("selecting unit")
		self.selected_unit_list.append(u)

	def remove_unit(self, u):
		print ("Removing Unit")
		self.unit_list.remove(u)

	def give_move_order(self, end:cave.Vector2):
		print ("giving move order")
		for x in self.selected_unit_list:
	
			if x is not None:
				#x.moveTo(pos)
				# in the first version
				# we actually moved to a physical vec3
				# we will use a generic a* grid instead
				self.ref_pathfindingscript.find_path(cave.Vector2(x.cur_x, x.cur_y), end)

	def start(self, scene: cave.Scene):
		self.ref_pathfindingscript = scene.get("Pathfinding").getPy("Pathfinder")
		pass

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	