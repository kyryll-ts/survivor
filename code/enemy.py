import pygame
from pathlib import Path
import math

BASE_DIR = Path(__file__).resolve().parent
CODE_DIR = BASE_DIR.parent / "code"
animationloader = CODE_DIR.parent / "animationloader.py"
from code.animationloader import load_animation_sets
clock = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()

		
		self.damage = 5
		self.health = 10

		self.enemy_walk = BASE_DIR.parent / "assets" / "enemy.png"

		self.animation_list = load_animation_sets(self.enemy_walk, 32, 32, 5, 4)

		self.action = 0      # Current Row (0, 1, or 2)
		self.frame_index = 0 # Current Column
		self.frames = self.animation_list[self.action] 

		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center=(x, y))
        
		self.speed = 0.5
		self.last_update = pygame.time.get_ticks()
		self.frame_cooldown = 200

		self.detection_radius = 999
		self.slowdownfactor = 0.5

		self.pos_x = x
		self.pos_y = y


	def check_player_collision(self, player_rect):

		if self.rect.colliderect(player_rect):
			self.speed =0
		else:
			self.speed =0.5

	def draw_health_bar(self, surface):
    
		bar_x = self.rect.x
		bar_y = self.rect.y - 10
		bar_width = self.rect.width
		bar_height = 5
    
    
		health_ratio = self.health / 10 # 10 is your max_health
    
    
		pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
    
		pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height))


	def update(self, player_rect):
		new_action = 0

		self.frame_index += 0.1
		if self.frame_index >= len(self.frames):
			self.frame_index = 0

		self.image = self.frames[int(self.frame_index)]

		if self.health <= 0:
			self.kill()
			return

		dx = player_rect.centerx - self.rect.centerx
		dy = player_rect.centery - self.rect.centery
		dist_sq = dx*dx + dy*dy

		if dist_sq < self.detection_radius ** 2:
			dist = math.sqrt(dist_sq)
			if dist != 0:
				dx /= dist
				dy /= dist

		#inversed controls

		self.pos_x += dx * self.speed
		self.pos_y += dy * self.speed

		# Round to the NEAREST integer instead of just truncating
		self.rect.x = round(self.pos_x)
		self.rect.y = round(self.pos_y)
		self.check_player_collision(player_rect)

	def draw(self, surface):
		surface.blit(self.image, self.rect)
		self.draw_health_bar(surface)