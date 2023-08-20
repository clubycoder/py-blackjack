from deck import Deck


# A Hand is really just a Deck that
# starts out empty and knows how to
# calculate a score.
class Hand(Deck):
    def __init__(self):
        super().__init__()
        self.cards.clear()

    def add(self, card):
        self.cards.append(card)

    def get_score(self):
        score = 0
        # Add non aces (value < 11) first
        for card in self.cards:
            value = card.get_value()
            if value < 11:
                score += value
        # Add aces counting as an 1 or value
        # depending on if it would push the
        # score over 21
        for card in self.cards:
            value = card.get_value()
            if value >= 11:
                if score + value <= 21:
                    score += value
                else:
                    score += 1
        return score
