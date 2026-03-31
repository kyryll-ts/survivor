import pygame
from pathlib import Path

pygame.init()

BASE_DIR = Path(__file__).resolve().parent

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.walkspeed = 4

        self.player_path = BASE_DIR.parent / "assets" / "player.png"

        if not self.player_path.exists():
            raise FileNotFoundError(f"Missing image: {self.player_path}")

        self.image = pygame.image.load(self.player_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        pass