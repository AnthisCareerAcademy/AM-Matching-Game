from card_positions import create_card_positions
from generating_pairs_numbers import generate_pairs_numbers
from Numbers import Numbers

#create the cards
def create_cards_letters(NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down):
    positions = create_card_positions(NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS)
    pairs = generate_pairs_numbers()
    cards = []
    for i, symbol in enumerate(pairs):
        card = Numbers(symbol, positions[i], CARD_SIZE, symbol_face_down)
        cards.append(card)
    return cards