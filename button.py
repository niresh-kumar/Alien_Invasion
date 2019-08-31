import pygame.font

class Button():
	""" A Button with words in it """
	def __init__(self, ai_settings, screen, msg):
		""" Initialize button attributes """
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# set dimension and properties of button
		self.width, self.height = 200, 50
		self.button_color = (0, 0, 255)
		self.text_color = (255, 0, 0)
		self.font = pygame.font.SysFont(None, 48)
		
		# Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		# The Button message need to be prepped only once
		self.prep_msg(msg)
	
	def prep_msg(self, msg):
		""" Turn msg into a renderd image and center 
			text on the button """
		self.msg_image = self.font.render(msg, True, self.text_color, 
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		""" Draw the button then the image of text"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		
