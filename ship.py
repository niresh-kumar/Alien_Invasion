import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings, screen):
		"""initialize the ship and set it's starting position"""
		super(Ship,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Load ship and get its rect
		self.image = pygame.image.load('images/spaceship.bmp')
		self.image = pygame.transform.scale(self.image, (50,50))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new ship at the bottom of the center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# Store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
		# Movement Flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		# Move ship left or right according to flag
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed
		if self.moving_left and self.rect.left > 0:		# Using if instead of elif
			self.center -= self.ai_settings.ship_speed	
									# because elif gives preference to
									# to right if both keys are held
		# update rect object from self.center
		self.rect.centerx = self.center
	def blitme(self):
		""" Draw the ship at its current location """
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		self.center = self.screen_rect.centerx
