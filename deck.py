import random
from cards import cards


# The Deck starts out with all of the
# cards shuffled, lets you draw a
# card, and knows how to show them.
class Deck:
    def __init__(self):
        self.cards = cards.copy()
        random.shuffle(self.cards)

    def num_cards(self):
        return len(self.cards)

    def draw(self):
        card = self.cards.pop()
        return card

    def show(self):
        num_rows = int(self.num_cards() / 8)
        if self.num_cards() % 8 > 0:
            num_rows += 1
        for row in range(num_rows):
            for line in range(5):
                for row_card_num in range(8):
                    card_num = row * 8 + row_card_num
                    if card_num < len(self.cards):
                        card = self.cards[card_num]
                        print(card.get_graphic_line(line), end=" ")
                print("")
