# Bank Class ------------------------------------------------------
# At least 2 Unit tests must be written for EACH of the above methods in the Bank class:
    #     addAccountToBank
    #     removeAccountFromBank
    #     findAccount
    #     addMonthlyInterest (only if you attempt the extra credit)
# Account Class ----------------------------------------------------
# At least 2 Unit tests must be written for EACH of the above methods in the Account class:
    # deposit
    # withdraw
    # isValidPIN
# Bank Utility -----------------------------------------------------
# At least 2 Unit tests must be written for EACH of the above methods in the BankUtility class:
    # isNumeric
    # convertFromDollarsToCents
    # generateRandomInteger
# Coin Collector ----------------------------------------------------
# At least 3 Unit tests must be written for the parseChange method
import Bank
import BankUtility
import Account
import CoinCollector
import unittest

class TestHastings(unittest.TestCase):
    def test_addAccountToBank(self):
        """
        Testing add account to bank
        """
        account_number = 0
        fname = ''
        lname = ''
        pin = ''
        ssn = ''
        balance = 0
        self.assertTrue(Bank.Bank().addAccountToBank(account_number, fname,lname,pin,ssn,balance))
    def test_removeAccountFromBank(self):
        """
        Testing remove account from bank
        """
        pin = ''
        a_num1 = '123'
        a_num2 = ''
        self.assertFalse(Bank.Bank().removeAccountFromBank(a_num1,pin))
        self.assertTrue(Bank.Bank().removeAccountFromBank(a_num2,pin))
    def test_findAccount(self):
        """
        Testing function find account
        """
        account1 = ''
        account2 = '2'
        self.assertEqual(Bank.Bank().findAccount(account2),'null')
        self.assertTrue(Bank.Bank().findAccount(account1))
    def test_addMonthlyInterest(self):
        """
        Testing monthly interest method
        """
        percent_1 = 1.00
        percent_2 = 'a'
        self.assertFalse(Bank.Bank().addMonthlyInterest(percent_2))
        self.assertFalse(Bank.Bank().addMonthlyInterest(percent_1)) # returns false because it does not see anything in Bank

    def test_deposit(self):
        acc = '2363'
        fname = 'test'
        lname = 'test'
        pin = '2321'
        ssn = '23127'
        balance = 12.35

        self.assertEqual(Account.Account(acc,fname,lname,ssn,pin,balance).deposit(1.00),13.35)
        self.assertEqual(Account.Account(acc,fname,lname,ssn,pin,balance).deposit(1.65),14.00)
    def test_withdraw(self):
        acc = '2363'
        fname = 'test'
        lname = 'test'
        pin = '2321'
        ssn = '23127'
        balance = 122.74

        self.assertEqual(Account.Account(acc,fname,lname,ssn,pin,balance).withdraw(2.74),120)
        self.assertAlmostEqual(Account.Account(acc,fname,lname,ssn,pin,balance).withdraw(120),2.74) #rounded due to a small error in the computation
    def test_ValidPIN(self):
        acc = '2363'
        fname = 'test'
        lname = 'test'
        ssn = '23127'
        balance = 122.74
        pin1 = 'a'
        pin2 = '1234'

        self.assertFalse(Account.Account(acc,fname,lname,ssn,pin1,balance).isValidPIN(pin1))
        self.assertTrue(Account.Account(acc,fname,lname,ssn,pin2,balance).isValidPIN(pin2))

    def test_isNumeric(self):
        num = 'a'
        num2 = '124'
        self.assertTrue(BankUtility.BankUtility().isNumeric(num2))
        self.assertFalse(BankUtility.BankUtility().isNumeric(num))
    def test_convertDollarsToCents(self):
        amount1 = 10
        amount = 2
        self.assertEqual(BankUtility.BankUtility().convertFromDollarsToCents(amount1),1000)
        self.assertEqual(BankUtility.BankUtility().convertFromDollarsToCents(amount),200)
    def test_generateRandomInt(self):
        min = 1
        max = 10
        max2 = 3
        self.assertLess(BankUtility.BankUtility().generateRandomInteger(min,max),11)
        self.assertLess(BankUtility.BankUtility().generateRandomInteger(min,max2),4)

    def test_CoinCollector(self):
        coin1 = 'PNDWHTS' # should be 1.66
        coin2 = 'WW' #should be 2
        coin3 = 'PP' # should be .02

        self.assertAlmostEqual(CoinCollector.CoinCollector(coin1).parseChange(),1.66)
        self.assertAlmostEqual(CoinCollector.CoinCollector(coin2).parseChange(),2.0)
        self.assertAlmostEqual(CoinCollector.CoinCollector(coin3).parseChange(),0.02)

if __name__ == "__main__":
    unittest.main()




