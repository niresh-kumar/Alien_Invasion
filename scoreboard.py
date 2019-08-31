import pygame.font
import pygame
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	""" A class to report scoring information """
	
	def __init__(self, ai_settings, screen, stats):
		""" Initialize score keeping attributes """
		
		self.screen = screen
		self.ai_settings = ai_settings
		self.stats = stats
		self.screen_rect = screen.get_rect()
		
		#Font settings for scoring information
		self.text_color = (255, 0, 0)
		self.font = pygame.font.SysFont(None, 48)
		
		# Prep initial score image
		self.prep_score()
		#Prepare high score image
		self.prep_high_score()
		#prepare level image
		self.prep_level()
		
		#prepare ship lives
		self.prep_ships()
		
	def prep_score(self):
		""" Turn the score into rendered image """
		rounded_score = int(round(self.stats.score, -1))
		score_str = "Score:" + "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, 
			self.text_color, self.ai_settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def prep_high_score(self):
		""" Turn high score into rendered image """
		rounded_high_score = int(round(self.stats.high_score, -1))
		high_score_str = "HighScore:" + "{:,}".format(rounded_high_score)
		self.high_score_image = self.font.render(high_score_str, True, 
			self.text_color, self.ai_settings.bg_color)
		# Center high score on the top of screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top
		
	def prep_level(self):
		""" Turn level into renderd image """
		level_str = "level:" + str(self.stats.level)
		self.level_image = self.font.render(level_str, True, 
			self.text_color, self.ai_settings.bg_color)
		#position level below score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	def prep_ships(self):
		""" Show how many ships are left """
		self.ships = Group()
		for ship_number in range(self.stats.ships_left +1 ):
			ship = Ship(self.ai_settings, self.screen)
			ship.image = pygame.transform.scale(ship.image,(30,30))
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	def show_score(self):
		""" Draw the score on screen """
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
