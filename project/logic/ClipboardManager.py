from data.DatabaseManager import DatabaseManager
from PyQt5.QtCore import pyqtSignal, QObject  # pylint: disable = no-name-in-module


class ClipboardManager(QObject):
    """
    Klasa zarządzająca schowkiem aplikacji oraz interakcją z bazą danych.

    Ta klasa dziedziczy po QObject i emituje sygnały w odpowiedzi na zmiany w bazie danych.

    Attributes:
        all_list_updated (pyqtSignal): Sygnał emitowany po aktualizacji całej listy danych.
        one_element_list_updated (pyqtSignal): Sygnał emitowany po dodaniu pojedynczego elementu do listy.
    """

    _instance = None

    all_list_updated = pyqtSignal()
    one_element_list_updated = pyqtSignal(object)

    @classmethod
    def get_instance(cls):
        """
        Zwraca instancję singletona.

        Returns:
            ClipboardManager: Instancja singletona.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        super().__init__()

        self.clipboard = None
        self.current_selected_item = (
            None  # Przechowuje aktualnie wybrany element z listy
        )
        self.database_manager = DatabaseManager()

    def on_init_fetch_data_from_database_to_ui(self):
        """
        Funkcja odpowiada za pobranie danych z bazy danych i zainicjalizowanie listy w oknie głównym.

        Returns:
            list: Lista danych z bazy danych.
        """
        data = (
            self.database_manager.get_all_data()
        )  # Pobranie wszystkich danych z bazy danych
        return data

    def add_to_database(self, value):
        """
        Funkcja odpowiada za kontakt z bazą danych.

        Sprawdza czy wartość znajduje się w bazie danych.
        Jeśli się znajduje to usuwa ją i dodaje ponownie na pozycje najnowsza.
        Jeśli nie znajduje się to dodaje wartość do bazy danych.
        Wywoluje zmiane danych na liście w oknie głównym.

        Dzięki czemu pobieramy wszystkie dane z bazy tylko gdy jest to konieczne.
        W pozostałych przypadkach dodając jeden element, robimy to szybciej.

        Args:
            clipboard: Tekst zapisany w schowku.
        """
        self.clipboard = value  # Przypisanie wartości do zmiennej clipboard

        if self.database_manager.check_if_exists(self.clipboard):
            self.database_manager.delete_data(self.clipboard)
            self.database_manager.add_data(self.clipboard)
            self.all_list_updated.emit()
        else:
            self.database_manager.add_data(self.clipboard)
            data = self.database_manager.get_last_data()
            self.one_element_list_updated.emit(data)

    def delete_from_database(self, value):
        """
        Funkcja odpowiada za kontakt z bazą danych.

        Usuwa wartość z bazy danych.
        Wywoluje zmiane danych na liście w oknie głównym.

        Args:
            value: Tekst zapisany w schowku.
        """

        if self.database_manager.check_if_exists(value):
            self.database_manager.delete_data(value)
            self.all_list_updated.emit()
        else:
            print("Nie ma takiego elementu w bazie danych")

    def update_database(self, old_value, new_value):
        """
        Funkcja odpowiada za kontakt z bazą danych.

        Aktualizuje wartość w bazie danych.
        Wywoluje zmiane danych na liście w oknie głównym.

        Args:
            old_value: Stara wartość
            new_value: Nowa wartość
        """
        if self.database_manager.check_if_exists(old_value):
            if self.database_manager.check_if_exists(new_value):
                self.database_manager.delete_data(old_value)
                self.add_to_database(new_value)
            else:
                self.database_manager.delete_data(old_value)
                self.database_manager.add_data(new_value)
            self.all_list_updated.emit()
        else:
            print("Nie ma takiego elementu w bazie danych")

    def set_selected_item_in_clipboard(self, value):
        """
        Ustawia aktualnie wybrany element z listy.
        """
        self.current_selected_item = value

    def get_selected_item(self):
        """
        Zwraca aktualnie wybrany element z listy.

        Returns:
            str: Aktualnie wybrany element z listy.
        """
        return self.current_selected_item
