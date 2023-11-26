#Olivia Booth
#CIS261
#Week 8 Deck of Cards Lab

import random

class Card:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
        
class Deck:
    def __init__(self):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.reset()
        
    def reset(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
    
    def count(self):
        return len(self.deck)


#Code below

 
print("Welcome to the Card Dealer")
print("\nI have shuffled a deck of 52 cards.")

deck = Deck()

deck.shuffle()

AmountOfCardsToDeal = int(input("\nHow many cards do you want?:  "))
dealt_cards = []
  
for _ in range(AmountOfCardsToDeal):
   card = deck.deal()
   if card is not None:
      dealt_cards.append(f"{card.rank} of {card.suit}")
   else:
      print("No more cards in the deck.")
if dealt_cards:
    print(f"\nDealt card(s): ")
    for card in dealt_cards:
        print(card)

count = deck.count()
print(f"\nRemaining cards in the deck: {count}")

print("\nGood luck!")
