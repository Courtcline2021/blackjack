import random

card_suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
card_list = ['Ace', '2', '3', '4', '5', '6', '7', '8','9', '10', 'King', 'Queen', 'Jack']
deck = [(card_suit) for suit in card_suit for card in card_list]

def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])
    
random.shuffle(deck)
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]

while True:
    player_score = sum(card_value(card) for card in player_card)
    dealer_score = sum(card_value(card) for card in dealer_card)
    print("Cards Player Has: ", player_card)
    print("Score of the Player: ", player_score)
    print("\n")
    choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower()
    if choice == "play":
        new_card = deck.pop()
        player_card.append(new_card)
    elif choice == "stop":
        break
    else:
        print("Invalid choice. PLease try again.")
        continue

    if player_score > 21 :
        print("Cards Dealer Has: ", dealer_card)
        print("Score of the Dealer: ", dealer_score)
        print("Cards Player Has: ", player_card)
        print("Dealer wins(Player Loss Because Player Score is exceeding 21)")
        break

while dealer_score < 17:
    new_card = deck.pop()
    dealer_card.append(new_card)
    dealer_score += card_value(new_card)

print("Cards Dealer Has: ", dealer_card)
print("Score of Dealer: ", dealer_score)
print("\n")

if dealer_score > 21:
    print("Cards Dealer Has: ", dealer_card)
    print("Score of Dealer Has: ", dealer_score)
    print("Cards Player Has: ", player_card)
    print("Score of the Player: ", player_score)
    print("Player wins (Dealer Loss Because Dealer Exceeds 21)")

elif player_score > dealer_score:
    print("Cards Dealer Has: ", dealer_card)
    print("Score of the Dealer: ", dealer_score)
    print("Cards Player Has: ",player_card)
    print("Score of the Player: ", player_score)
    print("Player wins (Player has High Score than Dealer)")

elif dealer_score > player_score:
    print("Cards Dealer Has: ", dealer_card)
    print("Score of the Dealer: ", dealer_score)
    print("Cards Player Has: ", player_card)
    print("Score of the Player: ", player_score)
    print("Dealer wins (Dealer has High Score than Player)")

else:
    print("Card Dealer Has: ", dealer_card)
    print("Score of Dealer: ", dealer_score)
    print("Cards Player Has: ", player_card)
    print("Score of Player: ", player_score)
    print("Its a Tie!")
