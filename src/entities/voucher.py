class Voucher():
    def __init__(self, number: int, cost_centre: str, debet: bool, credit: bool, ammount: int, message: str):
        self.number = number
        self.cost_centre = cost_centre
        self.debet_credit = debet, credit
        self.ammount = ammount
        self.message = message
