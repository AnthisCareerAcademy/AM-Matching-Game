import pygame
from timer import timer
from end_game_loop import end_game_loop
from event_handling import event_handling
from create_cards_numbers import create_cards_numbers

# Game loop
def game_loop_numbers(scores, screen, font, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down):
    cards = create_cards_numbers(NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down)
    first_card = None
    second_card = None
    clock = pygame.time.Clock()
    running = True
    start_time = pygame.time.get_ticks()

    while running:
        screen.fill('black')
        if scores:
            font.render_to(screen, (500, 50), f"High Score: {scores[0]}", pygame.Color('dodgerblue'))
        else:
            font.render_to(screen, (500, 50), f"High Score:", pygame.Color('dodgerblue'))

        # Draw all cards
        for card in cards:
            card.draw(screen)

        running = end_game_loop(cards)

        score = timer(start_time, font, screen, clock)

        pygame.display.flip()

        first_card, second_card = event_handling(cards, first_card, second_card, screen)

        clock.tick(30)
        #running = False

    return score