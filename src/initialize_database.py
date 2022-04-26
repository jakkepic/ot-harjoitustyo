from database_connection import get_database_connection

def initialize_database():
    db = get_database_connection()
    db.isolation_level = None
    db.execute("DROP TABLE IF EXISTS vouchers")
    db.execute("CREATE TABLE vouchers (id INTEGER primary key, number INTEGER, costcentre TEXT, debitcredit INTEGER, ammount INTEGER, message TEXT)")
    db.execute("CREATE INDEX idx_number ON vouchers (number)")
    db.execute("DROP TABLE IF EXISTS accounts")
    db.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, number TEXT, name TEXT)")

if __name__ == "__main__":
    initialize_database()
