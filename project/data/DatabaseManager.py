import sqlite3

DB_PATH = 'project\data\database.db'

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS clipboard (id INTEGER PRIMARY KEY, value TEXT)')
        self.connection.commit()

    def add_data(self, value):
        self.cursor.execute(f'INSERT INTO clipboard (value) VALUES (?)', (value,))
        self.connection.commit()

    def get_records(self, limit=10):
        self.cursor.execute(f'SELECT value FROM clipboard LIMIT ?', (limit,))
        return [row[0] for row in self.cursor.fetchall()]

    def close_connection(self):
        self.connection.close()
        print("Connection closed.")

#testy
if __name__ == "__main__":
    db_manager = DatabaseManager(DB_PATH)

    db_manager.create_table()  # Utwórz tabelę przy pierwszym uruchomieniu
    db_manager.add_data("plik1")
    db_manager.add_data("plik2")

    records = db_manager.get_records(5)  # Pobierz 5 rekordów
    print("Określona liczba rekordów:")
    print(records)
    db_manager.close_connection()  # Zamknij połączenie z bazą danych
