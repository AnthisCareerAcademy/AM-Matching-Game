import pygame.freetype
import sys

# Get player name
def get_player_name(WIDTH, HEIGHT, screen):
    input_box=pygame.Rect(WIDTH//4, HEIGHT//3, WIDTH//2,40)
    active=True
    player_name=''
    font=pygame.freetype.SysFont(None,34)
    pygame.event.clear()
    special = pygame.freetype.SysFont(None, 80)

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active=False
                elif event.key == pygame.K_BACKSPACE:
                    player_name=player_name[:-1]
                else:
                    player_name+=event.unicode
        screen.fill('black')

        special.render_to(screen, (280, 150), f"Enter Name", pygame.Color('dodgerblue'))

        pygame.draw.rect(screen,pygame.Color('dodgerblue'), input_box,2)
        font.render_to(screen,(input_box.x+5, input_box.y+5),player_name,pygame.Color('dodgerblue'))
        pygame.display.flip()

    return player_name