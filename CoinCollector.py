# This class represents a machine that can count change and has one method:

#     A method called ‘parseChange’ that takes one parameter, a String that represents a set of coins/change.  
#     The method must look at each character in the String and calculate the amount it represents in cents as a 
#     ‘long’ (number) and return it.  The following characters represent valid coins:
#         ‘P’ represents a penny (1 cent)
#         ‘N’ represents a nickel (5 cents)
#         ‘D’ represents a dime (10 cents)
#         ‘Q’ represents a quarter (25 cents)
#         ‘H’ represents a half-dollar (50 cents)
#         ‘W’ represents a whole dollar (100 cents)
# At least 3 Unit tests must be written for the parseChange method

class CoinCollector:
    def __init__(self,coins) -> None:
        self.pennies = coins.count('P') * 0.01
        self.nickel = coins.count('N') * 0.05
        self.dime = coins.count("D") * 0.10
        self.quarters = coins.count("Q") * 0.25
        self.half = coins.count('H') * 0.50
        self.whole = coins.count('W') * 1.00

    def parseChange(self):
        # implement parseChange here
        # 3 UNIT TESTS REQUIRED
        total = self.pennies + self.nickel + self.dime + self.quarters + self.half + self.whole
        return total