from data.DatabaseManager import DatabaseManager
from PyQt5.QtCore import pyqtSignal,QObject # pylint: disable = no-name-in-module

class ClipboardManager(QObject):

    _instance = None

    all_list_updated = pyqtSignal(object)
    one_element_list_updated = pyqtSignal(object)
 
    @classmethod
    def get_instance(cls):
        """
        Zwraca instancję singletona.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
  
    def __init__(self):
        super().__init__()
        
        self.clipboard = None
        self.database_manager = DatabaseManager()


    def on_init_fetch_data_from_database_to_ui(self):
        """
            Funkcja odpowiada za pobranie danych z bazy danych i zainicjalizowanie listy w oknie głównym.
        """
        data = self.database_manager.get_all_data() # Pobranie wszystkich danych z bazy danych
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

            :param clipboard: Tekst zapisany w schowku.
        """
        self.clipboard = value # Przypisanie wartości do zmiennej clipboard   

        if(self.database_manager.check_if_exists(self.clipboard)):
            self.database_manager.delete_data(self.clipboard)
            self.database_manager.add_data(self.clipboard)
            data = self.database_manager.get_all_data()

            self.all_list_updated.emit(data)
        else:
            self.database_manager.add_data(self.clipboard)
            data = self.database_manager.get_last_data()

            self.one_element_list_updated.emit(data)
        

    def getAllDataFromDatabase(self):
        print("doszło super")


    def delete_from_database(self,value):
        """
            Funkcja odpowiada za kontakt z bazą danych.

            Usuwa wartość z bazy danych.
            Wywoluje zmiane danych na liście w oknie głównym.

            :param value: Tekst zapisany w schowku.
        """
        self.database_manager.delete_data(value)
        data = self.database_manager.get_all_data()
        self.all_list_updated.emit(data)

    