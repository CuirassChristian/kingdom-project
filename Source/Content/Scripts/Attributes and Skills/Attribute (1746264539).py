import cave

class Attribute():
	atr_name : str = "Attribute"
	base_value : int = 1
	scale_per_level : float = 0.1
	modified_value : int = 1

	def __init__(self, name : str, base, scale):
		self.atr_name = name
		self.base_value = base
		self.scale_per_level = scale
		self.modified_value = self.base_value

	def get_scaled_value (self, level):
		scaled_value = self.base_value + (self.scale_per_level * level)
		#print(self.atr_name + " scaled value is " + str(scaled_value))
		self.modified_value = scaled_value
		return scaled_value
		
	def start(self, scene: cave.Scene):
		pass
		
	def end(self, scene: cave.Scene):
		pass
	