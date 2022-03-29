import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_rahamaara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_myyntiluvut_oikein(self):
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 0)
    
    # Maukkaat käteisellä riittää
    def test_maukas_riittaa(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_maukas_palautusrahat(self):
        palautusrahat = self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(palautusrahat, 50)
    
    def test_maukas_kasvattaa_myyntiluvut(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 1)

    # Maukkaat käteisellä ei riitä
    def test_maukas_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_maukas_palautusrahat_ei_riita(self):
        palautusrahat = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(palautusrahat, 300)
    
    def test_maukas_kasvattaa_myyntiluvut(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 0)
    
    # Edulliset käteisellä riittää
    def test_edullinen_riittaa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    
    def test_edullinen_palautusrahat(self):
        palautusrahat = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(palautusrahat, 60)
    
    def test_edullinen_kasvattaa_myyntiluvut(self):
        self.kassa.syo_edullisesti_kateisella(300)
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 1)

    # Edulliset käteisellä ei riitä
    def test_edullinen_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_edullinen_palautusrahat(self):
        palautusrahat = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(palautusrahat, 200)
    
    def test_edullinen_kasvattaa_myyntiluvut(self):
        self.kassa.syo_edullisesti_kateisella(200)
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 0)

    # Kortit
    def test_kortilla_edullinen(self):
        kortti = Maksukortti(300)
        onnistuu = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuu, True)

    def test_kortilla_edullinen_muuttaa_saldoa(self):
        kortti = Maksukortti(300)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 60)
    
    def test_edullinen_kortti_kasvattaa_myyntiluvut(self):
        kortti = Maksukortti(300)
        self.kassa.syo_edullisesti_kortilla(kortti)
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 1)
    
    def test_kortilla_edullinen_kassa_muuttumaton(self):
        kortti = Maksukortti(300)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortilla_maukas(self):
        kortti = Maksukortti(500)
        onnistuu = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuu, True)

    def test_kortilla_maukas_muuttaa_saldoa(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
    
    def test_maukas_kortti_kasvattaa_myyntiluvut(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 1)
    
    def test_kortilla_maukas_kassa_muuttumaton(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    # Kortit ei riitä
    def test_kortilla_edullinen_ei_riita(self):
        kortti = Maksukortti(200)
        onnistuu = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuu, False)
    
    def test_kortilla_edullinen_ei_muutta_saldoa(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
    
    def test_edullinen_ei_riita_kortti_kasvattaa_myyntiluvut(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 0)
    
    def test_kortilla_maukas_ei_riita(self):
        kortti = Maksukortti(300)
        onnistuu = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuu, False)
    
    def test_kortilla_maukas_ei_muutta_saldoa(self):
        kortti = Maksukortti(300)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 300)
    
    def test_maukas_kortti_kasvattaa_myyntiluvut_ei_riita(self):
        kortti = Maksukortti(300)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 0)
    
    def test_lataa_kortti(self):
        kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(kortti, 400)
        self.assertEqual(kortti.saldo, 500)
    
    def test_lataa_kortti_kassa_muuttuu(self):
        kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(kortti, 400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_lataa_kortti_nolla(self):
        kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(kortti, -10)
        self.assertEqual(kortti.saldo, 100)