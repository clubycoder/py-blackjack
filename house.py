from player import Player


# The House is mostly just like a
# Player that doesn't run out of money
class House(Player):
    def __init__(self):
        super().__init__(0)
        self.name = "House"

    def start_hand(self, deck):
        super().start_hand(deck)
        # The house hides the second card
        self.hand.cards[1].turned = True

    def take_turn(self, deck, player):
        self.hand.cards[1].turned = False
        done = False
        while not done:
            self.show()
            # Already higher than player
            if self.get_score() > player.get_score():
                done = True
            # Blackjack or bust
            elif self.get_score() >= 21:
                done = True
            # Should draw
            elif self.get_score() < 17:
                self.draw(deck)
            # High enough to stay
            else:
                done = True

