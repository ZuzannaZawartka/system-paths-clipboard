from PyQt5.QtWidgets import (  # pylint: disable = no-name-in-module
    QLineEdit,
    QLabel,
    QListWidget,
)
from .Window import Window
from .MainWindowList import MainWindowList # pylint: disable = no-name-in-module

class MainWindow(Window):
    """
    Klasa `MainWindow` reprezentuje główne okno aplikacji.

    Dziedziczy po klasie `Window` i dostarcza funkcjonalności
    interfejsu użytkownika dla głównego okna aplikacji.

    Attributes:
        label (QLabel): Etykieta do wyświetlania tekstu.
        text_edit (QLineEdit): Pole do wprowadzania tekstu.
        list_widget (QListWidget): Lista opcji wyświetlana w oknie.
    """

    def __init__(self):
        """
        Inicjalizacja głównego okna (`MainWindow`).

        Ustawia tytuł okna i inicjuje interfejs użytkownika.
        """
        super(MainWindow, self).__init__("Main Window")
        self.main_window_list = MainWindowList(self)
        self.init_ui()

    def init_ui(self):
        """
        Ustawia interfejs użytkownika dla głównego okna.

        Tworzy etykietę, pole do wprowadzania tekstu oraz listę opcji.
        """
        # Etykieta do wyświetlania tekstu
        self.label = QLabel("Edit:")
        self.layout.addWidget(self.label)

        # Pole do wprowadzania tekstu
        self.text_edit = QLineEdit()
        self.layout.addWidget(self.text_edit)

        # Lista opcji wyświetlana w oknie
        self.main_window_list.init_list_widget()

