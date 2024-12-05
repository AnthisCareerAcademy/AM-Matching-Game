import pygame
import random

# Cards for the game
CARD_SIZE = 100
MARGIN = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def create_card_positions():
    positions = []
    for i in range(4):
        for j in range(4):
            x = MARGIN + j * (CARD_SIZE + MARGIN)
            y = MARGIN + i * (CARD_SIZE + MARGIN)
            positions.append((x, y))
    return positions

positions = create_card_positions()

# Generate pairs
def generate_pairs():
    symbols = list(range(8)) * 2
    random.shuffle(symbols)
    return symbols
pairs = generate_pairs()

# Cards class
class Card: # Card class
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
            text = font.render(str(self.symbol), True, BLACK)
            screen.blit(text, (self.position[0] + 35, self.position[1] + 25))
        else:
            pygame.draw.rect(screen, GREEN, self.rect)