import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(190)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
    
    def test_ota_rahaa(self):
        onnistuuko = self.maksukortti.ota_rahaa(9)
        self.assertEqual(onnistuuko, True)
    
    def test_ota_liian_paljon_rahaa(self):
        onnistuuko = self.maksukortti.ota_rahaa(11)
        self.assertEqual(onnistuuko, False)