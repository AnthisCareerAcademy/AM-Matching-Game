import importlib.util
import subprocess
import sys

from end_game_loop import end_game_loop

if importlib.util.find_spec("pygame") is None:
    # Install the package using pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

import pygame
import pygame.freetype
from create_cards_letters import create_cards_letters


# Constants for card and game setup
CARD_SIZE = 200
MARGIN = 40
NUM_ROWS = 4
NUM_COLS = 4
WIDTH = (CARD_SIZE + MARGIN) * NUM_COLS + MARGIN
HEIGHT = (CARD_SIZE + MARGIN) * NUM_ROWS + MARGIN
scores = ['20','19']

# Initialize Pygame
pygame.init()
clock=pygame.time.Clock()
font=pygame.freetype.SysFont(None, 34)
font.origin=True

# Set up the display and images
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PM Anthis Memory Game")
symbol_face_down = pygame.image.load('cover_art/cover_art.jpg').convert()
redo_image = pygame.image.load('replay_buttons/play_again.jpg').convert()
end_image = pygame.image.load('replay_buttons/end_game.jpg').convert()





# Game loop
def game_loop():
    cards = create_cards_letters(NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down)
    first_card = None
    second_card = None
    clock = pygame.time.Clock()
    running = True
    not_over = True
    start_time = pygame.time.get_ticks()
    out = 20

    while running:
        screen.fill('black')
        if scores:
            font.render_to(screen, (500, 50), f"High Score: {scores[0]}", pygame.Color('dodgerblue'))
        else:
            font.render_to(screen, (500, 50), f"High Score:", pygame.Color('dodgerblue'))

        # Draw all cards
        for card in cards:
            card.draw(screen)

        end_game_loop(cards)

        #Timer
        ticks = pygame.time.get_ticks() - start_time
        millis = ticks % 1000
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        font.render_to(screen, (100, 50), out, pygame.Color('dodgerblue'))
        pygame.display.flip()
        clock.tick(60)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                #keeps track which cards are being compared
                for card in cards:
                    if card.rect.collidepoint(pos) and not card.revealed and not card.matched:
                        card.revealed = True

                        if first_card is None:
                            first_card = card
                        elif second_card is None:
                            second_card = card
                    card.draw(screen)
                    pygame.display.flip()

            # Check if two cards are flipped
            if first_card and second_card:
                pygame.time.wait(300)
                if first_card.symbol == second_card.symbol:
                    first_card.matched = True
                    second_card.matched = True
                else:
                    first_card.revealed = False
                    second_card.revealed = False
                first_card.draw(screen)
                second_card.draw(screen)
                pygame.display.flip()

                first_card = None
                second_card = None

        clock.tick(30)
    return out

def start_restart():
    out = game_loop()

    redo = pygame.Rect(50, 250, 400, 400)
    nope = pygame.Rect(550, 250, 400, 400)
    game_over = True

    #checks if the player wants to start a new round
    while game_over:

        scores.append(out)
        scores.sort()

        screen.fill('black')

        font.render_to(screen, (500, 50), f"High Score: {scores[0]}", pygame.Color('dodgerblue'))
        font.render_to(screen, (500, 150), f"Your Score: {out}", pygame.Color('dodgerblue'))

        image = pygame.transform.scale(redo_image, (400, 400))
        screen.blit(image, (50, 250))

        image = pygame.transform.scale(end_image, (400, 400))
        screen.blit(image, (550, 250))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if redo.collidepoint(pos):
                    game_loop()
                if nope.collidepoint(pos):
                    game_over = False


# Start the game
start_restart()

# Quit Pygame
pygame.quit()
