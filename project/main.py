import sys
from PyQt5.QtWidgets import QApplication
from ui.WindowManager import WindowManager

from ui.KeyListener import KeyListener
from logic.ClipboardManager import ClipboardManager

# from project.data.DatabaseManager import DatabaseManager


class AppManager:
    def __init__(self):
        self.windowManager = WindowManager()
    
        # Utwórz instancję klasy KeyListener
        self.key_listener = KeyListener()
        self.key_listener.key_pressed.connect(self.handle_key_pressed)

        # Utwórz instancję klasy ClipboardManager (połączenie między ui a bazą danych)
        self.clipboard_manager = ClipboardManager()

    def handle_key_pressed(self, key):
        # Obsługa naciśnięcia klawisza
        print(f"Key pressed: {key}")
        # self.clipboard_manager.checkIsInDatabase(key)
        # print(self.clipboard_manager.getDataFromDatabase())

    def run(self):
        self.key_listener.start_listening()
        self.windowManager.run();
       
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_manager = AppManager()
    app_manager.run()
    sys.exit(app.exec_())