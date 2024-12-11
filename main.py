import importlib.util
import subprocess
import sys


if importlib.util.find_spec("pygame") is None:
    # Install the package using pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

import pygame
import pygame.freetype

# Constants for card and game setup
CARD_SIZE = 200
MARGIN = 40
NUM_ROWS = 4
NUM_COLS = 4
WIDTH = (CARD_SIZE + MARGIN) * NUM_COLS + MARGIN
HEIGHT = (CARD_SIZE + MARGIN) * NUM_ROWS + MARGIN
scores = []

# Initialize Pygame
pygame.init()
clock=pygame.time.Clock()
font=pygame.freetype.SysFont(None, 34)
font.origin=True

# Set up the display and images
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PM Anthis Memory Game")
symbol_face_down = pygame.image.load('cover_art/bloosmoil.png').convert()
redo_image = pygame.image.load('replay_buttons/play_again.jpg').convert()
end_image = pygame.image.load('replay_buttons/end_game.jpg').convert()


from start import start

# Start the game
start(scores, screen, font, redo_image, end_image, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down, WIDTH, HEIGHT)

# Quit Pygame
pygame.quit()