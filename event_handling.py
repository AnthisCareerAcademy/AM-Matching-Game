import pygame
from main import screen, clock

# Event handling
def event_handling(cards, first_card, second_card):
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # keeps track which cards are being compared
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