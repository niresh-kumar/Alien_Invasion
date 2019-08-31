import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" Class to manage bullets fired from ship """
	
	def __init__(self, ai_settings, screen, ship):
		""" Create bullet object at ships current position """
		super(Bullet, self).__init__()  # python2.7 way of initializing 
										# super class
		self.screen = screen
		
		#Create a bullet at (0,0) and change to correct position
		self.rect = pygame.Rect( 0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# Store bullet's position as a decimal value
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed = ai_settings.bullet_speed
		
	def update(self):
		""" Move bullet up the screen """
		# update the decimal position of the bullet
		self.y -= self.speed
		# update the rect position
		self.rect.y = self.y
		
	def draw_bullets(self):
		""" Draw the bullet on the screen """
		pygame.draw.rect(self.screen, self.color, self.rect)
		
		
			
