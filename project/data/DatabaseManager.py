import os 
import sqlite3


class DatabaseManager:
    """
    Klasa zarządzająca bazą danych SQLite, umożliwiająca operacje na tabeli 'clipboard'.

    Attributes:
        db_name (str): Nazwa pliku bazy danych.
    """

    def __init__(self):
        self.database_path()
        self.create_table()

    def database_path(self):
        """
        Ustawia ścieżkę do pliku bazy danych.
        """
          # Ustaw ścieżkę do bieżącego katalogu, w którym znajduje się plik main.py
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Ustaw ścieżkę względną do bazy danych
        db_relative_path = os.path.join( 'database.db')

        # Utwórz pełną ścieżkę do bazy danych
        self.db_name = os.path.join(current_dir, db_relative_path)


    def execute_query(self, query, *params):
        """
        Wykonuje zapytanie SQL na bazie danych.

        Args:
            query (str): Zapytanie SQL.
            *params: Parametry zapytania.

        Returns:
            sqlite3.Cursor: Obiekt kursora z wynikami zapytania.
        """
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            return cursor

    def create_table(self):
        """
        Creates a table named 'clipboard' if it doesn't already exist in the database.
        The table has two columns: 'id' (INTEGER) and 'value' (TEXT).
        """
        query = (
            f"CREATE TABLE IF NOT EXISTS clipboard (id INTEGER PRIMARY KEY, value TEXT)"
        )
        self.execute_query(query)

    def add_data(self, value):
        """
        Funkcja dodaje wartość do bazy danych.

        Wartość zostaje dodana do bazy danych w tabeli 'clipboard'.

        Args:
            value: wartość do dodania
        """
        query = "INSERT INTO clipboard (value) VALUES (?)"
        self.execute_query(query, value)

    def get_all_data(self, limit=20):
        """
        Funkcja zwraca wszystkie wartości z bazy danych
        z możliwością ustawienia limitu.

        Args:
          limit: ilość wartości do zwrócenia (domyślnie 20)
        """

        query = "SELECT value FROM clipboard ORDER BY id DESC LIMIT ?"
        cursor = self.execute_query(query, limit)

        return [row[0] for row in cursor.fetchall()]

    def get_last_data(self):
        """
        Funkcja zwraca ostatnią wartość z bazy danych.

        Returns:
            str: ostatnia wartość z bazy danych
        """
        query = "SELECT value FROM clipboard ORDER BY id DESC LIMIT 1"
        cursor = self.execute_query(query)
        return cursor.fetchone()[0]

    def check_if_exists(self, value):
        """
        Funkcja sprawdza czy wartość znajduje się w bazie danych.

        Args:
            value: wartość do sprawdzenia

        Returns:
            bool: True jeśli wartość istnieje, False w przeciwnym przypadku
        """
        query = "SELECT value FROM clipboard WHERE value = ?"
        cursor = self.execute_query(query, value)
        return cursor.fetchone() is not None

    def delete_data(self, value):
        """
        Funkcja usuwa wartość z bazy danych.

        Args:
            value: wartość do usunięcia
        """
        query = "DELETE FROM clipboard WHERE value = ?"
        self.execute_query(query, value)


if __name__ == "__main__":

    database = DatabaseManager()
