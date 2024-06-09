import pygame

from lib import Vec2


class Rectangle:

    def __init__(self, size: Vec2, position: Vec2, color: tuple[int, int, int] = (0, 0, 0)):
        self.size = size
        self.position = position
        self.velocity = Vec2(0, 0)
        self.color = color
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def update_position(self):
        self.position += self.velocity
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def set_velocity(self, new_velocity: Vec2):
        self.velocity = new_velocity
        return self
