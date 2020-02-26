from Hand import Hand
from Chip import Chip

class Player:
    def __init__(self, name, total=100):
        self.name = name
        self.chip = Chip(total)
        self.hand = Hand()
        self.blackjack = False
        self.bust = False
