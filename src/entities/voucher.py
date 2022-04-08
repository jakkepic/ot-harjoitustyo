class Voucher():
    def __init__(self, number: int, cost_centre: str, debit_credit: int, ammount: int, message: str):
        self.number = number
        self.cost_centre = cost_centre
        # 0 if debit, 1 if credit
        self.debit_credit = debit_credit
        self.ammount = ammount
        self.message = message
