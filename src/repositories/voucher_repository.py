from entities.voucher import Voucher
from database_connection import get_database_connection

class VoucerRepository():
    def __init__(self) -> None:
        pass

    def save_voucer(self, v: Voucher):
        db = get_database_connection()
        db.isolation_level = None
        previous = db.execute("SELECT * FROM vouchers WHERE number == ?", [v.number]).fetchone()
        if previous:
            return False
        db.execute("INSERT INTO vouchers (number, costcentre, debitcredit, ammount, message) VALUES (?, ?, ?, ?, ?)", [v.number, v.cost_centre, v.debit_credit, v.ammount, v.message])
        return True
    
    def delete_voucher(self, v: Voucher):
        db = get_database_connection()
        db.isolation_level = None
        previous = db.execute("DELETE FROM vouchers WHERE number == ?", [v.number]).fetchone()

    def fetch_vouchers():
        vouchers = []
        db = get_database_connection()
        db.isolation_level = None
        data = db.execute("SELECT number, costcentre, debitcredit, ammount, message FROM vouchers").fetchall()
        for e in data:
            v = Voucher(e[0], e[1], e[2], e[3], e[4])
            vouchers.append(v)
        return vouchers
