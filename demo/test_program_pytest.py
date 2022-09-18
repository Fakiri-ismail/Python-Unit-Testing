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
@pytest.mark.skip(reason="Failed Test") # To skip failed test
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

# Parametrize (running the same test with different values)
@pytest.mark.parametrize("number", [1, 2, 5, 7])
def test_positive_number(number):
    assert number > 0

# Use fixture as parametrize
@pytest.fixture(params=[1, 2, 3, 4])
def number_1(request):
    return request.param

def test_positive_number_param(number_1):
    assert number_1 > 0