""" contains settings """
class Settings():
	""" Class to store all settings of alien_invasion """
	def __init__(self):
		""" Initialize game settings """
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		
		#ship settings
		self.ship_limit = 2
		
		#bullet settings
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (120,120,120)
		self.bullets_allowed = 4
		
		# alien settings
		self.fleet_drop_speed = 10
		
		#how quickly the game speeds up
		self.speedup_scale = 1.5
		self.score_scale = 2
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		""" Initialize settings that change during the game """
		# alien settings
		self.alien_speed = 1
		# bullet settings
		self.bullet_speed = 2
		# fleet direction 1 represents right and fleet direction -1 is 
		#left
		self.fleet_direction = 1
		# ship settings
		self.ship_speed = 1.5
		#Scoring settings
		self.alien_points = 50
	
	def increase_speed(self):
		""" Increase speed settings """
		self.ship_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale 
		self.bullet_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
