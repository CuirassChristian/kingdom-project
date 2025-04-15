import cave

class RoleData():

	attributes = []

	def __init__(self, name : str, g_str, g_int, g_wis, g_dex, g_agil, g_cons, g_comm):

		self.attributes = []

		self.roleName = name	
		self.base_str = (g_str[0], g_str[1])
		self.base_int = (g_int[0], g_int[1])
		self.base_wis = (g_wis[0], g_wis[1])
		self.base_dex = (g_dex[0], g_dex[1])
		self.base_agi = (g_agil[0], g_agil[1])
		self.base_const = (g_cons[0], g_cons[1])
		self.base_comm = (g_comm[0], g_comm[1])

	def set_attributes(self, atr_list):
		attributes = atr_list

	def start(self, scene: cave.Scene):
		pass

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	