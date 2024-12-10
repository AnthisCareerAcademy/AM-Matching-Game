from card_positions import create_card_positions
from generating_pairs_letters import generate_pairs_letters
from Letters import Letters

#create the cards
def create_cards_letters(NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS, symbol_face_down):
    positions = create_card_positions(NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS)
    pairs = generate_pairs_letters()
    cards = []
    for i, symbol in enumerate(pairs):
        card = Letters(symbol, positions[i], CARD_SIZE, symbol_face_down)
        cards.append(card)
    return cards