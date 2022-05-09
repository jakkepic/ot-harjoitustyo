import unittest
from entities.voucher import Voucher
from entities.coscentre import CostCentre

# Tests classes from entities
class TestEntities(unittest.TestCase):
    def setUp(self):
        self.voucher_1 = Voucher(1, '0001', 0, 10, "Testi")
        self.costcentre = CostCentre('1001', 'Testing')

    # Tests that a voucher can be created
    def test_voucher_ammount(self):
        ammount = self.voucher_1.ammount
        self.assertEqual(ammount, 10)
    
    # Tests that CostCentre-object can be created, ant that debet ammount is initially 0
    def test_costcentre_income(self):
        ammount = self.costcentre.debit
        self.assertEqual(ammount, 0)

    # Tests that CostCentre-object can be created, ant that credit ammount is initially 0
    def test_costcentre_expenses(self):
        ammount = self.costcentre.credit
        self.assertEqual(ammount, 0)