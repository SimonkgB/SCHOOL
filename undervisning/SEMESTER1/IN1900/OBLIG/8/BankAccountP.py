

class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):    # NEW - read balance value
        return self._balance

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)
    
    def transfer(self, amount, number):
        self._balance -= amount
        number._balance += amount
        return number._balance


a1 = BankAccountP("John", "Olsson", "19371554951", 20000)
a2 = BankAccountP("Liz", "Olsson",  "19371564761", 20000)
a1.transfer(7000,a2)
a1.print_info()
a2.print_info()


def test_BankAccountP():
    excpected = 7000
    computed = (a2._balance - a1._balance)/2
    success = (computed == excpected)
    message = "idiot"
    assert success, message
test_BankAccountP()


"""
Terminal> python.exe BankAccoutP.py
John Olsson, 19371554951, balance: 13000
Liz Olsson, 19371564761, balance: 27000
"""