import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_high_score(stats, sb):
	""" Check for new high score """
	if stats.high_score < stats.score:
		stats.high_score = stats.score
		sb.prep_high_score()
	
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
	""" Respond to ship being hit by alien """
	if stats.ships_left > 0:
		# Decrement ships left
		stats.ships_left -= 1
		
		# update score board
		sb.prep_ships()
		# empty the bullets and aliens
		bullets.empty()
		aliens.empty()
	
		#Create new fleet and center the ship
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()
	
		# pause
		sleep(0.5)
	
	else:
		pygame.mouse.set_visible(True)
		stats.game_active = False

def alien_hit_bottom(ai_settings, stats, screen, ship, aliens, bullets, 
	sb):
	""" respond if a alien hits the bottom """
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Treat same as ship getting hit
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets, 
				sb)
			break
			

def check_fleet_edges(ai_settings, aliens):
	""" respond appropriately if a alien has reached an edge """
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	""" Drop the entire fleet and change direction """
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
		

def get_number_alien_x(ai_settings, alien_width):
	""" Determine number of aliens that fit in a row """
	available_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x
	
def get_number_rows(ai_settings, ship_height, alien_height):
	""" Determine the number of rows that can fit"""
	available_space_y = (ai_settings.screen_height - 3 * alien_height
		- ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""Create a alien and place them in a row"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + (2 * alien.rect.height 
		* row_number)
	aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
	""" Create a full fleet of aliens """
	# create an alien 
	# Spacing between two aliens equal to one alien width
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, 
		alien.rect.height)
	
	#create the fleet of aliens
	for row_number in range(number_rows):
		
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, 
				row_number)
	
def fire_bullet(event, ai_settings, screen, ship, bullets):
	""" Fire a bullet when limit not reached """
	if len(bullets) < ai_settings.bullets_allowed:
		# create new bullet and add it to group
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
		
def check_keydown_event(event, ai_settings, screen, ship, bullets, stats):
	""" respond to keypress """
	if event.key == pygame.K_RIGHT:
		# move ship to right
		ship.moving_right = True
		
	elif event.key == pygame.K_LEFT:
		#move ship to left
		ship.moving_left = True
	
	elif event.key == pygame.K_SPACE:
		fire_bullet(event, ai_settings, screen, ship, bullets)
	
	elif event.key == pygame.K_q:
		# write high score to file 
		with open('high_score.txt', 'w') as f_obj:
			f_obj.write(str(stats.high_score))
			
		sys.exit()
		

def check_keyup_event(event, ship):
	""" respond to keyrelease """
	if event.key == pygame.K_RIGHT:
		#stop moving ship to right
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		#stop moving ship to left
		ship.moving_left = False
		
def check_play_button(ai_settings, screen, stats, play_button, ship, 
	aliens, bullets, mouse_x, mouse_y, sb):
	""" Start new game when player press play """
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		# reset dynamic settings
		ai_settings.initialize_dynamic_settings()
		# hide mouse cursor
		pygame.mouse.set_visible(False)
		# reset the game statistics
		stats.reset_stats()
		stats.game_active = True
		
		# reset scoreboard images
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()
		#empty bullets and aliens
		bullets.empty()
		aliens.empty()
		
		#redraw the fleet and center ship
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()
		
		
def check_events(ai_settings, screen, ship, bullets, play_button, stats, 
	aliens, sb):
	""" Respond to keypress, keyrelease and mouse events """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,ai_settings, screen, ship, bullets, 
				stats)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(ai_settings, screen, stats, 
					play_button, ship, aliens, bullets, mouse_x, 
					mouse_y, sb)
			
def update_screen(ai_settings, screen, ship, bullets, aliens, 
	play_button, stats, sb):
	""" update image on the screen and flip to new screen """
	
	
	# redraw the screen during each pass of loop
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	# redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullets()
	
	#Draw Score information
	sb.show_score()
	# Draw play button if game is inactive
	if not stats.game_active: # We draw it last so it is above other 
		play_button.draw_button() #elemetns
		
	# make the most recently drawn screen visible
	pygame.display.flip()

def check_bullet_alien_collisions(ai_settings, screen, stats, aliens, 
	ship, bullets, sb):
		""" Check for collision of bullet and alien and remove them """
		# check if any bullet has hit a alien and delete them.
		collisions = pygame.sprite.groupcollide(bullets, aliens, True, 
			True)
		
		# update score
		if collisions:
			for aliens in collisions.values():
				
				stats.score += ai_settings.alien_points *len (aliens)
				sb.prep_score()
			check_high_score(stats, sb)
			 
		#check if all aliens are destroyed and create new fleet
		if len(aliens) == 0:
			# Destroy all bullets and create new fleet and increase speed
			bullets.empty()
			# increase level
			ai_settings.increase_speed()
			stats.level += 1
			sb.prep_level()
			create_fleet(ai_settings, screen, aliens, ship)

def update_bullets(ai_settings, screen, stats, ship, bullets, aliens, sb):
	""" update position of bullet and get rid of old bullets """
	# update bullet position
	bullets.update()
	
	#Remove old bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
	check_bullet_alien_collisions(ai_settings, screen, stats, aliens, 
		ship, bullets, sb)
	
def update_aliens(ai_settings, stats, screen, aliens, ship, bullets, sb):
	""" update the position of the aliens"""
	check_fleet_edges(ai_settings, aliens)
	#update alien position
	aliens.update()
	
	#Check if alien has collided with ship
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
		
	#check if alien has hit bottom
	alien_hit_bottom(ai_settings, stats, screen, ship, aliens, bullets, 
		sb)
