from hand import Hand


class Player:
    def __init__(self, money):
        self.name = "Player"
        self.money = money
        self.hand = Hand()
        self.current_bet = 0

    def start_hand(self, deck):
        self.hand = Hand()
        self.hand.add(deck.draw())
        self.hand.add(deck.draw())

    def draw(self, deck):
        self.hand.add(deck.draw())

    def bet(self, amount):
        if amount > self.money:
            # Invalid bet
            return False
        self.current_bet = amount
        self.money -= amount
        return True

    def get_score(self):
        return self.hand.get_score()

    def win(self):
        self.money += self.current_bet * 2

    def push(self):
        self.money += self.current_bet

    def show(self):
        score = str(self.get_score())
        for card in self.hand.cards:
            if card.turned:
                score = "?"
        print("[ %s - Score = %s ]" % (self.name, score))
        self.hand.show()

    def take_turn(self, deck, player=None):
        done = False
        while not done:
            self.show()
            # Blackjack or bust
            if self.get_score() >= 21:
                done = True
            else:
                hit = input("Hit? (y or n) > ")
                if hit == "y":
                    self.draw(deck)
                else:
                    done = True

