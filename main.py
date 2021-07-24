import os
from Packages import Classes
from Packages import Functions


# Print an opening statement
os.system('cls')
print('\nWelcome to BlackJack! Get as close to 21 as you can without going over!\n\
Dealer hits until she reaches 17. Aces count as 1 or 11.\n\n')
# Set up the Player's chips
player_chips = Classes.Chips()

while True:

    # Create & shuffle the deck, deal two cards to each player
    deck = Classes.Deck()
    deck.shuffle()

    player_hand = Classes.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    dealer_hand = Classes.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())



    # Prompt the Player for their bet
    Functions.take_bet(player_chips)


    # Show cards (but keep one dealer card hidden)
    Functions.show_some(player_hand,dealer_hand)


    while Functions.playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        Functions.hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        if Functions.show:
            os.system('cls')
            Functions.show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            Functions.player_busts(player_hand,dealer_hand,player_chips)
            break


        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            Functions.hit(deck, dealer_hand)

            # Show all cards
        os.system('cls')
        Functions.show_all(player_hand,dealer_hand)

            # Run different winning scenarios
        if dealer_hand.value > 21:
            Functions.dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            Functions.dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            Functions.player_wins(player_hand,dealer_hand,player_chips)

        else:
            Functions.push(player_hand,dealer_hand)


        # Inform Player of their chips total
    print("\nPlayer's winnings stand at",player_chips.total)

        # Ask to play again
    new_game = input("Would you like to play another hand?(Y/N): ")

    if new_game.lower() == 'y' or new_game.lower() == 'yes':
        os.system('cls')
        Functions.playing = True
        continue


    break



