import pygame
import sys
pygame.init()


TILES = 16
TILE_SIZE = 32

displayw = TILES * TILE_SIZE
displayh = TILES * TILE_SIZE
window = pygame.display.set_mode((displayw,displayh))

clock = pygame.time.Clock()

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



		
			18, 171, 227
			pygame.display.update()
			clock.tick(60)






if __name__ == "__main__":
    # This block only runs if the script is the main entry point
    main(displayw, displayw)