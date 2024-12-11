from game_loop_numbers import game_loop_numbers
from restart import restart

def star_match_numbers(scores, screen, font, redo_image, end_image, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS,
                    symbol_face_down,
                    WIDTH, HEIGHT):
    score = game_loop_numbers(scores, screen, font, NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down)

    ready = restart(scores, screen, font, redo_image, end_image,
                    WIDTH, HEIGHT, score)
    return ready