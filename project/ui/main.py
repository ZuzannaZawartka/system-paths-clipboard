import sys
from PyQt5.QtWidgets import QApplication
from WindowManager import WindowManager
# from project.data.DatabaseManager import DatabaseManager


class AppManager:
    def __init__(self):
        self.windowManager = WindowManager()
        # self.databaseManager= DatabaseManager()

    def run(self):
        self.windowManager.run();
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_manager = AppManager()
    app_manager.run()
    sys.exit(app.exec_())