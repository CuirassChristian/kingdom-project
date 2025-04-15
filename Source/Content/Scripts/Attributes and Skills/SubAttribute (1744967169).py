import cave

class SubAttribute(cave.Component):
	atr_name : str = "SubAttribute"
	base_value : int = 1
	cur_value : int = 1
	modifying_attributes = []
	modified_value : int = 1
	
	def __init__(self, name : str, base):
		cave.Component.__init__(self)
		self.atr_name = name
		self.base_value = base
		self.cur_value = self.base_value
		self.modified_value = self.base_value

	def set_attributepair (self, atr, value):
		attributePair = AttributePair(atr, value)
		self.modifying_attributes.append(attributePair)
		#print (self.atr_name + " has created attribute pair for (" + attributePair.attribute.atr_name + " ) it scales " + str(value))

	def get_subattribute_value(self):
		value = self.base_value

		for m in self.modifying_attributes:
			#print(f"Modifying {self.atr_name} with {m.attribute.atr_name} value: {m.attribute.modified_value}, scaling: {m.value}")
			value += m.attribute.modified_value * m.value

		return value
		
	def start(self, scene: cave.Scene):
		pass
		
	def end(self, scene: cave.Scene):
		pass

	