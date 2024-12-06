import pygame
import random

# Constants for card and game setup
CARD_SIZE = 100
MARGIN = 20
NUM_ROWS = 4
NUM_COLS = 4
WIDTH = (CARD_SIZE + MARGIN) * NUM_COLS + MARGIN
HEIGHT = (CARD_SIZE + MARGIN) * NUM_ROWS + MARGIN

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PM Anthis Memory Game")

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
            pygame.draw.rect(screen, WHITE, self.rect)
            font = pygame.font.Font(None, 74)
            text = font.render(str(self.symbol), True, RED)
            screen.blit(text, (self.position[0] + 35, self.position[1] + 25))
        else:
            pygame.draw.rect(screen, GREEN, self.rect)

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
    symbols = list(range(8)) * 2  # 8 unique symbols, each appearing twice
    random.shuffle(symbols)
    return symbols

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

    while running:
        screen.fill(BLACK)

        # Draw all cards
        for card in cards:
            card.draw(screen)

        # Event handling
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

                # Check if two cards are flipped
                if first_card and second_card:
                    if first_card.symbol == second_card.symbol:
                        first_card.matched = True
                        second_card.matched = True
                    else:
                        pygame.time.wait(500)
                        first_card.revealed = False
                        second_card.revealed = False

                    first_card = None
                    second_card = None

        pygame.display.flip()
        clock.tick(30)

# Start the game
game_loop()

# Quit Pygame
pygame.quit()
