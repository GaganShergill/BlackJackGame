from BlackJack import BlackJack


def input_number_of_decks():
    while True:
        try:
            deck_num = int(input(f"Enter the Number of Decks to be used(1-3): "))
        except ValueError:
            print("Wrong Value! Try Again")
        else:
            if deck_num not in range(1,4):
                print('Enter in range 1 to 3')
            else:
                break
    return deck_num



if __name__ == '__main__':

    print("BlackJack Game--->")
    deck_num = input_number_of_decks()
    game = BlackJack(deck_num)
    game.make_players()
    continue_game = True
    while continue_game:
        game.play()
        another_game = input('Play another game(y/n)?')
        if another_game.lower() == 'y':
            continue_game = game.reset(deck_num)
        else:
            print('Hasta La Vista Baby')
            continue_game = False
