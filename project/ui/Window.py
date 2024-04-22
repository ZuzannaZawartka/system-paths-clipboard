from PyQt5.QtWidgets import QWidget, QVBoxLayout  # pylint: disable = no-name-in-module
import os
import sys
from PyQt5.QtCore import Qt  # pylint: disable = no-name-in-module
from PyQt5.QtGui import QIcon  # pylint: disable = no-name-in-module
from PyQt5.QtCore import QSize  # pylint: disable = no-name-in-module
from PyQt5.QtWidgets import (  # pylint: disable = no-name-in-module
    QApplication,
    QAction,
    QMenu,
    QSystemTrayIcon,
)
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, DIFFERENCE_FROM_BOTTOM


class Window(QWidget):
    """
    Klasa `Window` reprezentuje podstawowe okno aplikacji.

    Dostarcza funkcjonalności takie jak przełączanie między oknami
    oraz obsługa zdarzenia zamykania okna.

    Attributes:
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

        # Ustawienie tytułu okna
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
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Uzyskanie ścieżki do folderu assets
        assets_dir = os.path.join(current_dir, "assets")

        # Uzyskanie pełnej ścieżki do pliku tray_icon.png w folderze assets
        icon_path = os.path.join(assets_dir, "tray_icon.png")

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

    def showEvent(self, event):
        super().showEvent(event)
        self.activateWindow()

    def closeEvent(self, event):  # pylint: disable=invalid-name
        """
        Obsługuje zdarzenie zamykania okna.

        Args:
            event (QCloseEvent): Zdarzenie zamykania okna.
        """
        event.ignore()  # Ignoruj domyślną obsługę zdarzenia zamykania
        self.hide()  # Ukryj okno, zamiast zamykać je

    def close_app_by_exit(self):
        """
        Zamknięcie aplikacji na klikniecie exit.

        Zatrzymuje aplikację, ale nie wychodzi z `app.exec_()`.
        """
        self.app.quit()
