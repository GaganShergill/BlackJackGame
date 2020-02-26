from Player import Player
from Hand import Hand
from Deck import Deck

class BlackJack:
    def __init__(self, num_of_deck=1):
        self.players = []
        self.dealer = Hand()
        self.deck = Deck(num_of_deck)
        self.dealer_blackjack = False
        self.all_players_bust = True

    def input_number_of_players(self):
        while True:
            try:
                num = int(input("Enter Number of Players?(1-4): "))
            except ValueError:
                print("Wrong Value! Try Again")
            else:
                if num in range(1, 5):
                    break
                else:
                    print("Number of Players not in range 1 to 4!")
        return num

    def input_name(self, num):
        while True:
            name = input(f"Enter Player {num} name(aA-zZ): ")
            if name.isalpha():
                name = name.capitalize()
                break
            else:
                print("Enter the Alphabets(a-z)!!")
        return name

    def input_total_chips(self, name):
        while True:
            try:
                total = int(input(f'{name}, total Chips you want to buy?(Max Limit: 25,000): '))
            except ValueError:
                print('Wrong Entry ! Enter Again')
            else:
                if total > 25000:
                    print("Maximum Limit Exceeded. Enter Again")
                elif total <= 0:
                    print("Invalid Amount ! Enter Again")
                else:
                    break
        return total

    def input_bet(self, name, total):
        while True:
            try:
                bet = int(input(f'{name}, how many chips will you Bet? (Total Chips:{total}): '))
            except ValueError:
                print('Wrong Entry ! Enter Again')
            else:
                if bet > total:
                    print("You don't have enough money! Bet Again")
                elif bet <= 0:
                    print("Invalid Bet ! Bet Again")
                else:
                    break
        return bet

    def display_all(self, show_dealer2_card=False):
        print('\nCurrent Hands on Table---->>')
        if show_dealer2_card:
            print(f'Dealer: {self.dealer.cards}; Total: {self.dealer.value}')
        else:
            print(f"Dealer: ['{self.dealer.cards[0]}', 'Hidden']")
        for player in self.players:
            print(f'{player.name}: {player.hand.cards}; Total Sum: {player.hand.value}; Bet: {player.chip.bet}')

    def ask_decision(self, player):
        while True:
            option = ']'
            if player.chip.bet * 2 <= player.chip.total and len(player.hand.cards) == 2:
                option = ', 3.Double Down]'
            try:
                decision = int(input('Choose your Option[1.Hit, 2.Stand'+option))
            except ValueError:
                print('Wrong Entry! Enter Again')
            else:
                if option == ']':
                    if decision not in [1, 2]:
                        print('Enter from the options stated')
                    else:
                        break
                else:
                    if decision not in [1, 2, 3]:
                        print('Enter from the options stated')
                    else:
                        break
        return decision

    def show_results(self):
        for player in self.players:
            print(player.name + '---->>')
            if player.blackjack:
                if self.dealer_blackjack:
                    print('PUSH')
                else:
                    player.chip.blackjack()
                    print('WINS')

            elif player.hand.value < 21:
                if self.dealer.value > 21:
                    player.chip.win_bet()
                    print('WINS')
                elif self.dealer.value < 21:
                    if self.dealer.value < player.hand.value:
                        player.chip.win_bet()
                        print('WINS')
                    elif self.dealer.value == player.hand.value:
                        print('PUSH')
                    else:
                        player.chip.lose_bet()
                        print('LOSE')
                else:
                    player.chip.lose_bet()
                    print('LOSE')

            elif player.hand.value == 21:
                if self.dealer_blackjack:
                    player.chip.lose_bet()
                    print('LOSE')
                elif self.dealer.value == 21:
                    print('PUSH')
                else:
                    player.chip.win_bet()
                    print('WINS')

            else:
                player.chip.lose_bet()
                print('LOSE')

    def display_chips(self):
        print('\nRemaining Chips-->')
        for player in self.players:
            print(f'{player.name}: {player.chip.total}')

    def make_players(self):
        num = self.input_number_of_players()
        for i in range(num):
            name = self.input_name(i + 1)
            total = self.input_total_chips(name)
            self.players.append(Player(name, total))

    def play(self):
        self.deck.shuffle()
        for player in self.players:
            player.chip.bet = self.input_bet(player.name, player.chip.total)
            player.hand.add_card(self.deck.deal())
            player.hand.add_card(self.deck.deal())
            player.hand.adjust_for_aces()

        self.dealer.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.dealer.adjust_for_aces()
        if self.dealer.value == 21:
            self.dealer_blackjack = True
        self.display_all()

        for player in self.players:
            print(player.name + "'s Turn --->")
            if player.hand.value == 21:
                player.blackjack = True
                print("BLACK JACK!")
                continue

            while True:
                decision = self.ask_decision(player)
                if decision == 1:       #hit option
                    player.hand.add_card(self.deck.deal())
                    player.hand.adjust_for_aces()

                    if player.hand.value == 21:
                        print(f'{player.hand.cards}; Total Sum: {player.hand.value}')
                        break
                    elif player.hand.value > 21:
                        player.bust = True
                        print(f'{player.hand.cards}; Total Sum: {player.hand.value}')
                        print('BUSTED!!!')
                        break
                    print(f'{player.hand.cards}; Total Sum: {player.hand.value}')

                elif decision == 2:     #stand option
                    break
                elif decision == 3:     #double down
                    player.chip.bet *= 2
                    player.hand.add_card(self.deck.deal())
                    player.hand.adjust_for_aces()
                    if player.hand.value > 21:
                        player.bust = True
                        print(f'{player.hand.cards}; Total Sum: {player.hand.value}')
                        print('BUSTED!!!')
                    else:
                        print(f'{player.hand.cards}; Total Sum: {player.hand.value}')
                    break

        for player in self.players:
            if not player.bust:
                self.all_players_bust = False

        print("Dealer's Turn --->")
        while not self.all_players_bust and self.dealer.value < 17:
            self.dealer.add_card(self.deck.deal())
            self.dealer.adjust_for_aces()
        print(f'{self.dealer.cards}; Total Sum: {self.dealer.value}')

        self.display_all(True)
        self.show_results()
        self.display_chips()

    def reset(self, deck_num):
        game_details = []
        deck = self.deck
        for player in self.players:
            game_details.append((player.name, player.chip.total))

        self.__init__(deck_num)
        self.deck = deck
        for name, total in game_details:
            if total <= 0:
                print(f'Due to Low Balance, {name} is kicked out')
                continue
            self.players.append(Player(name, total))
        if len(self.players) == 0:
            print('No Players Left')
            print('Exiting....')
            return False
        return True
