from entities.voucher import Voucher

class HtService:
    def __init__(self) -> None:
        pass

    def create_voucher(self, number: int, cost_centre: str, debet: bool, credit: bool, ammount: int, message: str):
        voucher = Voucher(number, cost_centre, debet, credit, ammount, message)