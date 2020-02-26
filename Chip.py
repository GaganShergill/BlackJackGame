class Chip:
    def __init__(self, total):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def blackjack(self):
        self.total += int(self.bet*1.5)