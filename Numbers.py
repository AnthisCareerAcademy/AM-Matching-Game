import pygame

#class for the numbers
class Numbers:
    def __init__(self, symbol, position, CARD_SIZE, symbol_face_down):
        self.symbol = symbol
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], CARD_SIZE, CARD_SIZE)
        self.revealed = False
        self.matched = False
        self.symbol_face_down = symbol_face_down

    def draw(self, screen):
        if self.revealed or self.matched:
            image = pygame.transform.scale(self.symbol,(120,120))
            screen.blit(image, (self.position[0] + 35, self.position[1] + 25))
        else:
            image = pygame.transform.scale(self.symbol_face_down, (120, 120))
            screen.blit(image, (self.position[0] + 35, self.position[1] + 25))