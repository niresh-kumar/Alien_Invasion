import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A Class to represent a single alien in the fleet """
	
	def __init__(self, ai_settings, screen):
		""" Initialize the alien and set its starting position """
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Load the alien image and set its rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		
		#Start the alien near the top left corner of screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# Store the aliens exact position
		self.x = float(self.rect.x)
	
	def check_edges(self):
		""" Return true if alien hits either edge """
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		
	def update(self):
		""" Move the alien left or right """
		self.x += (self.ai_settings.alien_speed * 
			self.ai_settings.fleet_direction)
		self.rect.x = self.x
		
	def blitme(self):
		""" Draw the alien at the current position """
		self.screen.blit(self.image, self.rect)
