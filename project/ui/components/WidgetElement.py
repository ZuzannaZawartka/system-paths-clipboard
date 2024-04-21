import os
from PyQt5.QtWidgets import QLineEdit,QWidget # pylint: disable = no-name-in-module

path = os.path.join(os.path.dirname(__file__), 'style.css')

class WidgetElement(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

    def load_stylesheet(self, widget):
        # Ścieżka do pliku ze stylami CSS
        css_path = os.path.join(os.path.dirname(__file__), 'style.css')

        # Sprawdzenie czy plik CSS istnieje
        if os.path.exists(css_path):
            # Odczytanie zawartości pliku CSS
            with open(css_path, 'r') as f:
                style_sheet = f.read()

            # Zastosowanie stylu CSS do danego widgetu
            widget.setStyleSheet(style_sheet)
        else:
            print(f"File not found: {css_path}")