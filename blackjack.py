from deck import Deck
from house import House
from player import Player


house = House()
player = Player(100)

done = False
while not done:
    deck = Deck()
    # Player bet
    valid_bet = False
    while not done and not valid_bet:
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("You have $%d" % (player.money))
        bet_amount = input("Bet or q to quit > ")
        if bet_amount == "q":
            done = True
        else:
            valid_bet = player.bet(int(bet_amount))
    if not done:
        player.start_hand(deck)
        house.start_hand(deck)
        house.show()
        player.take_turn(deck)
        # Player busts
        if player.get_score() > 21:
            print("Player busts!")
        else:
            house.take_turn(deck, player)
            # House busts
            if house.get_score() > 21:
                print("House busts!")
                player.win()
            # Player wins
            elif player.get_score() > house.get_score():
                print("Player wins!")
                player.win()
            # Push
            elif player.get_score() == house.get_score():
                print("Push!")
                player.push()
            # Player loses
            else:
                print("House wins!")
