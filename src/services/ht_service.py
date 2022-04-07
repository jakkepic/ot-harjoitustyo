from entities.voucher import Voucher
from entities.costcentre import CostCentre

class HtService:
    def __init__(self) -> None:
        pass

    def create_voucher(number: int, cost_centre: str, debet: bool, credit: bool, ammount: int, message: str):
        return Voucher(number, cost_centre, debet, credit, ammount, message)
    
    def create_costcentre(idcode, name=None):
        return CostCentre(idcode, name)