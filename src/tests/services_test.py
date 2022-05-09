import unittest
from entities.voucher import Voucher
from entities.coscentre import CostCentre
from build import build
from services.ht_service import HtService
build()

class TestServices(unittest.TestCase):
    def setUp(self):
        self.voucher_1 = Voucher(1, '0001', 0, 10, "Testi")
        self.costcentre = CostCentre('1001', 'Testing')
        self.service = HtService()
    
    def test_save_voucher(self):
        self.service.save_voucher(self.voucher_1.number, self.voucher_1.cost_centre, self.voucher_1.debit_credit, self.voucher_1.ammount, self.voucher_1.message)
        vouchers = self.service.get_vouchers()
        testvoucher = vouchers[0]
        self.assertEqual(testvoucher.number, 1)

