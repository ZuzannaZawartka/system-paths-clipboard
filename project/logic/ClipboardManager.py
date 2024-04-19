from data.DatabaseManager import DatabaseManager

class ClipboardManager:
    def __init__(self):
        self.clipboard = None
        self.database_manager = DatabaseManager()

    def addToDatabase(self, clipboard):
        """
            Funkcja odpowiada za kontakt z bazą danych.

            Sprawdza czy wartość znajduje się w bazie danych.
            Jeśli sie znajduje indkesuje wartość jako najnowszą, jeśli nie dodaje wartość do bazy danych.

            :param clipboard: Tekst zapisany w schowku.
        """
        self.clipboard = clipboard # Przypisanie wartości do zmiennej clipboard   
        print("ClipboardManager: ", self.clipboard)
        self.database_manager.add_data(self.clipboard) # Dodanie wartości do bazy danych
        

    def getAllDataFromDatabase(self):
        pass

    
if __name__ == '__main__':
    clipboard_manager = ClipboardManager()
    