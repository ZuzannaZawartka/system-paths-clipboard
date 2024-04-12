import sys
from PyQt5.QtWidgets import QApplication
from WindowManager import WindowManager
# from project.data.DatabaseManager import DatabaseManager


class AppManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.windowManager = WindowManager()
        # self.databaseManager= DatabaseManager()

    def run(self):
        # Uruchom główne okno
        self.windowManager.run()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    app_manager = AppManager()
    app_manager.run()
