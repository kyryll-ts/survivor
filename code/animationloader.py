import pygame

class SpriteSheet(object):
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
        try:
            self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
        except pygame.error as message:
            print('Cannot load image:', file_name)
            raise SystemExit(message)

    def get_image(self, x, y, width, height):
        
        image = pygame.Surface([width, height], pygame.SRCALPHA).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        
        return image