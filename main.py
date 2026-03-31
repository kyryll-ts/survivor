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

player = Player(100, 100)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)


class main():
	def __init__(self, displayh, displayw):

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


			player.input_update()
			all_sprites.update()

			window.fill((30, 30, 30))
			all_sprites.draw(window)
			
		
			
			pygame.display.update()
			clock.tick(60)






if __name__ == "__main__":
    # This block only runs if the script is the main entry point
    main(displayw, displayw)