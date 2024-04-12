import sys
from PyQt5.QtWidgets import QApplication
from WindowManager import WindowManager

class AppManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window_manager = WindowManager()

    def run(self):
        # Uruchom główne okno
        self.window_manager.run()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    app_manager = AppManager()
    app_manager.run()
