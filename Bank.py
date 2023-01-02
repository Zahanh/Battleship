# The Bank class must store the following attributes
#     An array of Accounts 
#     The array represents all the accounts in the bank.
#     The bank must support up to 100 accounts when submitted
#     A constant that represents the number of accounts supported by the bank 
        # (you should set this to a low value during development to help test running out of accounts)
#----------------------------------------------------------------------------------------------------------------
# The Bank class must implement the following methods:
#     A method, ‘addAccountToBank’, that takes one parameter, an Account object, to add to the 
        # array of accounts in the Bank.  The method should iterate through all the accounts in the 
        # array until it finds an empty/null index.  It should then add the account to that index in the 
        # array to represent a new account that was opened and return true to indicate the account was successfully 
        # added.  If there is no more room for the Bank to accept any more accounts (i.e. there are already 100 
        # accounts in the array). The method should print a message saying, “No more accounts available” and 
        # should return false.
#     A method, ‘removeAccountFromBank’, that takes one parameter, an Account object, to remove from 
        # the accounts array.  The method should iterate through all the accounts in the array and try to match 
        # the account provided to the accounts in the Bank by the account number.  If the account number of the 
        # provided account matches the account number of the Account in the array, then that index of the array 
        # should be marked ‘null’ to indicate that the account is closed and no longer exists.
#     A method, ‘findAccount’ that takes one parameter, an int representing the account number.  
        # The method should iterate through all the accounts in the array and try to match the account 
        # number provided to the accounts in the Bank by the account number.  If a match is found, the Account 
        # object should be returned.  If an account with the provided account number does not exist, the method 
        # should return ‘null’ to indicate a matching Account was not found.
#     (Optional for EXTRA CREDIT): A method, ‘addMonthlyInterest’ that takes one parameter, a ‘double’ 
        # representing the percentage of the annual interest rate (e.g. if the rate is 2.5%, the value entered 
        # would be 2.5).  The method should then iterate through all the accounts in the array and deposit a monthly 
        # interest payment into every account.  The monthly interest for the account is calculated by taking the 
        # current balance and multiplying a monthly interest rate.
# At least 2 Unit tests must be written for EACH of the above methods in the Account class:
    #     addAccountToBank
    #     removeAccountFromBank
    #     findAccount
    #     addMonthlyInterest (only if you attempt the extra credit)
import Account
import BankUtility

