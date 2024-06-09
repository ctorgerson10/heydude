import math
import random
import pygame
from pygame.locals import *

from lib import Rectangle, Vec2

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("hey dude!")
clock = pygame.time.Clock()
running = True

# game config
scale = 50
fps = 120
speed = 5
max_rectangles = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# define shapes
r1 = Rectangle(Vec2(scale, scale), Vec2(scale, scale), RED)
r1.set_velocity(Vec2(5, 5))

rectangles = [r1]

def spawn_new_rectangle():
    if not len(rectangles) >= max_rectangles:
        size = Vec2(scale, scale)
        position = Vec2(random.randint(0, width - scale), random.randint(0, height - scale))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        velocity = Vec2(random.randint(1, speed * 2), random.randint(1, speed * 2))
        rectangles.append(Rectangle(size, position, color).set_velocity(velocity))


if fps == 120:
    speed = math.floor(speed / 2)

while running:
    keys = pygame.key.get_pressed()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    for shape in rectangles:
        shape.draw(screen)
        shape.update_position()

        if shape.position.x >= width - scale or shape.position.x <= 0:
            shape.velocity.x *= -1
            shape.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            spawn_new_rectangle()

        if shape.position.y >= height - scale or shape.position.y <= 0:
            shape.velocity.y *= -1
            shape.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            spawn_new_rectangle()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
