import pygame
from pathlib import Path


pygame.init()

BASE_DIR = Path(__file__).resolve().parent
CODE_DIR = BASE_DIR.parent / "code"
animationloader = CODE_DIR.parent / "animationloader.py"
from code.animationloader import load_animation_sets

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.dx =0
        self.dy =0

        self.health = 100
        self.walkspeed = 2

        #self.player_path = BASE_DIR.parent / "assets" / "player.png"
        self.player_walk = BASE_DIR.parent / "assets" / "player_walk.png"

        self.animation_list = load_animation_sets(self.player_walk, 32, 32, 5, 4)

        self.action = 0      # Current Row (0, 1, or 2)
        self.frame_index = 0 # Current Column
        self.frames = self.animation_list[self.action] 

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))
        
        self.speed = 5
        self.last_update = pygame.time.get_ticks()
        self.frame_cooldown = 100




        #if not self.player_path.exists():
            #raise FileNotFoundError(f"Missing image: {self.player_path}")

        #self.image = pygame.image.load(self.player_path).convert_alpha()
        #self.rect = self.image.get_rect(center=(x, y))



    def input_update(self):
        keys = pygame.key.get_pressed()
        new_action = 0
        self.dx =0
        self.dy =0

        if keys[pygame.K_LEFT]:
            self.dx -= self.walkspeed
            new_action = 2
        elif keys[pygame.K_RIGHT]:
            self.dx += self.walkspeed
            new_action = 1
        elif keys[pygame.K_UP]:
            self.dy -= self.walkspeed
            new_action = 3
        elif keys[pygame.K_DOWN]:
            self.dy += self.walkspeed
            new_action = 4
        else:
            new_action = 0



        if new_action != self.action:
            self.action = new_action
            self.frames = self.animation_list[self.action] # Update the active row
            self.frame_index = 0

        # Use self.frames to update the image
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

    def update(self, *args):
        self.rect.x += self.dx
        self.rect.y += self.dy


    def check_screen_collision(self, SCREEN_WIDTH, SCREEN_HEIGHT):
    # Horizontal collision
        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            

        # Vertical collision
        if self.rect.top < 0:
            self.rect.top = 0
            
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            