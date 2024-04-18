import sys
from PyQt5.QtWidgets import QApplication
from WindowManager import WindowManager
from KeyListener import KeyListener
# from project.data.DatabaseManager import DatabaseManager


class AppManager:
    def __init__(self):
        self.windowManager = WindowManager()
        
        # Utwórz instancję klasy KeyListener
        # self.key_listener = KeyListener()
       
        # self.databaseManager= DatabaseManager()

    def run(self):
        pass
        # self.windowManager.run();
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_manager = AppManager()
    # keyHandler = KeyListener()
    app_manager.run()
    
    sys.exit(app.exec_())