class GameStats():
	""" Keep track of statistics for the game """
	def __init__(self, ai_settings):
		"""Initialize statistics """
		self.ai_settings = ai_settings
		
		# read high score from file
		try:
			with open('high_score.txt') as f_obj:
				self.high_score = int(f_obj.read())
		except:
			self.high_score = 0
			
		self.reset_stats()
		
		# start alien invasion in inactive state
		self.game_active = False
	
	def reset_stats(self):
		""" Initialize statistics that can change during the game """
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
