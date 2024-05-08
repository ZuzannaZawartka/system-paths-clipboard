import os
from PyQt5.QtWidgets import QWidget  # pylint: disable = no-name-in-module


class WidgetElement(QWidget):
    """
    Klasa bazowa dla elementów interfejsu użytkownika, umożliwiająca ładowanie stylów CSS do widgetów.

    Attributes:
        parent (QWidget): Referencja do obiektu rodzica (widget nadrzędny).
    """

    def __init__(self, parent=None):
        """
        Inicjalizuje obiekt klasy WidgetElement.

        Args:
            parent (QWidget): Referencja do obiektu rodzica (widget nadrzędny).
        """
        super().__init__(parent)
        self.parent = parent

    def load_stylesheet(self, widget):
        """
        Ładuje styl CSS do określonego widgetu.

        Args:
            widget (QWidget): Widget, do którego mają zostać zastosowane style CSS.

        Raises:
            FileNotFoundError: Jeśli plik style.css nie istnieje.

        """
        # Ścieżka do pliku ze stylami CSS
        css_path = os.path.join(os.path.dirname(__file__), "style.css")

        if os.path.exists(css_path):
            # Odczytanie zawartości pliku CSS
            with open(css_path, "r") as f:
                style_sheet = f.read()

            # Zastosowanie stylu CSS do danego widgetu
            widget.setStyleSheet(style_sheet)
        else:
            raise FileNotFoundError(f"File not found: {css_path}")
