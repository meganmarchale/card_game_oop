from card import Deck, Card
import math
import random

# I have already created my cards in Card() and my full deck in Deck().
# Now I'll create a class player that will suffle the card and then distribute the cards to the players


class Player:
    def __init__ (self, players):
        self.players = ["Jan", "Tom", "Meg", "Max"]
        self.hand = []

# If time : adding conditions -- number of players should be between 0 and 52 tops. 
class turn_count(Player):
    def __init__(self):
        super().__init__(Player)
        self.num_players = len(self.players)
        self.num_turn = math.floor(52 // self.num_players)
        self.remaining_cards = 52 % self.num_players
    
    def test(self):
        return self.num_players
        return self.num_turn
        return self.remaining_cards
    
    def __str__(self):
        return f"Players: {self.num_players}, Turns: {self.num_turn}"


test_turn = turn_count()
print(test_turn)


# Now I need to shuffle my deck and then distribute the cards
class Shuffle(Deck):
    def __init__(self):
        super().__init__(Deck)

    def shuffle_deck(self):
        random.shuffle(self.full_deck)
        return self.full_deck

test_shuffle = Shuffle()
print(test_shuffle)

class distribute(Player, Deck):
    def __init__(self):
        super().__init__(Player, Deck)
        for player in self.players:
            for Card in self.full_deck:
