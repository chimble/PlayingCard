import random

class PlayingCard():

    values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits_list = ['hearts', 'clubs', 'diamonds', 'spades']

    def __init__(self, suit, value):
        self.suit = suit.title()
        self.value = value
    def __repr__(self):
        return str(self.value) + ' of ' + str(self.suit)
    def short(self):
        if self.value == 'ace':
            self.value = 'A'
        elif self.value == 'king':
            self.value = 'K'
        elif self.value == 'queen':
            self.value = 'Q'
        elif self.value == 'jack':
            self.value = 'J'
        print(str(self.value) + str(self.suit[0]).upper())
    def compair_cards(self, card2):
        return str(self.value) + ' of ' + str(self.suit) + " vs. " + str(card2.value) + ' of ' + str(card2.suit)
    def suits(self):
        return suits_list
    def values(self):
        return values_list

class Deck():

    def __init__(self):
        self.cards = []
        for value in PlayingCard.values_list:
            for suit in PlayingCard.suits_list:
                card = PlayingCard(suit, value)
                self.cards.append(card)
    def __repr__(self):
        return "".join(repr(self.cards))
    def __getitem__(self, index):
        return self.cards[index]
    def shuffle(self):
        random.shuffle(self.cards)
    # def deal(self):
    #     player_hand1 = self.cards[0]
    #     player_hand2 = self.cards[1]
    #     dealer_hand1 = self.cards[2]
    #     dealer_hand2 = self.cards[3]
    #     self.cards = self.cards[4:]
    #     return player_hand1, player_hand2
    def hit(self):
        next_card = self.cards[0]
        self.cards = self.cards[1:]
        return(next_card)
    def stand(self):
        pass


starting_deck = Deck()
player_hand_sum = 0
dealer_hand_sum = 0
print("welcome to blackjack. goodluck!")
print("here is your starting hand: ")
#starting_deck.shuffle()
print(starting_deck[0])
print(starting_deck[1])

print("here is the dealer's starting hand: {} and FACEDOWNCARD".format(starting_deck[2], starting_deck[3]))
player_hand_sum += starting_deck.hit().value
player_hand_sum += starting_deck.hit().value
dealer_hand_sum += starting_deck.hit().value
dealer_hand_sum += starting_deck.hit().value
print(dealer_hand_sum)

while player_hand_sum <=20:
    print("hand total is: {}".format(player_hand_sum))
    user_input = input("would you like to hit or stand? (H/S)")
    if user_input == 'h':
        print(starting_deck[0])
        player_hand_sum += starting_deck.hit().value
        if player_hand_sum >21:
            print("YOU LOSE")
        elif player_hand_sum == 21:
            print("YOU WIN")
    elif dealer_hand_sum >= player_hand_sum:
        print("YOU LOSE!")
        exit()
    else:
        while True:
            if dealer_hand_sum <=17 and dealer_hand_sum < player_hand_sum:
                print("dealer hits: {}".format(starting_deck[0]))
                dealer_hand_sum += starting_deck.hit().value
            elif dealer_hand_sum > 17 and dealer_hand_sum <= player_hand_sum:
                print("PLAYER WINS!")
                exit()
            elif dealer_hand_sum >= player_hand_sum and dealer_hand_sum <= 21:
                print("DEALER WINS!")
                exit()

















#abcd
