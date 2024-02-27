import sqlite3


class Database:
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect("data.db")

    def query(self, stmt, parameters = []):
        return self.connection.execute(stmt)