from program import add, get_data
import pytest

# Positive Test
def test_sum_of_even_numbers():
    assert add(2, 4) % 2 == 0

def test_sum_of_odd_numbers():
    assert add(1, 3) % 2 == 0

# Negative Test
def test_string_input():
    assert add("Fakiri", 3) == "Error: Invalid input"

# Fail Test
def test_get_data():
    if not get_data(None):
        pytest.fail("No Data")
