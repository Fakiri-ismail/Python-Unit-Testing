def add(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return "Error: Invalid input"
    else:
        return x + y

def get_data(l):
    return l


class Account():

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
