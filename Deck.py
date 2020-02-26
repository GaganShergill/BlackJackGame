from Card import Card
import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Ace', 'Jack', 'Queen', 'King']


class Deck:
    def __init__(self, num):
        self.num = num
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        self.deck *= self.num

    def __str__(self):
        deck_comp = ''
        for suit in suits:
            for rank in ranks:
                deck_comp += '\n' + rank + ' of ' + suit
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        if len(self.deck) == 0:
            self.__init__(self.num)
            self.shuffle()
        return single_card