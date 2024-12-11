from game_loop import game_loop
from restart import restart

def star_match(scores, screen, font, redo_image, end_image, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS,
                    symbol_face_down,
                    WIDTH, HEIGHT):
    score = game_loop(scores, screen, font, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down)

    ready = restart(scores, screen, font, redo_image, end_image, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS,
                    symbol_face_down,
                    WIDTH, HEIGHT, score)
    return ready