import math
import random
import time
from enum import Enum

import pygame
from pygame.locals import *

from lib import PlayerRectangle, Rectangle, Vec2

pygame.init()
width, height = 720, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("hey dude!")
clock = pygame.time.Clock()
running = True

# game config
scale = 50
fps = 60
speed = 5


# game state
class State(Enum):
    STARTING = 1
    RUNNING = 2
    PAUSED = 3
    ENDING = 4
    EXIT = 5


current_state = State.STARTING

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (237, 79, 149)
GREEN = (149, 237, 79)
BLUE = (79, 149, 237)


# functions


def quit_game():
    """ran when user exits the program"""
    pygame.quit()


def reset_game(p1score: int = 0, p2score: int = 0):
    """resets players and ball to start positions"""
    player1 = PlayerRectangle(Vec2(50, height/2), p1score)
    player2 = PlayerRectangle(Vec2(width-70, height/2), p2score)
    player_objects = (player1, player2)
    ball_object = Rectangle(Vec2(15, 15), Vec2(width/2, height/2), GREEN)
    return player_objects, ball_object


def check_victory_condition():
    global current_state
    if p1.score == 5:
        current_state = State.ENDING
        declare_victor("Player 1")
    if p2.score == 5:
        current_state = State.ENDING
        declare_victor("Player 2")


def set_random_ball_velocity():
    """sets ball velocity randomly"""
    global ball
    ball.set_velocity(Vec2(random.choice([-speed-1, speed+1]), random.choice([-speed+3, speed-3])))


# initial setup
players, ball = reset_game()
p1, p2 = players
start_button = pygame.font.Font(None, 64).render("SPACE to Start", True, GREEN)
if fps == 120:
    speed = math.floor(speed / 2)


# start menu
def start_menu():
    """basic start menu"""
    global current_state
    while current_state == State.STARTING:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_state = State.EXIT
                quit_game()

        screen.fill(BLACK)

        # render
        screen.blit(start_button, (width/2 - start_button.get_size()[0]//2, height/2))

        if keys[pygame.K_SPACE]:
            current_state = State.RUNNING

        # flip()
        pygame.display.flip()
        clock.tick(fps)

    if current_state == State.RUNNING:
        play()


def countdown(display, start: int):
    font = pygame.font.Font(None, 64)
    """countdown screen before game starts"""
    for i in range(start, 0, -1):
        display.fill(BLACK)
        countdown_text = font.render(str(i), True, GREEN)
        display.blit(countdown_text, (width // 2 - countdown_text.get_width() // 2, height // 2 - countdown_text.get_height() // 2))
        for player in players:
            player.update_and_draw_player(display)
        pygame.display.flip()
        time.sleep(1)


# main game loop
def play():
    global current_state, p1, p2, ball, players

    countdown(screen, 3)
    set_random_ball_velocity()

    while current_state == State.RUNNING:
        keys = pygame.key.get_pressed()
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_state = State.EXIT
                quit_game()

        # fill screen / clear last frame
        screen.fill(BLACK)

        # render game
        for player in players:
            player.update_and_draw_player(screen)

        ball.update_position()
        ball.draw(screen)

        # player movement
        if keys[pygame.K_w]:
            if not p1.position.y < 0:
                p1.position.y -= speed
        if keys[pygame.K_s]:
            if p1.position.y < height - p1.size.y:
                p1.position.y += speed
        if keys[pygame.K_UP]:
            if not p2.position.y < 0:
                p2.position.y -= speed
        if keys[pygame.K_DOWN]:
            if p2.position.y < height - p2.size.y:
                p2.position.y += speed

        # ball checks
        if ball.position.x < 0:
            players, ball = reset_game(p1.score, p2.score + 1)
            p1, p2 = players
            check_victory_condition()
            countdown(screen, 2)
            set_random_ball_velocity()
        if ball.position.x >= width:
            players, ball = reset_game(p1.score + 1, p2.score)
            p1, p2 = players
            check_victory_condition()
            countdown(screen, 2)
            set_random_ball_velocity()

        if ball.position.y <= 0 or ball.position.y >= width - ball.size.y:
            ball.velocity.y *= -1
        if Rectangle.check_collision(ball, p1) or Rectangle.check_collision(ball, p2):
            ball.velocity.x *= -1
            ball.velocity.y *= random.choice([-1, 1])
            ball.velocity.y += random.choice([-1, 0, 1])

        # flip()
        pygame.display.flip()
        clock.tick(fps)


def declare_victor(victor: str):
    global current_state, screen, players, p1, p2, ball

    while current_state == State.ENDING:
        keys = pygame.key.get_pressed()
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_state = State.EXIT
                quit_game()

        screen.fill(BLACK)

        message = pygame.font.Font(None, 64).render(f"{victor} wins!", True, BLUE)
        restart = pygame.font.Font(None, 64).render("SPACE to restart", True, BLUE)
        screen.blit(message, (width/2 - message.get_size()[0]//2, height/2))
        screen.blit(restart, (width/2 - restart.get_size()[0]//2, height/2 + message.get_size()[1]))

        for player in players:
            player.update_and_draw_player(screen)

        if keys[pygame.K_ESCAPE]:
            current_state = State.EXIT
            quit_game()
        if keys[pygame.K_SPACE]:
            current_state = State.RUNNING
            players, ball = reset_game()
            p1, p2 = players
            start_menu()

        pygame.display.flip()
        clock.tick(fps)


start_menu()
