from entities.voucher import Voucher
from entities.costcentre import CostCentre
from repositories.voucher_repository import VoucerRepository

class HtService:
    def __init__(self) -> None:
        pass

    def create_voucher(self, number: int, cost_centre: str, debet_credit: int, ammount: int, message: str):
        return Voucher(number, cost_centre, debet_credit, ammount, message)
    
    def save_voucher(self, v: Voucher):
        success = VoucerRepository.save_voucer(v)
        return success
    
    def get_vouchers():
        return VoucerRepository.fetch_vouchers
    
    def delete_voucher(self, n: int):
        VoucerRepository.delete_voucher(n)

    def change_voucher(self, v: Voucher):
        n = v.number
        self.delete_voucher(n)
        s = self.save_voucher(v)
        return s
    
    def create_costcentre(self, idcode, name=None):
        return CostCentre(idcode, name)