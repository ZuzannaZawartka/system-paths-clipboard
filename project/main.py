import sys
from PyQt5.QtWidgets import QApplication  # pylint: disable = no-name-in-module
from ui.MainWindow import MainWindow
from ui.KeyListener import KeyListener
from logic.ClipboardManager import ClipboardManager


class AppManager:
    """
    Klasa `AppManager` łączy wszystkie elementy aplikacji w całość.

    Attributes:
        window_manager (WindowManager): Obiekt zarządzający interfejsem użytkownika.
        key_listener (KeyListener): Obiekt nasłuchujący klawiaturę.
        clipboard_manager (ClipboardManager): Obiekt zarządzający schowkiem (clipboard).
    """

    def __init__(self):
        """
        Inicjalizuje obiekt `AppManager`.
        """
        self.clipboard_manager = ClipboardManager()
        self.main_window = MainWindow()
        self.key_listener = KeyListener()

    def run(self):
        """
        Uruchamia główną pętlę aplikacji.
        Rozpoczyna nasłuchiwanie klawiatury i uruchamia główne okno aplikacji.
        """
        self.key_listener.start_listening()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_manager = AppManager()
    app_manager.run()
    sys.exit(app.exec_())
