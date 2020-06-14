import unittest

class NumbersCanBeAdded(unittest.TestCase):
    def test_numbers_can_be_added(self):
        self.assertEqual(numbers_can_be_added(1, 2), 3) #ar sudejus 1 su 2 bus 3
        self.assertIsInstance(numbers_can_be_added(3, 2), int) #ar tai int tipas
        sarasas = [1, 2, 3]
        self.assertIn(3, sarasas) #ar yra sarase 3

    def test_numbers_can_multiply(self):
        self.assertEqual(numbers_multiply(6, 6), 36)

    def test_name_is_rolandas(self):
        self.assertEqual(get_name("rolandas"), 'rolandas') #ar perduotas vardas yra rolandas

    def test_ar_turi_tarpu(self):
        self.assertIs(ar_turi_tarpu('Jonas Jonavičius su Bebru Bebravičium'), True)

def numbers_can_be_added(x, y):
    return x + y

def numbers_multiply(x, y):
    return x * y

def get_name(name):
    return name

def ar_turi_tarpu(tekstas):
    if ' ' in tekstas:   #ar perduotam teskte yra bent vienas space tarpas?
        return True
    else:
        return False