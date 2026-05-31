import random

while True:
    playerIn = True

    deck = [2,3,4,5,6,7,8,9,10]*4 + ['J','Q','K','A']*4
    player = []
    dealer = []

    def dealCard(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

    def total(turn):
        total_value = 0
        aces = 0

        for card in turn:
            if isinstance(card, int):
                total_value += card
            elif card in ['J','Q','K']:
                total_value += 10
            else:
                total_value += 11
                aces += 1

        while total_value > 21 and aces:
            total_value -= 10
            aces -= 1

        return total_value

    def revealDealer():
        return dealer[0]

    #starting cards
    for _ in range(2):
        dealCard(player)
        dealCard(dealer)

    #PLAYER
    while playerIn:
        print("\n----------------------")
        print(f"Dealer shows: {revealDealer()} + ?")
        print(f"Your hand: {player} → Total: {total(player)}")

        if total(player) >= 21:
            break

        choice = input("1: Stay\n2: Hit\n")

        if choice == "1":
            playerIn = False
        elif choice == "2":
            dealCard(player)
        else:
            print("Invalid input!")

    # DEALER
    while total(dealer) < 17:
        dealCard(dealer)

    #RESULTS
    print("\n======================")
    print(f"Dealer hand: {dealer} → {total(dealer)}")
    print(f"Your hand: {player} → {total(player)}")
    print("======================")

    if total(player) > 21:
        print(" YOU BUST ")
    elif total(dealer) > 21:
        print(" YOU WIN ")
    elif total(player) == total(dealer):
        print(" TIE")
    elif total(player) > total(dealer):
        print(" YOU WIN ")
    else:
        print(" DEALER WINS ")

    # MENU
    again = input("\nPlay again? (y/n): ")
    if again.lower() != 'y':
        print("Goodbye!")
        break