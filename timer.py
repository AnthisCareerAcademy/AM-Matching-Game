import pygame
import pygame.freetype

def timer(start_time, font, screen, clock):
    ticks = pygame.time.get_ticks() - start_time
    millis = ticks % 1000
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes,
                                                        millis=millis,
                                                        seconds=seconds)
    font.render_to(screen, (100, 50), out, pygame.Color('dodgerblue'))
    pygame.display.flip()
    clock.tick(60)

    pygame.display.flip()
