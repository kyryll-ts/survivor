import pygame
import sys
from pathlib import Path
pygame.init()


TILES = 16
TILE_SIZE = 32

displayw = TILES * TILE_SIZE
displayh = TILES * TILE_SIZE
window = pygame.display.set_mode((displayw,displayh))

clock = pygame.time.Clock()

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"
CODE_DIR = BASE_DIR.parent / "code"

PLAYER = CODE_DIR / "player.py"
from code.player import Player
from code.enemy import Enemy

player = Player(displayw //2, displayh //2)
enemy = Enemy(displayw //2,10)

all_sprites = pygame.sprite.Group()
all_sprites.add(enemy)
all_sprites.add(player)



class main(pygame.sprite.Sprite):
	def __init__(self, displayh, displayw):

		super().__init__()

		self.dh = displayh
		self.dw = displayw

		self.main()



	def main(self):

		running = True

		while running:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					pygame.quit()
					sys.exit()

			enemy.update(player.rect)

			#enemy.check_player_collision(player.rect)
			player.input_update()
			player.check_screen_collision(displayh, displayw)
			all_sprites.update(player.rect)

			window.fill((30, 30, 30))
			enemy.draw(window)
			all_sprites.draw(window)
			
		
			
			pygame.display.update()
			clock.tick(60)






if __name__ == "__main__":
    # This block only runs if the script is the main entry point
    main(displayw, displayw)