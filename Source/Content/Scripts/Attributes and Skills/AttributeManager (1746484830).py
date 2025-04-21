import cave

class AttributeManager(cave.Component):

	basic_attributes = []
	sub_attributes = []

	def __init__(self):
		cave.Component.__init__(self)

	def start(self, scene: cave.Scene):
		self.sub_attributes = []
		self.basic_attributes = []
		self.generate_attributes()
		self.print_attributes()
		pass

	def get_attribute_for_role(self, role_data):
		#print ("Created role attributes: " + role_data.roleName)
		role_attributes = []

		stre = role_data.base_str
		inte = role_data.base_int
		wisd = role_data.base_wis
		dext = role_data.base_dex
		cons = role_data.base_const
		agil = role_data.base_agi
		comm = role_data.base_comm

		for a in self.basic_attributes:
			if a.atr_name == "Strength":
				stre = role_data.base_str
				role_attributes.append(Attribute(a.atr_name, stre[0], stre[1]))
			if a.atr_name == "Intelligence":
				inte = role_data.base_int
				role_attributes.append(Attribute(a.atr_name, inte[0], inte[1]))
			if a.atr_name == "Wisdom":
				wisd = role_data.base_wis
				role_attributes.append(Attribute(a.atr_name, wisd[0], wisd[1]))
			if a.atr_name == "Agility":
				dext = role_data.base_agi
				role_attributes.append(Attribute(a.atr_name, dext[0], dext[1]))
			if a.atr_name == "Dexterity":
				cons = role_data.base_dex
				role_attributes.append(Attribute(a.atr_name, cons[0], cons[1]))
			if a.atr_name == "Constitution":
				agil = role_data.base_const
				role_attributes.append(Attribute(a.atr_name, agil[0], agil[1]))
			if a.atr_name == "Command":
				comm = role_data.base_const
				role_attributes.append(Attribute(a.atr_name, comm[0], comm[1]))

		for r in role_attributes:
			print (r.atr_name + ": " + str(r.base_value) + " Growth: " + str(r.scale_per_level))
		return role_attributes
				

	def generate_attributes (self):
		atr_strength = Attribute("Strength", 1, 1)
		atr_intell = Attribute("Intelligence", 1, 1)
		atr_wisdom = Attribute("Wisdom", 1, 1)
		atr_agility = Attribute("Agility", 1, 1)
		atr_dex = Attribute("Dexterity", 1, 1)
		atr_const = Attribute("Constitution", 1, 1)
		atr_resource = Attribute("Resourcefulness", 1, 1)
		atr_perce = Attribute("Perception", 1,1)
		atr_command = Attribute("Command", 1,1)

		self.basic_attributes.append(atr_strength)
		self.basic_attributes.append(atr_intell)
		self.basic_attributes.append(atr_wisdom)
		self.basic_attributes.append(atr_agility)
		self.basic_attributes.append(atr_dex)
		self.basic_attributes.append(atr_const)
		self.basic_attributes.append(atr_resource)
		self.basic_attributes.append(atr_perce)
		self.basic_attributes.append(atr_command)

		# now we define sub attributes and their modifying values

		subatr_physatk = SubAttribute("Physical Attack", 1)
	
		subatr_physatk.set_attributepair(atr_strength, 25)
		subatr_physatk.set_attributepair(atr_agility, 1.9)
		subatr_physatk.set_attributepair(atr_resource, 0.5)

		subatr_magiatk = SubAttribute("Magical Attack", 1)

		subatr_magiatk.set_attributepair(atr_intell, 51)
		subatr_magiatk.set_attributepair(atr_wisdom, 1.9)
		subatr_magiatk.set_attributepair(atr_resource, 0.5)

		subatr_sight = SubAttribute("Vision", 1)
		subatr_sight.set_attributepair(atr_perce, 2.6)
		subatr_sight.set_attributepair(atr_wisdom, 1.3)
		subatr_sight.set_attributepair(atr_dex, 0.8)

		self.sub_attributes.append(subatr_sight)
		self.sub_attributes.append(subatr_physatk)
		self.sub_attributes.append(subatr_magiatk)

	def print_attributes(self):
		pass

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	