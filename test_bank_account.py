from bank_account import BankAccount
from main import account
import pytest


@pytest.fixture
def bank_account():
    """fixture for repeat code , used this func instead of repeat this code"""
    balance = 100
    account = BankAccount(balance)
    return account

#1
def test_init_balance(bank_account):
    """check if the init balance equal to 100"""
    assert bank_account.balance == 100

#2
def test_deposit(bank_account):
    """check if the balance equal to 150 after deposit 50"""
    bank_account.deposit(50)
    assert bank_account.balance == 150

#3
def test_deposit_invalid():
    """check if the balance equal to 100 after deposit -5"""
    balance = 100
    account = BankAccount(balance)
    account.deposit(-5)
    assert account.balance == 100

#4
def test_withdraw():
    """check if the balance equal to 40 after withdraw 60"""
    balance = 100
    account = BankAccount(balance)
    account.withdraw(60)
    assert account.balance == 40

#5
def test_withdraw_invalid():
    """check if the balance equal to 100 after withdraw -5"""
    balance = 100
    account = BankAccount(balance)
    account.withdraw(-5)
    assert  account.balance == 100

#6
def test_withdraw_invalid_2():
    """check if the balance equal to 100 after withdraw 101"""
    balance = 100
    account = BankAccount(balance)
    account.withdraw(101)
    assert account.balance == 100

#7
def test_withdraw_transaction():
    """check if the message withdrawn after withdraw"""
    balance = 100
    account = BankAccount(balance)
    account.withdraw(50)
    assert "withdrawn 50" in account.transaction

#8
def test_deposit_transaction():
    """check if the message deposited after deposit"""
    balance=100
    account = BankAccount(balance)
    account.deposit(20)
    assert "deposited 120" in account.transaction

#9
def test_get_balance():
    """check if get_balance() func Working properly"""
    balance = 100
    account = BankAccount(balance)
    assert account.get_balance() == 100
    account.deposit(10)
    assert account.get_balance() == 110


#10
def test_apply_Interest():
    """check if apply_Interest() func return balance + monthly_interest (repet)"""
    balance = 120
    account = BankAccount(balance)
    assert  account.apply_Interest() == 120.6


#11
def test_transaction_history_print():
    """check if test_transaction_history func return valid number of transactions"""
    balance = 100
    account = BankAccount(balance)
    assert account.transaction_history == 0
    account.deposit(10)
    assert  account.transaction_history == 1
    account.withdraw(20)
    assert account.transaction_history == 2


#12
def test_commissions_print():
    """check if test_commissions_print func return valid number of commissions"""
    balance = 100
    account = BankAccount(balance)
    account.deposit(10)
    assert account.commissions_print() == 110-1.75
