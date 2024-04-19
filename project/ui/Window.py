from PyQt5.QtWidgets import QWidget, QVBoxLayout # pylint: disable = no-name-in-module

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

        # Ustawienie tytułu okna
        self.setWindowTitle(title)

        # Ustawienie układu pionowego dla okna
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def closeEvent(self, event): # pylint: disable=invalid-name
        """
        Obsługuje zdarzenie zamykania okna.

        Args:
            event (QCloseEvent): Zdarzenie zamykania okna.
        """
        event.ignore()  # Ignoruj domyślną obsługę zdarzenia zamykania
        self.hide()  # Ukryj okno, zamiast zamykać je
