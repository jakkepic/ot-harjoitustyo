import code


class CostCentre():
    def __init__(self, idcode: str, name: str = 'new_cost_centre'):
        self.idcode = idcode
        self.name = name
        self.debet = 0
        self.credit = 0
