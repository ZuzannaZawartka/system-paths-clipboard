import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QSystemTrayIcon,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from MainWindow import MainWindow

class WindowManager:
    def __init__(self):

        self.app = QApplication(sys.argv)
        self.initUi()
        self.initWindows()
        self.initTray()

    def initUi(self):
        self.window_size = QSize(100, 400)

    def initWindows(self):
        self.main_window = MainWindow()

    def initTray(self):
        # Utwórz akcję dla opcji "Exit"
        exit_action = QAction("Exit", self.app)
        exit_action.triggered.connect(self.close)

        # Utwórz menu dla ikony zasobnika systemowego
        self.tray_menu = QMenu()
        self.tray_menu.addAction(exit_action)

        # Uzyskanie ścieżki do bieżącego pliku
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Uzyskanie ścieżki do folderu assets
        assets_dir = os.path.join(current_dir, "assets")

        # Uzyskanie pełnej ścieżki do pliku tray_icon.png w folderze assets
        icon_path = os.path.join(assets_dir, "tray_icon.png")

        # Utwórz ikonę zasobnika systemowego
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self.app)
        self.tray_icon.setToolTip("My Tray App")
        self.tray_icon.setContextMenu(self.tray_menu)


        self.tray_icon.activated.connect(self.whenTrayClicked)# Po kliknięciu w ikonę zasobnika systemowego

        # Pokaż ikonę w zasobniku systemowym
        self.tray_icon.show()

    def whenTrayClicked(self, reason):
        if reason != QSystemTrayIcon.Context:  # Sprawdź, czy aktywacja jest spowodowana menu kontekstowym QSystemTrayIcon.Trigger - reprezentuje standardowe akcje, takie jak kliknięcie lewym przyciskiem myszy
            if self.main_window.isHidden(): # Sprawdź, czy okno jest ukryte
                    self.main_window.show()# Pokaż okno
            else:
                if(self.main_window.isMinimized()):# Sprawdź, czy okno jest zminimalizowane
                    self.main_window.showNormal();# Pokaż okno
                else:
                    self.main_window.hide()# Ukryj okno

    def run(self):
        # Ukryj główne okno na starcie
        self.main_window.show();
        sys.exit(self.app.exec_())

    def close(self):
        # Zatrzymaj aplikację, ale nie wychodź z app.exec_()
        self.app.quit()

if __name__ == '__main__':
    app_manager = WindowManager()
    app_manager.run()
