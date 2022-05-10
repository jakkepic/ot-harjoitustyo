from entities.voucher import Voucher
from entities.coscentre import CostCentre
from repositories.voucher_repository import VoucerRepository

class HtService:
    def __init__(self) -> None:
        self._voucher_repository = VoucerRepository()
    

    # Methods that interract with vouchers
    def save_voucher(self, number: int, cost_centre: str, debit_credit: int, ammount: int, message: str):
        v = Voucher(number, cost_centre, debit_credit, ammount, message)
        success = self._voucher_repository.save_new_voucher(v)
        return success
    
    def get_vouchers(self):
        return self._voucher_repository.fetch_vouchers()
    
    def delete_voucher(self, n: int):
        self._voucher_repository.delete_voucher(n)

    # Methods that interact with the accounts
    def save_new_account(self, number: str, name:str):
        success = self._voucher_repository.save_account(number, name)
        return success
    
    def find_account(self, number:str):
        return self._voucher_repository.find_account(number)
        
    def get_accounts(self):
        return self._voucher_repository.fetch_accounts()

    # Methods for creating the income statements
    def collect_data(self):
        data = []
        accountscheme = {}
        accounts = self.get_accounts()
        for account in accounts:
            entry = CostCentre(account[0], account[1])
            accountscheme[entry.number] = entry
        
        vouchers = self.get_vouchers()
        for voucher in vouchers:
            if voucher.debit_credit == 0:
                accountscheme[voucher.cost_centre].debit += voucher.ammount
            elif voucher.debit_credit == 1:
                accountscheme[voucher.cost_centre].credit += voucher.ammount

        for key in accountscheme:
            data.append(accountscheme[key])
        return data
    
    def format_data(self, data):
        lines = []
        lines.append('Revenue:')
        total_revenue = 0
        total_expenses = 0
        for entry in data:
            total_revenue += entry.debit
            line = f"{entry.name:20} {'+' + str(entry.debit / 100):>15}"
            lines.append(line)
        revenue_line = f"{'Total revenue':20} {str(total_revenue / 100):>15}"
        lines.append(revenue_line)
        lines.append('')
        lines.append('Expenses:')
        for entry in data:
            total_expenses += entry.credit
            line = f"{entry.name:20} {'-' + str(entry.credit / 100):>15}"
            lines.append(line)
        exp_line = f"{'Total Expenses':20} {str(total_expenses / 100):>15}"
        lines.append(exp_line)
        net_income = total_revenue - total_expenses
        net_income_line = f"{'Net income':20} {str(net_income / 100):>15}"
        lines.append('')
        lines.append(net_income_line)
        return lines
    
    def get_income_statement_lines(self):
        data = self.collect_data()
        lines = self.format_data(data)
        return lines
