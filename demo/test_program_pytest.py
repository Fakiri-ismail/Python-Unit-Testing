from re import A
from program import add, get_data, Account
import pytest

# Positive Test
def test_sum_of_even_numbers():
    assert add(2, 4) % 2 == 0

def test_add():
    assert add(10, 3) == 13

# Negative Test
def test_string_input():
    assert add("Fakiri", 3) == "Error: Invalid input"

# Testing Error
def test_add_None():
    with pytest.raises(TypeError):
        add(None, None)

# Fail Test
def test_get_data():
    if not get_data(None):
        pytest.fail("No Data")

# Fixture
@pytest.fixture
def account():
    return Account(1000)

def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500

def test_withdraw(account):
    account.withdraw(500)
    assert account.balance == 500
