"""
Test example with doctest

>>> factorial(1)
1
"""


def factorial(x):
    """
    >>> factorial(0)
    1

    >>> factorial(3)
    6

    >>> [factorial(i) for i in range(6)]
    [1, 1, 2, 6, 24, 120]
    """
    return 1 if x == 1 or x == 0 else x * factorial(x -1)

if __name__ == "__main__":
    import doctest

    doctest.testmod()