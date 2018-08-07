from Card import Card
import random

"""
Defines a class of Hand, a single object of which represents a hand of cards
"""
class Hand:
    """
    One object of class hand represents a hand of cards
    """
    def __init__(self, numCardsInHand):
        """
        This is the constructor method for class Hand
        :param numCardsInHand: An int of the number of cards for that hand
        """
        self.numCardsInHand = numCardsInHand
        self.suits = ['c', 'd', 'h', 's']
        self.cardsInHand = []
        for card in range(numCardsInHand):
            randCard = self.hitMe()
            self.cardsInHand.append(randCard)


    def bjValue(self):
        """
        This method returns the blackjack value of a hand
        :return: returns an int of the sum of all of the blackjack values of the cards in that hand
        """
        bjValueInt = 0
        for card in self.cardsInHand:
            bjValueInt += card.bjValue()
        return bjValueInt

    def __str__(self):
        """
        This is the toString method of the Hand class
        :return: A string of all of the cards in a hand on seperate lines
        """
        returnStr = ""
        for card in self.cardsInHand:
            returnStr += card.__str__() + "\n"
        return returnStr


    def hitMe(self):
        """
        This method deals a card with a random suit and a random rank
        :return: A card with a random suit and a random rank
        """
        rank = random.randrange(1, 14)
        randSuit = random.randrange(4)
        suit = self.suits[randSuit]
        randCard = Card(rank, suit)
        return randCard

