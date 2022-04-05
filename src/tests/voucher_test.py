import unittest
from entities.voucher import Voucher

class TestVoucher(unittest.TestCase):
    def setUp(self):
        self.voucher_1 = Voucher(1, '0001', True, False, 10, "Testi")

    def test_voucher_ammount(self):
        ammount = self.voucher_1.ammount
        self.assertEqual(ammount, 10)