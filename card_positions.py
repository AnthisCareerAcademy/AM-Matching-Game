#creating positions for cards
def create_card_positions(NUM_ROWS, MARGIN, CARD_SIZE, NUM_COLS):
    positions = []
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            x = MARGIN + j * (CARD_SIZE + MARGIN)
            y = MARGIN + i * (CARD_SIZE + MARGIN)
            positions.append((x, y))
    return positions