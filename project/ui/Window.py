import os
import sys
from PyQt5.QtCore import Qt, QSize  # pylint: disable = no-name-in-module
from PyQt5.QtGui import QIcon  # pylint: disable = no-name-in-module
from PyQt5.QtWidgets import (  # pylint: disable = no-name-in-module
    QApplication,
    QAction,
    QMenu,
    QWidget,
    QVBoxLayout,
    QSystemTrayIcon,
)
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, DIFFERENCE_FROM_BOTTOM


class Window(QWidget):
    """
    Klasa `Window` reprezentuje podstawowe okno aplikacji.

    Dziedziczy po klasie `QWidget` i dostarcza podstawowe funkcjonalności okna.
    Zarządza funkcjonalnością tray icon oraz układem okna.

    Attributes:
        app (QApplication): Instancja aplikacji.
        title (str): Tytuł okna.
        tray_icon (QSystemTrayIcon): Ikona zasobnika systemowego.
        tray_menu (QMenu): Menu dla ikony zasobnika systemowego.

        layout (QVBoxLayout): Układ pionowy okna.
    """

    def __init__(self, title):
        """
        Inicjalizacja okna.

        Args:
            title (str): Tytuł okna.
        """
        super(Window, self).__init__()
        self.app = QApplication(sys.argv)

        # Ustawienie okna
        self.title = title
        self.setWindowTitle(title)
        self.init_tray()
        self.init_window()

        # Ustawienie układu pionowego dla okna
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def init_window(self):
        """
        Inicjalizacja głównego okna aplikacji.
        """
        self.window_size = QSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.desktop = QApplication.desktop()
        self.screen_rect = self.desktop.screenGeometry()
        self.screen_width, self.screen_height = (
            self.screen_rect.width(),
            self.screen_rect.height(),
        )

        self.initial_x = self.screen_width - WINDOW_WIDTH
        self.initial_y = self.screen_height - WINDOW_HEIGHT - DIFFERENCE_FROM_BOTTOM

        self.setGeometry(self.initial_x, self.initial_y, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowFlags(
            self.windowFlags() | Qt.FramelessWindowHint | Qt.Tool
        )  # Usunięcie ramki okna, i zablokowanie przesuwania okna

    def init_tray(self):
        """
        Inicjalizacja ikony w zasobniku systemowym.
        """
        # Utwórz akcję dla opcji "Exit"
        exit_action = QAction("Exit", self.app)
        exit_action.triggered.connect(self.close_app_by_exit)

        # Utwórz menu dla ikony zasobnika systemowego
        self.tray_menu = QMenu()
        self.tray_menu.addAction(exit_action)

        # Uzyskanie ścieżki do bieżącego pliku
        icon_path = os.path.join(os.path.dirname(__file__), "assets", "tray_icon.png")

        # Utwórz ikonę zasobnika systemowego
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self.app)
        self.tray_icon.setToolTip(self.title)
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
            if self.isHidden():
                self.show()
            else:
                if self.isMinimized():
                    self.showNormal()  # moze wymagac dodania activateWindow() jesli bysmy chcieli mnimalizowac
                else:
                    self.hide()

    def closeEvent(self, event):  # pylint: disable=invalid-name
        """
        Obsługuje zdarzenie zamykania okna.

        Args:
            event (QCloseEvent): Zdarzenie zamykania okna.
        """
        event.ignore()  # Ignoruj domyślną obsługę zdarzenia zamykania
        self.hide()  # Ukryj okno, zamiast zamykać je

    def showEvent(self, event):  # pylint: disable=invalid-name
        """
        override metody showEvent z klasy QWidget.
        Obsługuje zdarzenie pokazania okna.

        Args:
            event (QShowEvent): Zdarzenie pokazania okna.
        """
        super().showEvent(event)
        self.activateWindow()

    def close_app_by_exit(self):
        """
        Zamknięcie aplikacji na klikniecie exit.
        Zatrzymuje aplikację, ale nie wychodzi z `app.exec_()`.
        """
        self.app.quit()
