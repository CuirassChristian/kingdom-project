import cave

class RoleManager(cave.Component):

	def __init__(self):
		cave.Component.__init__(self)

	def start(self, scene: cave.Scene):

		self.ref_attribute_manager = None
		self.all_roles_list = []

		atr_manager_obj = scene.get("AttributeManager")

		if atr_manager_obj is not None:
			self.ref_attribute_manager = atr_manager_obj.getPy("AttributeManager")
			print("We have attribute object")

		if self.ref_attribute_manager is not None:
			self.generate_roles()

		pass

	def generate_roles(self):
		# value, growth
		# str, int, wis, dex, agi, con, command
		# STRENGTH HYBRIDS
		self.all_roles_list = []

		warrior = RoleData("Warrior", 	(19, 2.2), 		#strength
										(2, 0.1),		#intelligence
										(2, 0.23 ),		#wisdom
										(6, 1.2),		#dexterity
										(5, 1.4),		#agility
										(15, 1.6), 		#constitution
										(0, 0.5))		#command

		marauder = RoleData("Marauder", (21, 2.2), 		#strength
										(2, 0.1),		#intelligence
										(2, 0.23 ),		#wisdom
										(6, 1.2),		#dexterity
										(18, 1.4),		#agility
										(8, 1.6), 		#constitution
										(0, 0.5))		#command

		brawler = RoleData("Brawler", 	(21, 2.2), 		#strength
										(2, 0.1),		#intelligence
										(2, 0.23 ),		#wisdom
										(17, 1.2),		#dexterity
										(5, 1.4),		#agility
										(8, 1.6), 		#constitution
										(0, 0.5))		#command

		paladin = RoleData("Paladin", 	(19, 2.2), 		#strength
										(17, 0.1),		#intelligence
										(8, 0.23 ),	#wisdom
										(2, 1.2),		#dexterity
										(2, 1.4),		#agility
										(11, 1.6), 		#constitution	
										(0, 0.5))		#command	

		cleric = RoleData("Cleric", 	(17, 2.2), 		#strength
										(11, 0.1),		#intelligence
										(22, 0.23 ),	#wisdom
										(2, 1.2),		#dexterity
										(2, 1.4),		#agility
										(9, 1.6), 		#constitution	
										(0, 0.5))		#command

		guardian = RoleData("Guardian", (17, 2.2), 		#strength
										(7, 0.1),		#intelligence
										(8, 0.23 ),		#wisdom
										(2, 1.2),		#dexterity
										(2, 1.4),		#agility
										(13, 1.6), 		#constitution	
										(3, 1))			#command


		# INTELLIGENCE HYBRIDS

		illus = RoleData("Illusionist", (4, 2.2), 		#strength
										(17, 2.1),		#intelligence
										(17, 2.2),		#wisdom
										(4, 1.2),		#dexterity
										(4, 1.4),		#agility
										(6, 1.6),		#constitution
										(1, 0.9))		#command

		magician = RoleData("Magician", (2, 2.2), 		#strength
										(42, 3),		#intelligence
										(9, 0.23),		#wisdom
										(1, 1.2),		#dexterity
										(5, 1.4),		#agility
										(4, 1.6), 		#constitution	
										(0, 0.5))		#command						

		ninja = RoleData("Ninja", 		(4, 2.2), 		#strength
										(21, 0.1),		#intelligence
										(4, 0.23 ),		#wisdom
										(5, 1.2),		#dexterity
										(23, 1.4),		#agility
										(8, 1.6), 		#constitution
										(0, 0.5))		#command	

		shaman = RoleData("Shaman", 	(5, 2.2), 		#strength
										(22, 0.1),		#intelligence
										(8, 0.23 ),		#wisdom
										(21, 1.2),		#dexterity
										(2, 1.4),		#agility
										(9, 1.6), 		#constitution	
										(1, 0.5))		#command	

		tactician = RoleData("Tactician",(7, 2.2), 		#strength
										(22, 0.1),		#intelligence
										(4, 0.23 ),		#wisdom
										(4, 1.2),		#dexterity
										(2, 1.4),		#agility
										(9, 1.6), 		#constitution	
										(3, 1))			#command	

		# AGILITY HYBRIDS

		rogue = RoleData("Rogue",		(4, 2.2), 		#strength
										(5, 0.1),		#intelligence
										(4, 0.23 ),		#wisdom
										(4, 1.2),		#dexterity
										(33, 1.4),		#agility
										(10, 1.6), 		#constitution	
										(0, 1))			#command

		hunter = RoleData("Hunter",		(3, 2.2), 		#strength
										(5, 0.1),		#intelligence
										(7, 0.23 ),		#wisdom
										(24, 1.2),		#dexterity
										(22, 1.4),		#agility
										(6, 1.6), 		#constitution	
										(1, 1))			#command

		assassin = RoleData("Assassin",	(3, 2.2), 		#strength
										(5, 0.1),		#intelligence
										(20, 0.23 ),	#wisdom
										(3, 1.2),		#dexterity
										(27, 1.4),		#agility
										(6, 1.6), 		#constitution	
										(0, 0))			#command		

		bard = RoleData("Bard",			(5, 2.2), 		#strength
										(7, 0.1),		#intelligence
										(20, 0.23 ),	#wisdom
										(1, 1.2),		#dexterity
										(25, 1.4),		#agility
										(7, 1.6), 		#constitution	
										(3, 1))			#command		

		# DEXTERITY HYBRIDS

		ranger = RoleData("Ranger",		(4, 2.2), 		#strength
										(3, 0.1),		#intelligence
										(4, 0.23 ),		#wisdom
										(35, 1.2),		#dexterity
										(9, 1.4),		#agility
										(4, 1.6), 		#constitution	
										(2, 1))			#command	

		druid = RoleData("Druid",		(8, 2.2), 		#strength
										(5, 0.1),		#intelligence
										(27, 0.23 ),	#wisdom
										(21, 1.2),		#dexterity
										(2, 1.4),		#agility
										(2, 1.6), 		#constitution	
										(2, 1))			#command	

		beastmaster = RoleData("Beastmaster",(7, 2.2), 	#strength
										(7, 0.1),		#intelligence
										(7, 0.23 ),		#wisdom
										(25, 1.2),		#dexterity
										(2, 1.4),		#agility
										(4, 1.6), 		#constitution	
										(4, 1.4))		#command

		# COMMAND HYBRIDS

		admiral = RoleData("Admiral",	(9, 2.2), 		#strength
										(2, 0.1),		#intelligence
										(28, 0.23 ),		#wisdom
										(2, 1.2),		#dexterity
										(2, 1.4),		#agility
										(10, 1.6), 		#constitution	
										(5, 0.75))		#command

		general = RoleData("General",	(9, 2.2), 		#strength
										(4, 0.1),		#intelligence
										(7, 0.23 ),		#wisdom
										(3, 1.2),		#dexterity
										(5, 1.4),		#agility
										(8, 1.6), 		#constitution	
										(10, 0.75))		#command


		beastmaster.set_attributes(self.ref_attribute_manager.get_attribute_for_role(beastmaster))
		druid.set_attributes(self.ref_attribute_manager.get_attribute_for_role(druid))
		ranger.set_attributes(self.ref_attribute_manager.get_attribute_for_role(ranger))
		bard.set_attributes(self.ref_attribute_manager.get_attribute_for_role(bard))
		assassin.set_attributes(self.ref_attribute_manager.get_attribute_for_role(assassin))
		hunter.set_attributes(self.ref_attribute_manager.get_attribute_for_role(hunter))
		rogue.set_attributes(self.ref_attribute_manager.get_attribute_for_role(rogue))
		tactician.set_attributes(self.ref_attribute_manager.get_attribute_for_role(tactician))
		shaman.set_attributes(self.ref_attribute_manager.get_attribute_for_role(shaman))
		ninja.set_attributes(self.ref_attribute_manager.get_attribute_for_role(ninja))
		magician.set_attributes(self.ref_attribute_manager.get_attribute_for_role(magician))
		illus.set_attributes(self.ref_attribute_manager.get_attribute_for_role(illus))
		guardian.set_attributes(self.ref_attribute_manager.get_attribute_for_role(guardian))
		cleric.set_attributes(self.ref_attribute_manager.get_attribute_for_role(cleric))
		paladin.set_attributes(self.ref_attribute_manager.get_attribute_for_role(paladin))
		brawler.set_attributes(self.ref_attribute_manager.get_attribute_for_role(brawler))
		warrior.set_attributes(self.ref_attribute_manager.get_attribute_for_role(warrior))
		marauder.set_attributes(self.ref_attribute_manager.get_attribute_for_role(marauder))
		admiral.set_attributes(self.ref_attribute_manager.get_attribute_for_role(admiral))
		general.set_attributes(self.ref_attribute_manager.get_attribute_for_role(general))

		self.all_roles_list.extend([beastmaster, druid,
		ranger, bard, assassin, hunter,
		rogue, tactician, shaman, ninja, magician, illus, guardian,
		cleric, paladin, brawler, warrior, marauder, admiral, general])

		print ("we have generated " + str(len(self.all_roles_list)) + " roles")


	def update(self):
		events = cave.getEvents()
		
	def end(self, scene: cave.Scene):
		pass
	