from PyQt5.QtWidgets import QCheckBox  # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement


class Checkbox(WidgetElement):
    """
    Klasa reprezentująca pole wyboru (QCheckBox) w interfejsie użytkownika.

    Dziedziczy po klasie WidgetElement.

    Attributes:
        parent: Referencja do obiektu rodzica (widget nadrzędny).
        text (str): Tekst wyświetlany obok pola wyboru.
        is_checked (bool): Flaga określająca stan zaznaczenia pola wyboru.
        checkbox (QCheckBox): Obiekt pola wyboru PyQt.
    """

    def __init__(self, parent, text):
        """
        Inicjalizuje obiekt klasy Checkbox.

        Args:
            parent: Referencja do obiektu rodzica (widget nadrzędny).
            text (str): Tekst wyświetlany obok pola wyboru (domyślnie 'Save as new path').
        """
        super().__init__(parent)
        self.parent = parent
        self.text = text
        self.checkbox = QCheckBox(self.text)

        self.init_checkbox()

    def init_checkbox(self):
        """
        Inicjalizuje pole wyboru (QCheckBox) ustawiając tekst i stan zaznaczenia.
        """
        self.checkbox.setChecked(True)
        self.checkbox.setObjectName(self.text)
        self.load_stylesheet(self.checkbox)

    def get_checkbox_value(self):
        """
        Zwraca aktualny stan zaznaczenia pola wyboru.

        Returns:
            bool: True jeśli pole wyboru jest zaznaczone, False w przeciwnym razie.
        """
        return self.checkbox.isChecked()
