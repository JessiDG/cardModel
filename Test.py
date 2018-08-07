import unittest
from Card import Card
from Hand import Hand

import random

class Test(unittest.TestCase):
    """
    One object of this class tests the Hand class
    """

    def testHand(self):
        """
        This method allows us to test class Hand
        """

        print("Original test")
        h1 = Hand(3)
        print(h1)
        print(h1.bjValue())
        h1.hitMe()
        print(h1)
        print(h1.bjValue())
        h2 = Hand(2)
        print(h2)
        print(h1)  # to make sure that the creation of h2 didn't effect h1

        print("More robust test")
        for test in range(20):
            size = random.randrange(-2, 20)
            tester = Hand(size)
            print("---------A hand of size: " + str(size) + "---------")
            print(tester)
            print("This hand's blackjack value: " + str(tester.bjValue()))
            print()




if __name__ == "__main__":
    unittest.main(verbosity=2)

"""Output

testHand (__main__.Test) ... Original test
Seven of Diamonds
Eight of Spades
Ace of Clubs

16
Seven of Diamonds
Eight of Spades
Ace of Clubs

16
Two of Diamonds
Two of Clubs

Seven of Diamonds
Eight of Spades
Ace of Clubs

More robust test
---------A hand of size: 0---------

This hand's blackjack value: 0

---------A hand of size: -2---------

This hand's blackjack value: 0

---------A hand of size: 11---------
Ten of Hearts
Five of Diamonds
Four of Hearts
Six of Diamonds
Two of Spades
Four of Diamonds
Ten of Clubs
Ace of Diamonds
Jack of Hearts
Five of Hearts
Four of Hearts

This hand's blackjack value: 61

---------A hand of size: 9---------
Four of Clubs
Eight of Spades
Three of Hearts
Nine of Diamonds
Jack of Hearts
Ace of Clubs
Seven of Clubs
Five of Hearts
Six of Hearts

This hand's blackjack value: 53

---------A hand of size: 18---------
Six of Spades
Ace of Hearts
Five of Spades
Three of Diamonds
Nine of Clubs
Five of Spades
Ace of Diamonds
Queen of Clubs
Seven of Hearts
Five of Clubs
King of Hearts
Queen of Hearts
Eight of Spades
Six of Clubs
Ten of Diamonds
Jack of Clubs
Eight of Spades
Queen of Hearts

This hand's blackjack value: 124

---------A hand of size: 9---------
Seven of Hearts
Five of Hearts
Seven of Clubs
Queen of Clubs
Four of Hearts
Two of Clubs
Ten of Hearts
Ace of Spades
Ace of Spades

This hand's blackjack value: 47

---------A hand of size: 3---------
Three of Hearts
Queen of Diamonds
Queen of Hearts

This hand's blackjack value: 23

---------A hand of size: 18---------
Three of Clubs
Ace of Diamonds
Three of Diamonds
Four of Diamonds
Three of Spades
Queen of Clubs
Eight of Spades
Five of Spades
Two of Clubs
Jack of Hearts
Ace of Spades
Six of Spades
Ten of Hearts
Five of Diamonds
Five of Spades
Three of Diamonds
Five of Spades
Four of Diamonds

This hand's blackjack value: 88

---------A hand of size: 14---------
Queen of Spades
Jack of Hearts
Ten of Hearts
Jack of Hearts
Ace of Diamonds
Five of Spades
Ten of Diamonds
Queen of Spades
Nine of Diamonds
Seven of Clubs
Ten of Hearts
Two of Hearts
Two of Hearts
Eight of Clubs

This hand's blackjack value: 104

---------A hand of size: -2---------

This hand's blackjack value: 0

---------A hand of size: 8---------
Ace of Hearts
Ten of Clubs
Jack of Hearts
King of Hearts
Four of Clubs
Ace of Diamonds
King of Hearts
Ace of Diamonds

This hand's blackjack value: 47

---------A hand of size: 7---------
Ace of Clubs
Two of Hearts
Queen of Spades
Ten of Spades
Seven of Hearts
Three of Clubs
Nine of Spades

This hand's blackjack value: 42

---------A hand of size: 14---------
Jack of Hearts
Seven of Clubs
Five of Hearts
Ten of Hearts
Nine of Clubs
Six of Diamonds
Seven of Diamonds
Four of Diamonds
Six of Diamonds
Four of Diamonds
Seven of Diamonds
Three of Clubs
Ten of Hearts
Eight of Diamonds

This hand's blackjack value: 96

---------A hand of size: 13---------
Two of Diamonds
Six of Clubs
Eight of Hearts
Four of Clubs
Nine of Hearts
Three of Diamonds
Queen of Diamonds
King of Clubs
Two of Diamonds
Two of Hearts
Queen of Hearts
Queen of Clubs
Ten of Diamonds

This hand's blackjack value: 86

---------A hand of size: 5---------
Queen of Spades
Four of Spades
Four of Diamonds
Eight of Spades
Six of Spades

This hand's blackjack value: 32

---------A hand of size: 15---------
Ace of Spades
Queen of Diamonds
King of Spades
Nine of Diamonds
Three of Diamonds
Three of Spades
Eight of Spades
Seven of Spades
Five of Diamonds
Ace of Spades
Five of Diamonds
Jack of Clubs
Seven of Spades
Nine of Clubs
Seven of Diamonds

This hand's blackjack value: 95

---------A hand of size: 19---------
Five of Spades
King of Spades
Three of Clubs
Three of Hearts
King of Clubs
King of Clubs
Eight of Diamonds
Queen of Clubs
Jack of Clubs
Jack of Clubs
Queen of Diamonds
Jack of Diamonds
Four of Hearts
Nine of Diamonds
Five of Spades
Jack of Clubs
Seven of Clubs
Jack of Hearts
Ace of Hearts

This hand's blackjack value: 145

---------A hand of size: 19---------
Four of Spades
Eight of Hearts
Seven of Clubs
Three of Spades
Queen of Diamonds
Six of Diamonds
Jack of Diamonds
Ace of Hearts
Ace of Clubs
Seven of Spades
Three of Hearts
Jack of Hearts
Ace of Spades
Six of Hearts
Three of Spades
Two of Diamonds
Seven of Diamonds
Two of Diamonds
King of Diamonds

This hand's blackjack value: 101

---------A hand of size: 17---------
Two of Diamonds
Seven of Hearts
Ten of Clubs
King of Spades
King of Diamonds
Jack of Hearts
Four of Clubs
Seven of Hearts
Queen of Spades
Two of Hearts
Jack of Diamonds
Six of Hearts
Nine of Hearts
Four of Diamonds
Eight of Clubs
King of Clubs
Eight of Hearts

This hand's blackjack value: 127

---------A hand of size: 8---------
Six of Clubs
Jack of Hearts
Seven of Spades
Three of Hearts
King of Hearts
Three of Diamonds
Three of Hearts
Ten of Clubs

This hand's blackjack value: 52

ok

----------------------------------------------------------------------
Ran 1 test in 0.003s

OK

Process finished with exit code 0
"""