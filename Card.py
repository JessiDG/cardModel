"""
	Defines a class Card. A single object of card takes an int for a rank and a string for a suit
"""
class Card:
    """
        One object of this class stores one card's suit and rank
    """
    def __init__ (self, rank, suit):
        """
            Sets the object's suit and rank, testing to ensure they fit requirements; if not, set them to defaults
        """
        Card.suitsToWords = {'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts', 's': 'Spades'}
        Card.rankToWords = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
                            7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen',
                            13: "King"}
        if type(rank) is not int or type(suit) is not str:
            raise TypeError
        if rank not in Card.rankToWords.keys() or suit not in Card.suitsToWords.keys():
            raise ValueError

        self.rank = rank
        self.suit = suit

    def getRank(self):
        """
            returns the rank
        """
        return self.rank


    def getSuit(self):
        """
            returns the suit
        """
        return self.suit


    def bjValue(self):
        """
            returns the black jack value of the card, which is 10 for all face cards and the rank for all other cards
        """
        cardRank = self.getRank()
        if cardRank <= 10:
            return cardRank
        else:
            return 10


    def __str__(self):
        """
            returns a sentence that tells the rank and suit of the object
        """
        return Card.rankToWords[self.rank] + " of " + Card.suitsToWords[self.suit]


"""
     Creates 5 Card objects and calls methods on them for testing purposes
"""
if __name__ == "__main__":
    try:
        card1 = Card(3, 'c')
        print(card1)
        print(card1.getRank())
        print(card1.getSuit())
        print(card1.bjValue())
        print()
        #
        card3 = Card(2, 'd')
        print(card3)
        print(card3.getRank())
        print(card3.getSuit())
        print(card3.bjValue())
        print()
        #
        card5 = Card(11, 's')
        print(card5)
        print(card5.getRank())
        print(card5.getSuit())
        print(card5.bjValue())

        card4 = Card(12, 12)
        print(card4)
        print(card4.getRank())
        print(card4.getSuit())
        print(card4.bjValue())
        print()

    except TypeError:
        print("Type: You can't set the rank to anything other than an int or the suit to anything but a string")
    try:
        card4 = Card(12, 'l')
        print(card4)
        print(card4.getRank())
        print(card4.getSuit())
        print(card4.bjValue())
        print()

        card2 = Card('2', 's')
        print(card2)
        print(card2.getrank())
        print(card2.getSuit())
        print(card2.bjValue())
        print()

        card2 = Card(-1, 's')
        print(card2)
        print(card2.getrank())
        print(card2.getSuit())
        print(card2.bjValue())
        print()
    except ValueError:
        print("Value error: The only acceptable suits are c, d, h, s and ranks must be between 1-13")
    finally:
        print("That's the end of the tests! ")
