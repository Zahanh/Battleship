# This class should provide several utility methods to use throughout the program:
#     A method isNumeric will be provided for you.  You may utilize this method to determine 
#         if a String is a number.  If it is a number, it will return true, otherwise, it will return false. 
#         You do NOT need and should not modify this method.  It is free for you to use.
#     A method ‘promptUserForString’ that takes one parameter, a String that represents a prompt to 
#         print on the screen (e.g. “Enter your name”).  The method should then read a line of input from the keyboard and return as a String.
#     A method ‘promptUserForPositiveNumber’ that takes one parameter, a String that represents a 
#         prompt to print on the screen (e.g. “Enter a number”).  The method should then read a double 
#         from the keyboard.  If the number is less than or equal to 0, it should print a message and say 
#         “Amount cannot be negative.  Try again” and continue to loop.  If the number is positive, the method 
#         should return that number as a double.
#     A method ‘convertFromDollarsToCents’ that takes one parameter, a double that represents an 
#         mount of money in dollars (e.g. 3.57) and converts to a long (e.g. 357) and returns it.
#     A method ‘generateRandomInteger’ that takes two parameters, an integer representing the minimum 
#         value and an integer representing the maximum value of the range to generate a random number for 
#         and then return the number generated as an int.  For example, if you invoke generateRandomInteger(0,5), 
#         the method should return a random number from 0-5 (including both 0 and 5).

# You may add additional methods to this class as needed to assist or simplify your code. 

# At least 2 Unit tests must be written for EACH of the above methods in the BankUtility class:
    # isNumeric
    # convertFromDollarsToCents
    # generateRandomInteger

class BankUtility:
    def __init__(self) -> None:
        pass
    def promptUserForString(self,prompt):
        """
        takes one parameter, a String that represents a prompt to 
        print on the screen (e.g. “Enter your name”).  The method should then 
        read a line of input from the keyboard and return as a String.
        """
        # implement promptUserForString here
        str = input(prompt)
        return str # be sure to change this
    def promptUserForPositiveNumber(self,prompt):
        """
        takes one parameter, a String that represents a 
        prompt to print on the screen (e.g. “Enter a number”).  The method should then read a double 
        from the keyboard.  If the number is less than or equal to 0, it should print a message and say 
        “Amount cannot be negative.  Try again” and continue to loop.  If the number is positive, the method 
        should return that number as a double.
        """
        # implement promptUserForPositiveNumber here
        num = int(input(prompt))
        check = BankUtility().isNumeric(num) # verifying the number is numeric
        # if the input is not a number, it asks for the input again
        if check == False:
            while check == False:
                print("Not a number, Try again.")
                num = input(prompt)
        # if the number is less than 0 it asks for the input again
        if int(num) <= 0:
            while int(num) < 0:
                print("Number cannot be less than 0. Try again.")
                num = input(prompt)
        return float(num) # be sure to change this
    def generateRandomInteger(self,min,max):
        # 2 UNIT TEST REQUIRED
        """
        takes two parameters, an integer representing the minimum 
        value and an integer representing the maximum value of the range to generate a random number for 
        and then return the number generated as an int.  For example, if you invoke generateRandomInteger(0,5), 
        the method should return a random number from 0-5 (including both 0 and 5).
        """
        import random 
        # implement generateRandomInteger here
        self.randint = random.randint(min,max)
        return self.randint # be sure to change as needed
    def convertFromDollarsToCents(self,amount):
        # 2 UNIT TESTS REQUIRED
        """
        takes one parameter, a double that represents an 
        mount of money in dollars (e.g. 3.57) and converts to a long (e.g. 357) and returns it.
        """
        # implement convertFromDollarsToCents here
        cents = int(amount) * 100
        return cents # be sure to change as needed
    def isNumeric(self,numberToCheck):
        '''
        Checks if a given string is a number (long)
        This does NOT handle decimals.
        
        YOU DO NOT NEED TO CHANGE THIS METHOD
        THIS IS FREE FOR YOU TO USE AS NEEDED
        
        @param numberToCheck String to check
        @return true if the String is a number, false otherwise
        '''
        # 2 UNIT TESTS REQUIRED
        str(numberToCheck)
        if numberToCheck.isdigit():
            return True
        else:
            try:
                float(numberToCheck)
                return True
            except ValueError:
                return False
