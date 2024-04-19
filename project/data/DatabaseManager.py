import sqlite3
import constants as const

class DatabaseManager:
    def __init__(self):
        self.db_name = const.DB_PATH

    def execute_query(self, query, *params):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            return cursor

    def create_table(self):
        """
        Creates a table named 'clipboard' if it doesn't already exist in the database.
        The table has two columns: 'id' (INTEGER) and 'value' (TEXT).
        """
        query = (f'CREATE TABLE IF NOT EXISTS clipboard (id INTEGER PRIMARY KEY, value TEXT)')
        self.execute_query(query)

    def add_data(self, value):
        """
            Funkcja dodaje wartość do bazy danych.

            Jeśli wartość już istnieje, to zostanie usunięta i dodana ponownie na końcu listy.
            Jeśli jest nowa, to zostanie dodana na końcu listy.

            :param value: wartość do dodania
        """
        if self.check_if_exists(value):
            self.delete_data(value)
        query = "INSERT INTO clipboard (value) VALUES (?)"
        self.execute_query(query, value)

    def get_all_data(self, limit=10):
        """
            Funkcja zwraca wszystkie wartości z bazy danych
            z możliwością ustawienia limitu.

            :param limit: ilość wartości do zwrócenia
        """

        query = "SELECT value FROM clipboard ORDER BY id DESC LIMIT ?"
        cursor = self.execute_query(query, limit)
        return [row[0] for row in cursor.fetchall()]

    def check_if_exists(self, value):
        query = "SELECT value FROM clipboard WHERE value = ?"
        cursor = self.execute_query(query, value)
        return cursor.fetchone() is not None

    def delete_data(self, value):
        query = "DELETE FROM clipboard WHERE value = ?"
        self.execute_query(query, value)


#testy
if __name__ == "__main__":
    db_manager = DatabaseManager()

    db_manager.create_table()  # Utwórz tabelę przy pierwszym uruchomieniu
    db_manager.add_data("stozeczek")
    db_manager.add_data("dodaszniczek")

    db_manager.delete_data("plik1")

    records = db_manager.get_all_data()
    print(records)