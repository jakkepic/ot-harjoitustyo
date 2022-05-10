import unittest
from entities.voucher import Voucher
from entities.coscentre import CostCentre
from build import build
from services.ht_service import HtService

class TestServices(unittest.TestCase):
    def setUp(self):
        self.voucher_1 = Voucher(1, '1001', 0, 10, "Testi")
        self.costcentre = CostCentre('1001', 'Testing')
        self.service = HtService()
    
    # Test if voucher can be saved, and if voucher with same number can be found
    def test_save_voucher(self):
        build()
        self.service.save_voucher(self.voucher_1.number, self.voucher_1.cost_centre, self.voucher_1.debit_credit, self.voucher_1.ammount, self.voucher_1.message)
        vouchers = self.service.get_vouchers()
        testvoucher = vouchers[0]
        self.assertEqual(testvoucher.number, 1)
    
    # Tests that two vouchers cannot be saved with the same number
    def test_save_account_twice(self):
        build()
        self.service.save_voucher(self.voucher_1.number, self.voucher_1.cost_centre, self.voucher_1.debit_credit, self.voucher_1.ammount, self.voucher_1.message)
        test_save_again = self.service.save_voucher(self.voucher_1.number, self.voucher_1.cost_centre, self.voucher_1.debit_credit, self.voucher_1.ammount, self.voucher_1.message)
        self.assertEqual(test_save_again, False)

    # Test if account can be saved, and if account of same number can be found
    def test_save_account(self):
        build()
        self.service.save_new_account(self.costcentre.number, self.costcentre.name)
        test_exists = self.service.find_account(self.costcentre.number)
        self.assertEqual(test_exists, True)
    
    # Tests that two accounts cannot be saved with the same number
    def test_save_account_twice(self):
        build()
        self.service.save_new_account(self.costcentre.number, self.costcentre.name)
        test_save_again = self.service.save_new_account(self.costcentre.number, self.costcentre.name)
        self.assertEqual(test_save_again, False)
    
    # Tests that the method returns us something. 
    # Doesn't test if the formating is correct 
    def test_income_statement(self):
        build()
        self.service.save_new_account(self.costcentre.number, self.costcentre.name)
        self.service.save_voucher(self.voucher_1.number, self.voucher_1.cost_centre, self.voucher_1.debit_credit, self.voucher_1.ammount, self.voucher_1.message)
        lines = self.service.get_income_statement_lines()
        self.assertNotEqual(lines, None)