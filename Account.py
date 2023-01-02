# The Account class must store the following attributes:
#     Account number – a randomly generated 8-digit integer that cannot start with a 0
#     Owner First Name – a String that contains the first name of the account owner
#     Owner Last Name – a String that contains the last name of the account owner
#     Social Security Number – a String (not an integer) that contains the 9 digits of 
#         the account owner’s social security number (Note: do not use real social security numbers – 
#         use 999 or 000 as the first three digits for this program)
#     PIN – a String that represents the account owner’s 4-digit personal 
#         identification number – randomly generated upon account creation and may start with one or more zeroes
#     Balance – a number that represents the account balance in cents.   
#----------------------------------------------------------------------------------------------------
# At least 2 Unit tests must be written for EACH of the above methods in the Account class:
#     deposit
#     withdraw
#     isValidPIN

class Account:
    # add your attributes here
    def __init__(self,accnt_num,Fname,Lname,ssn,pin,balance) -> None:
        self.accntnum = accnt_num
        self.fname = Fname
        self.lname = Lname
        self.ssn = ssn
        self.pin = pin
        self.balance = balance

    # add methods as getters and setters for attributes
    def deposit(self,amount):# WORKS 
        """
        takes one parameter - an amount to deposit into the account as a "long".
        The method then adds the amount to the account balance and returns a "long" representing the new account balance
        """
        # implement deposit here
        #float(self.balance)
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        """
        takes one parameter - an amount to withdraw from the account as a "long".  
        The method then subtracts the amount from the account balance and returns a "long" representing the new account balance
        """
        # implement withdraw here
        float(self.balance) 
        self.balance -= float(amount)
        return self.balance # be sure to change this    
    def isValidPIN(self,pin):
        """
        takes one parameter, A String that represents a PIN.  The method then 
        compares the PIN that was passed in against the PIN that is on the account.  If the PINs match, it returns true, otherwise, it returns false.
        """
        # implement isValidPIN here
        if pin.isnumeric() == False:
            print("Null; invalid PIN")
            return False
        if self.pin == pin:
            return True
        else:
            return False  # be sure to change this   
    def toString(self):
        """
        Has no parameters but returns a String that contains the names and values of all of the attributes as follows.  
        This method should NOT print out anything but can be invoked as part of a System.out.println elsewhere.
        """
        return f""" 
============================================================
Account Number: {self.accntnum}
Owner First Name: {self.fname}
Owner Last Name: {self.lname}
Owner SSN: {self.ssn[0:3]}-{self.ssn[3:5]}-{self.ssn[5:]}
PIN: {self.pin}
Balance: ${float(self.balance):.2f}
============================================================"""
    def getAccountNumber(self):
        return self.accntnum
    def setAccountNumber(self,account):
        self.accntnum = account
    def getfname(self):
        return self.fname
    def setfname(self,fname):
        self.fname = fname
    def getlname(self):
        return self.lname
    def setlname(self,lname):
        self.lname = lname
    def getSSN(self):
        return self.ssn
    def setSSN(self,ssn):
        self.ssn = ssn
    def getPIN(self):
        return self.pin
    def setPIN(self,pin):
        self.pin = pin
    def getBalance(self):
        return float(self.balance)
    def setBalance(self,balance):
        self.balance = float(balance)

