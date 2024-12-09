import pygame
import random
import importlib.util
import subprocess
import sys
import pygame.freetype


if importlib.util.find_spec("pygame") is None:
    # Install the package using pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

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

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PM Anthis Memory Game")
symbol_face_down = pygame.image.load('cover_art/cover_art.jpg').convert()

# Card class
class Card:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], CARD_SIZE, CARD_SIZE)
        self.revealed = False
        self.matched = False

    def draw(self, screen):
        if self.revealed or self.matched:
            image = pygame.transform.scale(self.symbol,(300,120))
            screen.blit(image, (self.position[0] + 35-90, self.position[1] + 25))
        else:
            image = pygame.transform.scale(symbol_face_down, (120, 120))
            screen.blit(image, (self.position[0] + 35, self.position[1] + 25))


# Create card positions on the board
def create_card_positions():
    positions = []
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            x = MARGIN + j * (CARD_SIZE + MARGIN)
            y = MARGIN + i * (CARD_SIZE + MARGIN)
            positions.append((x, y))
    return positions

# Generate pairs of symbols (for a memory matching game)
def generate_pairs():
    symbols_face_up = [pygame.image.load("Matching game/A.png").convert(), pygame.image.load("Matching game/B.png").convert(), pygame.image.load("Matching game/C.png").convert(), pygame.image.load("Matching game/H.png").convert(), pygame.image.load("Matching game/L.png").convert(), pygame.image.load("Matching game/P.png").convert(), pygame.image.load("Matching game/S.png").convert(), pygame.image.load("Matching game/W.png").convert()] * 2  # 8 unique symbols, each appearing twice
    random.shuffle(symbols_face_up)
    return symbols_face_up

# Create the cards
def create_cards():
    positions = create_card_positions()
    pairs = generate_pairs()
    cards = []
    for i, symbol in enumerate(pairs):
        card = Card(symbol, positions[i])
        cards.append(card)
    return cards


# Game loop
def game_loop():
    cards = create_cards()
    first_card = None
    second_card = None
    clock = pygame.time.Clock()
    running = True
    not_over = True
    start_time = pygame.time.get_ticks()
    redo = pygame.Rect(100, 100, CARD_SIZE, CARD_SIZE)
    nope = pygame.Rect(200, 100, CARD_SIZE, CARD_SIZE)
    while running:
        screen.fill('black')

        # Draw all cards

        for card in cards:
            card.draw(screen)
        pygame.display.flip()

        for card in cards:
            if not card.matched:
                running = True
                break
            else:
                running = False

        # Event handling
        ticks = pygame.time.get_ticks() - start_time
        millis = ticks % 1000
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        font.render_to(screen, (100, 50), out, pygame.Color('dodgerblue'))
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
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
                pygame.time.wait(500)
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
    scores.append(out)
    scores.sort(reverse=True)
    print(scores[0])
    while True:
        screen.fill('black')
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

            if redo == pos:
                running = True
                game_loop()
            elif nope == pos:
                break



# Start the game
game_loop()

# Quit Pygame
pygame.quit()
