import pygame
from game_loop import game_loop
from restart import restart
from start_match import star_match

def start(scores, screen, font, redo_image, end_image, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down,
                  WIDTH, HEIGHT):
    letters = pygame.Rect(50, 250, 400, 400)
    numbers = pygame.Rect(550, 250, 400, 400)
    special = pygame.freetype.SysFont(None, 80)
    ready = True

    while ready:

        screen.fill('black')

        pygame.draw.rect(screen, 'grey', pygame.Rect(50, 250, 400, 400))
        pygame.draw.rect(screen, 'grey', pygame.Rect(550, 250, 400, 400))

        font.render_to(screen, (375, 50), f"Matching Game", pygame.Color('dodgerblue'))
        special.render_to(screen, (125, 425), f"Letters", pygame.Color('dodgerblue'))
        special.render_to(screen, (580, 425), f"Numbers", pygame.Color('dodgerblue'))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if letters.collidepoint(pos):
                    ready = star_match(scores, screen, font, redo_image, end_image, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS,
                            symbol_face_down,
                            WIDTH, HEIGHT)

                if numbers.collidepoint(pos):
                    ready = star_match(scores, screen, font, redo_image, end_image, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS,
                               symbol_face_down,
                               WIDTH, HEIGHT)
