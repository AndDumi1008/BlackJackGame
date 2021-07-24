# Functions.py

playing = True
show = True


# function for taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f'\nYou have {chips.total}. How many chips you want to bet? '))
        except ValueError:
            print('Error. Please enter an integer!')
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet exceed your total. Bet carefully, you have ', chips.total, ' chips.')
            else:
                break


# function for taking hits
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# function prompting the Player to Hit or Stand
def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    global show

    while True:
        option_HS = input("\n\nWould you like to Hit or Stand? (H/S): ")

        if option_HS.lower() == 'h' or option_HS.lower() == 'hit':
            hit(deck, hand)
            show = True

        elif option_HS.lower() == 's' or option_HS.lower() == 'stand':
            print('Player stands. Dealer is playing.')
            playing = False
            show = False

        else:
            print('Sorry, please try again.')
            continue
        break


# functions to display cards
def show_some(player, dealer):
    print("\n\nDealer's Hand:\n")
    print(" <Card Hidden>")
    print('', dealer.cards[1])
    print('--------------------------------')
    print("Player's Hand:\n", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\n\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("\nDealer's Hand =", dealer.value)
    print('--------------------------------')
    print("Player's Hand:", *player.cards, sep='\n ')
    print("\nPlayer's Hand =", player.value)


# handle end of game scenarios
def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")
