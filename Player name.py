# Get player name
def get_player_name_and_(score):
    input_box=pygame.Rect(WIDTH//4, HEIGHT//3, WIDTH//2,40)
    active=True
    player_name=''
    font=pygame.freetype.SysFont(None,34)

    while active:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
              pygame.quit()
              sys.exit()

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active=False
                elif event.key == pygame.K_BACKSPACE:
                    player_name=player_name[:-1]
                else:
                    player_name=event.unicode
        screen.fill('black')
        font.render_to(screen,(500, 50),f'High Score: {scores[0]}',pygame.Color('dodgerblue'))
        font.render_to(screen, (500, 150), f"Your Score: {score}", pygame.Color('dodgerblue'))

        pygame.draw.rect(screen,pygame.Color('dodgerblue'), input_box,2)
        font.render_to(screen,(input_box.x+5, input_box.y+5),player_name,pygame.Color('dodgerblue'))
        pygame.display.flip()
    print(f'Player: {player_name},Score:{score}')
    return player_name,score