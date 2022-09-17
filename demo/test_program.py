from program import add

def test_sum_of_even_numbers():
    assert add(2, 4) % 2 == 0

def test_sum_of_odd_numbers():
    assert add(1, 3) % 2 == 0