import os
import sys
from PyQt5.QtGui import QIcon  # pylint: disable = no-name-in-module
from PyQt5.QtCore import QSize  # pylint: disable = no-name-in-module
from PyQt5.QtWidgets import (  # pylint: disable = no-name-in-module
    QApplication,
    QAction,
    QMenu,
    QSystemTrayIcon,
)
from .MainWindow import MainWindow

class WindowManager:
    """
    Klasa `WindowManager` zarządza interakcjami z oknami aplikacji i ikoną w zasobniku systemowym.

    Attributes:
        app (QApplication): Obiekt aplikacji PyQt.
        window_size (QSize): Rozmiar okna głównego.
        main_window (MainWindow): Główne okno aplikacji.
        tray_menu (QMenu): Menu kontekstowe dla ikony zasobnika systemowego.
        tray_icon (QSystemTrayIcon): Ikona zasobnika systemowego.
    """

    def __init__(self):
        """
        Inicjalizacja `WindowManager`.
        """
        self.app = QApplication(sys.argv)
        self.init_ui()
        self.init_windows()
        self.init_tray()

    def init_ui(self):
        """
        Inicjalizacja ustawień interfejsu użytkownika.
        """
        self.window_size = QSize(100, 400)

    def init_windows(self):
        """
        Inicjalizacja głównego okna aplikacji.
        """
        self.main_window = MainWindow()

    def init_tray(self):
        """
        Inicjalizacja ikony w zasobniku systemowym.
        """
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
        self.tray_icon.activated.connect(self.on_tray_click)

        # Pokaż ikonę w zasobniku systemowym
        self.tray_icon.show()

    def on_tray_click(self, reason):
        """
        Obsługa akcji po kliknięciu na ikonę zasobnika systemowego.

        Args:
            reason (QSystemTrayIcon.ActivationReason): Powód aktywacji ikony.
        """
        if reason != QSystemTrayIcon.Context:
            if self.main_window.isHidden():
                self.main_window.show()
            else:
                if self.main_window.isMinimized():
                    self.main_window.showNormal()
                else:
                    self.main_window.hide()

    def run(self):
        """
        Uruchomienie aplikacji.

        Rozpoczyna wyświetlanie głównego okna i uruchamia pętlę zdarzeń aplikacji.
        """
        self.main_window.show()
        sys.exit(self.app.exec_())

    def close(self):
        """
        Zamknięcie aplikacji.

        Zatrzymuje aplikację, ale nie wychodzi z `app.exec_()`.
        """
        self.app.quit()


if __name__ == "__main__":
    app_manager = WindowManager()
    app_manager.run()
