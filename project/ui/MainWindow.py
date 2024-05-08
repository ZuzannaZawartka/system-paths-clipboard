from logic.ClipboardManager import ClipboardManager
from ui.components.SaveButton import SaveButton
from ui.components.DeleteButton import DeleteButton
from ui.components.Checkbox import Checkbox
from ui.components.List import List  # pylint: disable = no-name-in-module
from ui.components.LineEdit import LineEdit  # pylint: disable = no-name-in-module
from constants import (
    BUTTON_SAVE_NAME,
    BUTTON_DELETE_NAME,
    CHECKBOX_NAME,
    WINDOW_NAME,
)
from PyQt5.QtCore import Qt  # pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QHBoxLayout  # pylint: disable = no-name-in-module
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
        super(MainWindow, self).__init__(WINDOW_NAME)

        self.clipboard_manager = ClipboardManager.get_instance()
        self.line_edit = LineEdit(self)
        self.list = List(self, self.line_edit)
        self.save_button = SaveButton(self, BUTTON_SAVE_NAME)
        self.delete_button = DeleteButton(self, BUTTON_DELETE_NAME)
        self.checkbox = Checkbox(self, CHECKBOX_NAME)

        self.init_ui()

    def init_ui(self):
        """
        Ustawia interfejs użytkownika dla głównego okna.

        """

        # sektor 1 , input i przycisk zatwierdzający
        # Tworzenie układu poziomego dla QLineEdit i QPushButton
        self.horizontal_layout = QHBoxLayout()

        # Lista opcji wyświetlana w oknie
        self.horizontal_layout.addWidget(self.line_edit.text_edit)

        # Przycisk
        self.horizontal_layout.addWidget(self.save_button.button)

        # Dodanie układu poziomego do układu pionowego
        self.layout.addLayout(self.horizontal_layout)

        ##sektor 2 , checkbox , input na number ile ma byc wyświetlanych pozycji

        self.layout.addWidget(self.checkbox.checkbox)

        # sektor 2 , lista i obok przycisk usuwania
        # Tworzenie układu poziomego dla QList i QPushButton
        self.horizontal_layout2 = QHBoxLayout()

        # Inicjalizajca listy opcji wyświetlana w oknie
        self.horizontal_layout2.addWidget(self.list.list_widget)

        # Przycisk
        self.horizontal_layout2.addWidget(self.delete_button.button)
        self.horizontal_layout2.setAlignment(self.delete_button.button, Qt.AlignTop)

        # Dodanie układu poziomego do układu pionowego
        self.layout.addLayout(self.horizontal_layout2)

    def set_current_selected_item(self, value):
        """
        Ustawia aktualnie wybrany element z listy.
        """
        self.clipboard_manager.set_selected_item_in_clipboard(value)
        self.line_edit.set_text(value)
