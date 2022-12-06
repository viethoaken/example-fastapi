import pytest
from app.calculations import add, subtract, multiply, devide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    print('creating empty blank account')
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount (50)

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7)
])

def test_add(num1, num2, expected):
    # print("testing add function")
    assert add(num1, num2) == expected

def test_subtract():
    # print("testing add function")
    assert subtract(9, 4) == 5

def test_multiply():
    # print("testing add function")
    assert multiply(5, 3) == 15

def test_devide():
    # print("testing add function")
    assert devide(6, 3) == 2

def test_bank_set_initial_amount(bank_account):
    # bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    # bank_account = BankAccount()
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    # bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    # bank_account = BankAccount(50)
    bank_account.deposit(20)
    assert bank_account.balance == 70
    
def test_collect_interest(bank_account):
    # bank_account = BankAccount(50)
    bank_account.collect_interest()
    ## round: dua 1 so ve interger, sau dau. bao nhieu so thap phan
    assert round(bank_account.balance, 3) == 55 

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (100, 50, 50),
    (200, 100, 100),
    (300, 200, 100),
    # (300, 500, -200)
])

def test_transaction(zero_bank_account, deposited, withdrew, expected):
    # bank_account = BankAccount(50)
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
