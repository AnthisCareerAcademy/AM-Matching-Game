import pygame
import pygame.freetype
from player_name import get_player_name

def restart(scores, screen, font, redo_image, end_image,
                  WIDTH, HEIGHT, score):

    redo = pygame.Rect(50, 250, 400, 400)
    nope = pygame.Rect(550, 250, 400, 400)
    player_name = get_player_name(WIDTH, HEIGHT, screen)
    scores.append([score, player_name])
    scores = sorted(scores, key=lambda x: x[0])
    game_over = True

    #checks if the player wants to start a new round
    while game_over:
        screen.fill('black')

        font.render_to(screen, (500, 50), f'High Score: {scores[0][0]} - {scores[0][1]}', pygame.Color('dodgerblue'))
        font.render_to(screen, (500, 150), f"Your Score: {score}", pygame.Color('dodgerblue'))

        image = pygame.transform.scale(redo_image, (400, 400))
        screen.blit(image, (50, 250))

        image = pygame.transform.scale(end_image, (400, 400))
        screen.blit(image, (550, 250))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if redo.collidepoint(pos):
                    ready = True
                    game_over = False

                if nope.collidepoint(pos):
                    ready = False
                    game_over = False

    return ready
