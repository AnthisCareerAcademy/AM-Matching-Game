import pygame
import pygame.freetype
from game_loop import game_loop

def start_restart(scores, screen, font, redo_image, end_image, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down):
    out = game_loop(screen, scores, font, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down)

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