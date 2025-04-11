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

	def give_move_order(self, end:cave.Vector2, eP):
		print ("giving move order")
		for x in self.selected_unit_list:
	
			if x is not None:
				props = x.entity.getProperties()
				newx = props.get("x")
				newy = props.get("y")
				#x.moveTo(pos)
				# in the first version
				# we actually moved to a physical vec3
				# we will use a generic a* grid instead
				path = self.ref_pathfindingscript.find_path(cave.Vector2(newx,newy), end, eP)
				if path is not None:
					print ("unit manager has a path")
					x.moveTo(path)
					
					for n in path:
						#print (n)
						pass

	def start(self, scene: cave.Scene):
		self.ref_pathfindingscript = scene.get("Pathfinding").getPy("Pathfinder")
		pass

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	