import pygame

from lib import Vec2


class Rectangle:

    def __init__(self, size: Vec2, position: Vec2, color: tuple[int, int, int] = (255, 255, 255)):
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

    @staticmethod
    def check_collision(r1, r2):
        """checks for a collision between two rectangles, r1 and r2"""
        return r1.rect.colliderect(r2.rect)


class PlayerRectangle(Rectangle):

    def __init__(self, position: Vec2, score: int = 0):
        super().__init__(Vec2(20, 75), position, (255, 255, 255))
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.score = score
        self.font = pygame.font.Font(None, 144)

    def display_score(self, screen):
        score_text = self.font.render(f'{self.score}', True, (79, 149, 237))
        screen.blit(score_text, (self.position.x-20, 20))

    def update_and_draw_player(self, screen):
        self.update_position()
        self.display_score(screen)
        self.draw(screen)
