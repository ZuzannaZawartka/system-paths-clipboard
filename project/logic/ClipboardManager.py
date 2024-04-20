from data.DatabaseManager import DatabaseManager
from ui.MainWindow import MainWindow #singleton pattern

class ClipboardManager:

    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Zwraca instancję singletona.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
  
    def __init__(self):
        self.clipboard = None
        
        self.main_window = MainWindow.get_instance()
        self.list = self.main_window.list
        self.database_manager = DatabaseManager()

        self.on_init_fetch_data_from_database_to_ui()


    def on_init_fetch_data_from_database_to_ui(self):
        """
            Funkcja odpowiada za pobranie danych z bazy danych i zainicjalizowanie listy w oknie głównym.
        """
        data = self.database_manager.get_all_data() # Pobranie wszystkich danych z bazy danych
        self.list.init_list_widget(data) # Inicjalizacja listy w oknie głównym

    def add_to_database(self, clipboard):
        """
            Funkcja odpowiada za kontakt z bazą danych.

            Sprawdza czy wartość znajduje się w bazie danych.
            Jeśli się znajduje to usuwa ją i dodaje ponownie na pozycje najnowsza.
            Jeśli nie znajduje się to dodaje wartość do bazy danych.
            Wywoluje zmiane danych na liście w oknie głównym.

            Dzięki czemu pobieramy wszystkie dane z bazy tylko gdy jest to konieczne.
            W pozostałych przypadkach dodając jeden element, robimy to szybciej.

            :param clipboard: Tekst zapisany w schowku.
        """
        self.clipboard = clipboard # Przypisanie wartości do zmiennej clipboard   

        if(self.database_manager.check_if_exists(self.clipboard)):
            self.database_manager.delete_data(self.clipboard)
            self.database_manager.add_data(self.clipboard)
            data = self.database_manager.get_all_data()
            self.list.refresh_list_widget(data)
        else:
            self.database_manager.add_data(self.clipboard)
            data = self.database_manager.get_last_data()
            self.list.add_item_to_list_widget(data)
        

    def getAllDataFromDatabase(self):
        print("doszło super")


    