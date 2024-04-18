import sys
from PyQt5.QtWidgets import QApplication
from WindowManager import WindowManager
from KeyListener import KeyListener
# from project.data.DatabaseManager import DatabaseManager


class AppManager:
    def __init__(self):
        self.windowManager = WindowManager()
    
        # Utwórz instancję klasy KeyListener
        self.key_listener = KeyListener()
        self.key_listener.key_pressed.connect(self.handle_key_pressed)

    def handle_key_pressed(self, key):
        # Obsługa naciśnięcia klawisza
        print(f"Key pressed: {key}")

    def run(self):
        self.key_listener.start_listening()
        self.windowManager.run();
       
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_manager = AppManager()
    app_manager.run()
    sys.exit(app.exec_())