from entities.voucher import Voucher
from repositories.voucher_repository import VoucerRepository

class HtService:
    def __init__(self) -> None:
        self._voucher_repository = VoucerRepository()
    
    def save_voucher(self, number: int, cost_centre: str, debit_credit: int, ammount: int, message: str):
        v = Voucher(number, cost_centre, debit_credit, ammount, message)
        success = self._voucher_repository.save_new_voucher(v)
        return success
    
    def get_vouchers(self):
        return self._voucher_repository.fetch_vouchers()
    
    def delete_voucher(self, n: int):
        self._voucher_repository.delete_voucher(n)

    def change_voucher(self, v: Voucher):
        n = v.number
        self.delete_voucher(n)
        s = self.save_voucher(v)
        return s
    
    def save_new_account(self, number: str, name:str):
        success = self._voucher_repository.save_account(number, name)
        return success
    
    def find_account(self, number:str):
        return self._voucher_repository.find_account(number)
        
    def get_accounts(self):
        return self._voucher_repository.fetch_accounts()