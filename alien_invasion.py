import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	# Initialize game and create screen element
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("alien invasion")
	
	# Make play button
	play_button = Button(ai_settings, screen, "PLAY")
	# Create an instance to store gamestats
	stats = GameStats(ai_settings)
	# make a ship
	ship = Ship(ai_settings, screen)
	# make a group to store aliens
	aliens = Group()
	# make a group to store bullets
	bullets = Group()
	
	# Initialize scoreboard instance
	sb = Scoreboard(ai_settings, screen, stats)
	
	# create fleet of aliens
	gf.create_fleet(ai_settings, screen, aliens, ship)
	
	# Start the main loop for the game
	while True:
		
		gf.check_events(ai_settings, screen, ship, bullets, play_button,
			stats, aliens, sb)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, ship, bullets, 
				aliens, sb)
			gf.update_aliens(ai_settings, stats, screen, aliens, ship, 
				bullets, sb)
				
		gf.update_screen(ai_settings, screen, ship, bullets, aliens, 
			play_button, stats, sb)
		
		
run_game()
				
				
