import sys
from PyQt5.QtWidgets import QApplication # pylint: disable = no-name-in-module
from ui.WindowManager import WindowManager
from ui.KeyListener import KeyListener
from logic.ClipboardManager import ClipboardManager

class AppManager:
    """
    Klasa `AppManager` zarządza główną logiką aplikacji.

    Odpowiada za inicjalizację okna, nasłuchiwanie klawiatury
    i obsługę zdarzeń związanych z klawiaturą.

    Attributes:
        window_manager (WindowManager): Obiekt zarządzający interfejsem użytkownika.
        key_listener (KeyListener): Obiekt nasłuchujący klawiaturę.
        clipboard_manager (ClipboardManager): Obiekt zarządzający schowkiem (clipboard).
    """
    def __init__(self):
        """
        Inicjalizuje obiekt `AppManager`.
        """
        self.window_manager = WindowManager()
        self.key_listener = KeyListener()
        self.key_listener.key_pressed.connect(self.handle_key_pressed)
        self.clipboard_manager = ClipboardManager()

    def handle_key_pressed(self, key):
        """
        Obsługuje zdarzenie naciśnięcia klawisza.

        Wyświetla naciśnięty klawisz na konsoli.

        Args:
            key (str): Naciśnięty klawisz.
        """
        print(f"Key pressed: {key}")
        # Przykładowa obsługa klawisza: sprawdzanie czy jest w bazie danych
        # self.clipboard_manager.checkIsInDatabase(key)
        # print(self.clipboard_manager.getDataFromDatabase())

    def run(self):
        """
        Uruchamia główną pętlę aplikacji.

        Rozpoczyna nasłuchiwanie klawiatury i uruchamia główne okno aplikacji.
        """
        self.key_listener.start_listening()
        self.window_manager.run()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_manager = AppManager()
    app_manager.run()
    sys.exit(app.exec_())
