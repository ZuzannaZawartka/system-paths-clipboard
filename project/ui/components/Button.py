from PyQt5.QtWidgets import QPushButton  # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement


class Button(WidgetElement):
    """
    Klasa reprezentująca przycisk (QPushButton) w interfejsie użytkownika.

    Dziedziczy po klasie WidgetElement.

    Attributes:
        parent: Referencja do obiektu rodzica (widget nadrzędny).
        text (str): Tekst wyświetlany na przycisku.
        button (QPushButton): Obiekt przycisku PyQt.
    """

    def __init__(self, parent, text):
        """
        Inicjalizuje obiekt klasy Button.

        Args:
            parent: Referencja do obiektu rodzica (widget nadrzędny).
            text (str): Tekst wyświetlany na przycisku.
        """
        super().__init__(parent)
        self.parent = parent
        self.text = text
        self.button = QPushButton(self.text)

    def init_button(self, function):
        """
        Inicjalizuje przycisk (QPushButton) z określoną funkcją do wywołania po kliknięciu.

        Args:
            function: Funkcja wywoływana po kliknięciu przycisku.
        """
        # Ustawienie tekstu na przycisku
        self.button.setText(self.text)

        # Ustawienie nazwy obiektu na podstawie tekstu
        self.button.setObjectName(self.text)

        # Połączenie sygnału kliknięcia przycisku z określoną funkcją
        self.button.clicked.connect(function)

        # Załadowanie stylu dla przycisku
        self.load_stylesheet(self.button)
