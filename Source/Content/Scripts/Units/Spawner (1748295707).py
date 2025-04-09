import cave

class Spawner(cave.Component):

	defaultSpawnPos = None
	active_comm_player = None

	def start(self, scene: cave.Scene):
		self.defaultSpawnPos = self.entity.getChild("DefaultSpawnPos")
		self.spawnTransform = self.defaultSpawnPos.getTransform()
		pass
		
	def spawnHeroPlayer(self):
		ent = self.entity.getScene().addFromTemplate("HeroPlayer", self.spawnTransform.worldPosition)
		print ("spawning hero player")

	def spawnUnit(self):
		ent = self.entity.getScene().addFromTemplate("Unit", self.spawnTransform.worldPosition)
		print ("spawning unit")

	def spawnBoss (self):
		print ("spawning boss")
		if self.active_comm_player is not None:
			self.active_comm_player.kill()

		self.active_comm_player = self.entity.getScene().addFromTemplate("CommanderPlayer", self.spawnTransform.worldPosition)

	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	