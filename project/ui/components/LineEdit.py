from PyQt5.QtWidgets import QLineEdit  # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement


class LineEdit(WidgetElement):
    """
    Klasa reprezentująca pole tekstowe (QLineEdit) w interfejsie użytkownika.

    Dziedziczy po klasie WidgetElement.

    Attributes:
        parent: Referencja do obiektu rodzica (widget nadrzędny).
        text_edit (QLineEdit): Obiekt pola tekstowego PyQt.
    """

    def __init__(self, parent):
        """
        Inicjalizuje obiekt klasy LineEdit.

        Args:
            parent: Referencja do obiektu rodzica (widget nadrzędny).
        """
        super().__init__(parent)
        self.parent = parent
        self.init_line_edit()

    def init_line_edit(self):
        """
        Inicjalizuje pole tekstowe (QLineEdit) i ładuje styl dla niego.
        """
        self.text_edit = QLineEdit()

        self.load_stylesheet(self.text_edit)

    def set_text(self, text):
        """
        Ustawia tekst w polu tekstowym (QLineEdit) i ustawia focus na to pole.

        Args:
            text (str): Tekst do ustawienia w polu tekstowym.
        """
        self.text_edit.setText(text)
        self.text_edit.setFocus()

    def get_text(self):
        """
        Pobiera aktualny tekst z pola tekstowego (QLineEdit).

        Returns:
            str: Aktualny tekst wpisany w pole tekstowe.
        """
        return self.text_edit.text()
