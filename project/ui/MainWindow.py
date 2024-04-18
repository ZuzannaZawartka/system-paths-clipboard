from PyQt5.QtWidgets import (  # pylint: disable = no-name-in-module
    QLineEdit,
    QLabel,
    QListWidget,
)
from .Window import Window


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
        self.set_ui()

    def set_ui(self):
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

        # Lista opcji
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Option 1", "Option 2", "Option 3", "Option 4"])
        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)
        self.layout.addWidget(self.list_widget)

    def on_item_selected(self):
        """
        Obsługuje zdarzenie wyboru elementu z listy.

        Ustawia tekst pola do wprowadzania tekstu na wybrany element z listy.
        """
        self.text_edit.setText(self.list_widget.currentItem().text())
