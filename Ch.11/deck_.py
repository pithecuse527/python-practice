import random

class Card:
    suitNames = ['Club', 'Diamond', 'Heart', 'Spade']
    rankNames = [None, 'Ace', 'Jack', 'Queen', 'King'] +\
                [ str(x) for x in range(2,11)]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return Card.suitNames[self.suit] + " " +\
               Card.rankNames[self.rank]

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        lst = [str(card) for card in self.cards]
        return str(lst)

class Person:
    def __init__(self):
        self.cards = []
    def getCard(self, deck):
        card = random.choice(deck.cards)
        self.cards.append(card)
    def __str__(self):
        lst = [str(card) for card in self.cards]
        return str(lst)

deck = Deck()
#print(deck)

person1 = Person()

for i in range(10):
    person1.getCard(deck)
print(person1)


