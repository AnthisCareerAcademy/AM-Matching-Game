#ends the game
def end_game_loop(cards):
    for card in cards:
        if not card.matched:
            running = True
            break
        else:
            running = False
    return running