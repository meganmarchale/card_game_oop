import math

class Symbol():
    
    # This class creates icons and colors and attributes and we attribute a color to each icon.
    
    def __init__(self, icon):
       # icons = ["♥", "♦", "♣", "♠"]
       # colors = ["red", "black"]
        self.icon = icon
        if icon == "♥" or icon == "♦":
            self.color = "red"
        else:
            self.color = "black"

        
test= Symbol("♥")
print(test.color)


class Card(Symbol):
    
    # This method creates cards. Each card created should have a value and an icon. The color is already defined.
    
    def __init__(self,icon, value):
        super().__init__(icon)
        self.value = value

    def __str__(self):
        return f"{self.icon}{self.value}"
    
test_card = Card("♥", "2")
print(test_card)
        

class Deck:
    def __init__(self):
        self.icons = ["♥", "♦", "♣", "♠"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.full_deck = []
    
    def create_deck(self):
        for icon in self.icons:
            for value in self.values:
                self.full_deck.append(icon + value)
        return self.full_deck


my_deck = Deck()
deck_list = my_deck.create_deck()

print(deck_list)



