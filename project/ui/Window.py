from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize

class Window(QWidget):

    def __init__(self, title):
        """
        Inicjalizacja okna.

        Args:
            title (str): Tytuł okna.
        """
        super(Window, self).__init__()
        
        # Ustawienie tytułu okna
        self.setWindowTitle(title)

        # Ustawienie układu pionowego dla okna
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def switchWindow(self, windowInstanceToShow, windowInstanceToHide):
        """
        Przełącza między oknami.

        Args:
            windowInstanceToShow (QWidget): Instancja okna do pokazania.
            windowInstanceToHide (QWidget): Instancja okna do ukrycia.
        """
        # Ustawienie minimalnego rozmiaru okna
        windowInstanceToHide.setMinimumSize(self.size())
        windowInstanceToShow.setMinimumSize(self.size())

        # Ukrycie bieżącego okna i pokazanie nowego okna
        windowInstanceToShow.show()
        windowInstanceToHide.hide()
        
    def closeEvent(self, event):
        """
        Obsługuje zdarzenie zamykania okna.

        Args:
            event (QCloseEvent): Zdarzenie zamykania okna.
        """
        event.ignore()
        self.hide()