class Bank:
    def __init__(self) -> None:
        # creating a bank object which stores all of the account information
        self.count = 100
        self.bank = [
            ['']*self.count,
            ['']*self.count,
            ['']*self.count,
            ['']*self.count,
            ['']*self.count,
            ['']*self.count]
        # 0 = account number
        # 1 = fname
        # 2 = lname
        # 3 = ssn
        # 4 = pin
        # 5 = balance
        
    def addAccountToBank(self,account,fname,lname,pin,ssn,balance):# WORKS
        """
        takes one parameter, an Account object, to add to the 
        array of accounts in the Bank.  The method should iterate through all the accounts in the 
        array until it finds an empty/null index.  It should then add the account to that index in the 
        array to represent a new account that was opened and return true to indicate the account was successfully 
        added.  If there is no more room for the Bank to accept any more accounts (i.e. there are already 100 
        accounts in the array). The method should print a message saying, “No more accounts available” and 
        should return false.
        """
        # implement addAccountToBank here
        if "" in self.bank[0]:
            account_index = self.bank[0].index('')
            if account not in self.bank[0]:
                self.bank[0][account_index] = account # adding the account number
            else:
                while account in self.bank[0]:
                    account = BankUtility.BankUtility().generateRandomInteger(10000000,99999999)
            self.bank[4][account_index] = pin # creating a pin (3 digit)
            self.bank[1][account_index] = fname   
            self.bank[2][account_index] = lname  
            self.bank[3][account_index] = ssn # 9 digits
            self.bank[5][account_index] = balance  
            print(Account.Account(account,fname,lname,ssn,pin,balance).toString())
            return True 
        else:
            print(f'No more accounts available.')
            return False
    def removeAccountFromBank(self,account,pin):# WORKS
        """
        takes one parameter, an Account object, to remove from 
        the accounts array.  The method should iterate through all the accounts in the array and try to match 
        the account provided to the accounts in the Bank by the account number.  If the account number of the 
        provided account matches the account number of the Account in the array, then that index of the array 
        should be marked "null" to indicate that the account is closed and no longer exists.
        """
        # implement removeAccountFromBank here
        if account in self.bank[0]:
            if pin in self.bank[4]:
                i = self.bank[0].index(account)
                self.bank[0][i] = ''
                self.bank[4][i] = ''
                self.bank[1][i] = ''
                self.bank[2][i] = ''
                self.bank[3][i] = ''
                self.bank[5][i] = ''
                return 'null'
            else: 
                print('PIN invalid.\n')
                return False
    def findAccount(self,accountNumber):# WORKS
        """
        takes one parameter, an int representing the account number.  
        The method should iterate through all the accounts in the array and try to match the account 
        number provided to the accounts in the Bank by the account number.  If a match is found, the Account 
        object should be returned.  If an account with the provided account number does not exist, the method 
        should return "null" to indicate a matching Account was not found.
        """
        #accountNumber = int(accountNumber)
        if accountNumber in self.bank[0]:
            i = self.bank[0].index(accountNumber)
            fname = self.bank[1][i]
            lname = self.bank[2][i]
            ssn = self.bank[3][i]
            pin = self.bank[4][i]
            balance = self.bank[5][i]
        else: 
            return 'null'
        account_info = [fname,lname,ssn,pin,balance]
        return account_info 
    def addMonthlyInterest(self,percent):
        """
        takes one parameter, a "double" 
        representing the percentage of the annual interest rate (e.g. if the rate is 2.5%, the value entered 
        would be 2.5).  The method should then iterate through all the accounts in the array and deposit a monthly 
        interest payment into every account.  The monthly interest for the account is calculated by taking the 
        current balance and multiplying a monthly interest rate.
        """
        # EXTRA CREDIT
        if type(percent) == int or type(percent) == float:
            for i in self.bank[5]:
                if i in self.bank[5] and i != '':
                    percent = percent / 100
                    j = self.bank[5].index(i) # finding the index for each value
                    account = self.bank[0][j]
                    old_balance = float(self.bank[5][j])
                    interest = (float(i) * percent) / 12 # calculating the monthly interest 
                    self.bank[5][j] = float(old_balance) + interest
                    print("---------------------------------------------------------------------")
                    print(f"Deposited interest: ${round(interest,2)} into account number:{account}, old balance:${round(old_balance,2)} new balance:${round(float(self.bank[5][j]),2)}.\n")
                    print("---------------------------------------------------------------------") 
                    return True
            else:
                return False
        else:
            return False   
    def generateRandomAccountInformation(self):
        bankutl = BankUtility.BankUtility()
        i = 0
        num_accounts = bankutl.generateRandomInteger(0,self.count)
        while i < num_accounts:
            num = bankutl.generateRandomInteger(1000,9999) # generating a random number for the account information
            # below is making sure that there are no duplicate account numbers
            for j in self.bank[0]:
                while j == num:
                    if j == num:
                        num = bankutl.generateRandomInteger(1000,9999)
            self.bank[0].pop(0) # removing the top element of the stack
            self.bank[0].append(str(num)) # adding on to the bottom of the stack
            
            pin = bankutl.generateRandomInteger(100,999)
            for z in self.bank[4]:
                while z == pin:
                    if z == pin:
                        pin = bankutl.generateRandomInteger(100,999)
            self.bank[4].pop(0)
            self.bank[4].append(str(pin))

            fname = 'N/a'
            self.bank[1].pop(0)
            self.bank[1].append(fname)

            lname = 'N/a'
            self.bank[2].pop(0)
            self.bank[2].append(lname)

            ssn_start = 999
            ssn = bankutl.generateRandomInteger(100000,999999)
            ssn = str(ssn_start) + str(ssn)
            for z in self.bank[3]:
                while z == ssn:
                    if z == ssn:
                       ssn = bankutl.generateRandomInteger(100000,999999)
            self.bank[3].pop(0)
            self.bank[3].append(str(ssn))

            balance = bankutl.generateRandomInteger(0,1000)
            self.bank[5].pop(0)
            self.bank[5].append(str(balance))
            i+=1
    def updateAccountBalance(self,account,balance):
        """
        Method to update the account information in the bank. Takes the account information as the input
        and updates the information of the given index in the bank.
        """
        # Below is if statement to find the index of the given account number
        if account in self.bank[0]:
            i = self.bank[0].index(account)
            fname = self.bank[1][i]
            lname = self.bank[2][i]
            ssn = self.bank[3][i]
            pin = self.bank[4][i]
            self.bank[5][i] = balance
            Account.Account(account,fname,lname,ssn,pin,balance).toString()
            return [account,fname,lname,ssn,pin,balance]
        else:
            return 'null'
    def updateAccountPin(self,account,new_pin):
        """
        Method to update the account information in the bank. Takes the account information as the input
        and updates the information of the given index in the bank.
        """
        # Below is if statement to find the index of the given account number
        if account in self.bank[0]:
            i = self.bank[0].index(account)
            fname = self.bank[1][i]
            lname = self.bank[2][i]
            ssn = self.bank[3][i]
            balance = self.bank[5][i]
            self.bank[4][i] = new_pin
            return self.bank[4][i]
        else:
            return 'null'
        