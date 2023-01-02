# The BankManager class is where you will implement your ‘main’ method and start the program from. 

# The BankManager class should create an instance of a Bank object when the program runs and use that instance 
    # to manage the Accounts in the bank.  The BankManager class must implement the following methods:

# Your ‘main’ method.  The main method should display the menu and continually loop, performing the transactions, 
    # until the user enters 11 to exit the program.  If the user enters a number from 1-10, the program should call a method 
    # that implements the functionality for that transaction.  See details of each transaction at the end of this document.

# A method, ‘promptForAccountNumberAndPIN’ that takes one parameter, a Bank object that represents the bank. The method 
    # should prompt the user to enter an account number and then try to find a matching account with that account number in the bank.  
    # If an account cannot be found, the program should print “Account not found for account number: 12345678” (assuming the user entered 
    # 12345678) and return null.  If an account is found, the program should then prompt the user to enter a PIN.  If the PIN entered 
    # does not match the PIN for the account, then the program should print “Invalid PIN” and return null.  If the PIN matches, then the 
    # method should return the Account object.  This method will be needed for MOST (but not all) transactions.
import Account
import Bank
import BankUtility
import CoinCollector

class BankManager:
    def main():
        """
        The main method should display the menu and continually loop, performing the transactions, 
        until the user enters 11 to exit the program.  If the user enters a number from 1-10, the program should call a method 
        that implements the functionality for that transaction.  See details of each transaction at the end of this document.
        """
        # This is where you will implement your ‘main’ method and start
        # the program from.  The BankManager class should create an instance
        # of a Bank object when the program runs and use that instance to
        # manage the Accounts in the bank
        bank_is_on = True
        # BELOW IS CALLING THE MODULUE BANK, WITH CLASS BANK AND EXECUTING THE FUNCTION BELOW IT
            #https://www.geeksforgeeks.org/how-to-import-a-class-from-another-file-in-python/
        bank = Bank.Bank()
        bankutl = BankUtility.BankUtility()
        bank.generateRandomAccountInformation()
        while bank_is_on:
            print(f"""
            Please choose an option from 1 to 10; or 11 to quit.
            ---------------------------------------------------
            1: Open an Account
            2: Get account information and balance
            3: Change PIN
            4: Deposit money in account
            5: Transfer money between accounts
            6: Withdraw money from account
            7: ATM withdraw
            8: Deposit Change
            9: Close an account
            10: Add Monthly Interest to all accounts
            11: Exit
            ---------------------------------------------------
            """)
            user_input = input('')
            if user_input == '11':
                bank_is_on = False
                break
            elif user_input == '1':
                # Open an account
                print('OPEN ACCOUNT')
                accnt_num = str(bankutl.generateRandomInteger(10000000,99999999))
                fname = input('Enter Account Owners first name.\n')
                lname = input('Enter Account Owners last name.\n')
                ssn = input("Enter Account Owners SSN (9 digits).\n")
                if len(ssn) != 9:
                    while len(ssn) != 9:
                        print('Social Security Number must be 9 digits.')
                        ssn = input("Enter Account Owners SSN (9 digits).\n")
                pin = str(bankutl.generateRandomInteger(1000,9999))
                balance = float(0.00)
                bank.addAccountToBank(accnt_num,fname,lname,pin,ssn,balance)
            elif user_input == '2':
                # Get account information
                account = input('Please enter your account number.\n')
                account_info = bank.findAccount(account)
                if account_info != 'null':
                    print(Account.Account(account,account_info[0],account_info[1],account_info[2],account_info[3],account_info[4]).toString())
                else:
                    print(f'Account not found for account number {account}.')
            elif user_input == '3':
                accnt_num = input("Please enter your account number.\n")
                accnt_info = bank.findAccount(accnt_num)
                if accnt_info != 'null':           
                    fname = accnt_info[0]
                    lname = accnt_info[1]
                    ssn = accnt_info[2]
                    pin = accnt_info[3]
                    balance = accnt_info[4]
                    user_pin = input("Enter PIN.\n")
                    validPIN = Account.Account(accnt_num,fname,lname,ssn,pin,balance).isValidPIN(pin)
                    if validPIN:
                        if user_pin == pin:
                            new_pin1 = input("Please enter a new 4-digit pin.\n")
                            bankutl.isNumeric(new_pin1)
                            if len(new_pin1) != 4:
                                while len(new_pin1) != 4:
                                    print('PIN must be 4 digits, try again.')
                                    new_pin1 = input("Please enter a new 4-digit pin.\n")
                            new_pin2 = input("Please enter 4-digit pin again to confirm.\n")
                            if len(new_pin2) != 4:
                                while len(new_pin2) != 4:
                                    print('PIN must be 4 digits, try again.')
                                    new_pin2 = input("Please enter a new 4-digit pin.\n")
                                    bankutl.isNumeric(new_pin2)
                                    if new_pin1 != new_pin2:
                                        while new_pin1 != new_pin2:
                                            print('PINs do not match, try again.')
                                            new_pin1 = input("Please enter a new 4-digit pin.\n")
                                    bankutl.isNumeric(new_pin1)
                                    if len(new_pin1) != 4:
                                        while len(new_pin1) != 4:
                                            print('PIN must be 4 digits, try again.')
                                            new_pin1 = input("Please enter a new 4-digit pin.\n")
                                    new_pin2 = input("Please enter 4-digit pin again to confirm.\n")
                                    if len(new_pin2) != 4:
                                        while len(new_pin2) != 4:
                                            print('PIN must be 4 digits, try again.')
                                            new_pin2 = input("Please enter a new 4-digit pin.\n")
                                            bankutl.isNumeric(new_pin2)
                            bank.updateAccountPin(accnt_num,new_pin1)
                            print('PIN Updated.\n')
                        else:
                            print('Invalid PIN.\n')
                else: 
                    print(f"Account not found for account number: {accnt_num}.")
            elif user_input == '4':
                # deposit money in account
                accnt_num = input('Please enter your account number.\n')
                accnt_info = bank.findAccount(accnt_num)   
                if accnt_info != 'null':
                    user_pin = input("Please input your PIN.\n")        
                    fname = accnt_info[0]
                    lname = accnt_info[1]
                    ssn = accnt_info[2]
                    pin = accnt_info[3]
                    balance = float(accnt_info[4])
                    if user_pin == pin:
                        deposit = float(input('Please enter the deposit amount in dollars and cents.\n'))
                        if deposit > 0:
                            updated_balance = Account.Account(accnt_num,fname,lname,ssn,pin,balance).deposit(deposit)
                            new_balance = bank.updateAccountBalance(accnt_num,updated_balance)
                            print(f"New balance: {new_balance[5]}\n")
                        else: 
                            print('Invalid input, deposit cannot be negative.\n')
                    else:
                        print('Invalid PIN.\n') 
                else:
                    print(f'Account not found for account number {accnt_num}.\n')
            elif user_input == '5':
                #transfer money between accounts
                print("---------------------------------")
                print("Account to Transfer From\n")
                account_1 = input('Please input the first account number.\n')
                acc1 = bank.findAccount(account_1)
                if acc1 != 'null':
                    user_pin1 = input("Enter PIN.\n")
                    pin1 = acc1[3]
                    if user_pin1 == pin1:
                        fname1 = acc1[0]
                        lname1 = acc1[1]
                        ssn1 = acc1[2]
                        balance1 = float(acc1[4])
                        print("---------------------------------")
                        print("Account to Transfer To")
                        account_2 = input('Please input the second account number.\n')
                        acc2 = bank.findAccount(account_2)
                        if acc2 != 'null':  
                            user_pin2 = input("Enter PIN.\n")
                            #account_info = [fname,lname,ssn,pin,balance] is the return of .findAccount()
                            #-------------------------------
                            pin2 = acc2[3]
                            fname2 = acc2[0]
                            lname2 = acc2[1]
                            ssn2 = acc2[2]
                            balance2 = float(acc2[4])
                            if user_pin2 == pin2:
                                transfer = float(input(f'Please enter the amount youd like to transfer from {account_1} to {account_2}.\n'))
                                update_bal1 = Account.Account(account_1,fname1,lname1,ssn1,pin1,balance1).withdraw(transfer)
                                update_bal2 = Account.Account(account_2,fname2,lname2,ssn2,pin2,balance2).deposit(transfer)     
                                up_bal1 = bank.updateAccountBalance(account_1,update_bal1)
                                #Account.Account(account,fname,lname,ssn,pin,balance).toString()
                                up_bal2 = bank.updateAccountBalance(account_2,update_bal2)
                                print('Transfer Complete')
                                print(f"New balance in {account_1}: ${up_bal1[5]}.")
                                print(f"New balance in {account_2}: ${up_bal2[5]}.\n")
                            else:
                                print("Invalid PIN.\n")
                        else:
                            print(f'Account not found for account number {account_2}.')
                    else:
                        print("Invalid PIN.\n") 
                else:
                    print(f'Account not found for account number {account_1}.')        
            elif user_input == '6':
                # withdraw money
                accnt_num = input('Please enter your account number.\n')
                accnt_info = bank.findAccount(accnt_num)
                if accnt_info != 'null':
                    fname = accnt_info[0]
                    lname = accnt_info[1]
                    ssn = accnt_info[2]
                    pin = accnt_info[3]
                    balance = float(accnt_info[4])
                    user_pin = str(input('Please enter your PIN.\n'))
                    if user_pin == pin:
                        withdraw = float(input("Please enter the amount you'd like to widthdraw.\n"))
                        if withdraw > 0:
                            if withdraw > balance:
                                    print(f'Insuffcient funds in account {accnt_num}.\n')
                            elif withdraw <= balance:
                                updated_balance = Account.Account(accnt_num,fname,lname,ssn,pin,balance).withdraw(withdraw)
                                bank.updateAccountBalance(accnt_num,updated_balance)
                                print(f"${withdraw} has been withdrawn from account {accnt_num}.\n")
                            else: 
                                print('Invalid input, value cannot be negative.\n')
                    else:
                        print('Invalid PIN')
                else:
                    print(f'Account not found for account number {accnt_num}.\n')
            elif user_input == '7':
                """

                the program should prompt the user to enter their account number and then the PIN for the account number.  See the error 
                messages section for the messages to display if the account number or PIN are invalid.  
                
                If the account number is valid and the PIN matches the PIN on the account, the program should prompt the user to enter 
                the amount to withdraw in whole dollars as a multiple of $5 as shown below.  

                If the amount is less than 5, greater than 1000, or not divisible by 5, print a message that says “Invalid amount. Try again.”  
                Otherwise, calculate the number of $20 bills, $10 bills and $5 required to equal the amount withdrawn, print the 
                amounts on the screen and then call the withdraw method on the Account. 

                """
                bankutl = BankUtility.BankUtility()
                accnt_num = input("Please input your account number.\n")
                account_info = bank.findAccount(accnt_num)
                if account_info != 'null':
                    user_pin = input("Please enter your PIN.\n")
                    pin = account_info[3]
                    if pin == user_pin:
                        withdraw = input("Please enter the amount to widthdraw in a multiple of $5 (limit $1000).\n")
                        while bankutl.isNumeric(withdraw) == False:
                            print('Invalid Amount. Try Again.')
                            withdraw = input("Please enter the amount to widthdraw in a multiple of $5.\n")
                        if bankutl.isNumeric(withdraw) == True:
                            withdraw = float(withdraw)
                            # below is the a while loop to make sure the amount is within the parameters
                            while float(withdraw) < 5 or float(withdraw) > 1000 or float(withdraw) % 5 != 0:
                                print('Invalid Amount. Try Again.')
                                withdraw = input("Please enter the amount to widthdraw in a multiple of $5.\n")
                            if float(withdraw) > 5 and float(withdraw) < 1000 and float(withdraw) % 5 == 0:
                                bills = [20,10,5]
                                a = int(withdraw)
                                b = []
                                j = 0
                                # below is a for loop to split up the inputted withdrawl into 20s,10s,5s
                                for i in bills:
                                    b.append(a//i)
                                    a = a - (b[j] * i)
                                    j+=1
                                print(f"""
Number of $20 bills dispensed: {b[0]} 
Number of $10 bills dispensed: {b[1]} 
Number of $5 bills dispensed: {b[2]}\n""")
                                # account_info = [fname,lname,ssn,pin,balance] output of .findAccount()
                                account_info = bank.findAccount(accnt_num)
                                updated_info = Account.Account(accnt_num,account_info[0],account_info[1],account_info[2],account_info[3],float(account_info[4])).withdraw(withdraw)
                                new_acc = bank.updateAccountBalance(accnt_num,updated_info)
                                print(f'Updated balance: ${new_acc[5]:2f}.')
                            else:
                                print("Invalid amount.\n")
                    else:
                        print('Invalid PIN.\n')
                else:
                    print(f'Account not found for account number {accnt_num}.\n')
            elif user_input == '8':
                """
                For Deposit change, the program should prompt the user to enter their account number and then the PIN for 
                the account number.  See the error messages section for the messages to display if the account number or PIN 
                are invalid.  If the account number is valid and the PIN matches the PIN on the account, the program should prompt 
                the user to enter a String representing a set of coins as shown below.  
                    P - represents a penny (1 cent)
                    N - represents a nickel (5 cents)
                    D - represents a dime (10 cents)
                    Q - represents a quarter (25 cents)
                    H - represents a half-dollar (50 cents)
                    W - represents a whole dollar (100 cents)
                If any characters are invalid coins (e.g. X), the program should print “Invalid coin: X”.  Otherwise, convert the 
                String into the appropriate number of cents to a long and call the deposit method on the Account. Then the program 
                should print the updated balance of the account.

                """
                print("---------------DEPOSIT CHANGE---------------")
                account_num = input("Please Enter your Account Number.\n")
                account_info = bank.findAccount(account_num)
                if account_info != 'null':
                    user_pin = input("Please Enter your PIN.\n")
                    if user_pin == account_info[3]:
                        change = input('Please enter the change youd like to input (i.e. PNDQHW)\n').upper()
                        valid_change = ['P','N','D','Q','H','W']
                        b = []
                        for i in change:
                            if i not in valid_change:
                                print(f'{i} not a valid coin and is not counted.')
                                print(i)
                            elif i in valid_change:
                                b.append(i)
                        coins = ""
                        for i in b:
                            coins +=i
                        total_change = CoinCollector.CoinCollector(coins).parseChange()
                        print(f"Total change deposited: ${total_change:.2f}.")
                        deposit = Account.Account(account_num, account_info[0], account_info[1], account_info[2], account_info[3], float(account_info[4])).deposit(total_change)
                        bank.updateAccountBalance(account_num,deposit)
                    else:
                        print('Invalid PIN.\n')
                else:
                    print(f'Account not found for account number {account_num}.\n')
            elif user_input == '9':
                # close an account
                account = input('Please enter the account number youd like to close.\n')
                account_info = bank.findAccount(account)
                if account_info != 'null':
                    pin = input('Enter PIN.\n')
                    bank.removeAccountFromBank(account,pin)
                    print(f'Account {account} closed.')
                else:
                    print(f'Account not found for account number {account}.')
            elif user_input == '10':
                """
                the program should prompt the user to enter an annual interest rate.  The program should then calculate a monthly interest 
                payment based on the annual interest rate for each account based on its current balance and then deposit that amount into that account.
                
                In the example below, the first account had an original balance of $500, the second account had an original balance of $2500.
                
                Enter annual interest rate percentage (e.g. 2.75 for 2.75%):
                1.25
                Deposited interest: $0.52 into account number:47534813, new balance:$500.52
                Deposited interest: $2.60 into account number:36069443, new balance:$2,502.60                
                """
                apr = input("Please enter the annual interest rate.\n")
                if bankutl.isNumeric(apr) == False:
                    i = 0
                    while bankutl.isNumeric(apr) == False:
                        print('Invalid APR amount, try again.\n')
                        i+= 1
                        if i > 100:
                            break
                else:
                    apr = eval(apr)
                    bank.addMonthlyInterest(apr)
            else:
                print('Invalid option choice.\n')
    # @staticmethod    
    # def promptForAccountNumberAndPIN(bank_object):
        # BANK Object: 
            # 0 = account number
            # 1 = fname
            # 2 = lname 
            # 3 = ssn
            # 4 = pin
            # 5 = balance

        # A method, ‘promptForAccountNumberAndPIN’ that takes one parameter, a Bank object that represents the bank. The method 
            # should prompt the user to enter an account number and then try to find a matching account with that account number in the bank.  
            # If an account cannot be found, the program should print “Account not found for account number: 12345678” (assuming the user entered 
            # 12345678) and return null.  If an account is found, the program should then prompt the user to enter a PIN.  If the PIN entered 
            # does not match the PIN for the account, then the program should print “Invalid PIN” and return null.  If the PIN matches, then the 
            # method should return the Account object.  This method will be needed for MOST (but not all) transactions.
        accnt_num = input('Please enter your account number.\n')
        account_Info = Bank.Bank().findAccount(accnt_num)
        if account_Info == "null":
            print(f"Account information not found for account number: {accnt_num}.")
            return "null"
        else:
            # below is the output of .findAccount()
            # account_info = [fname,lname,ssn,pin,balance]
            user_pin = input("Enter your PIN.\n")
            if user_pin == account_Info[3]:
                return Account.Account(accnt_num,account_Info[0],account_Info[1],account_Info[2],account_Info[3],account_Info[4]).toString()
            else:
                print('Invalid PIN')
                return 'null'
    
if __name__ == '__main__':
    BankManager.main()