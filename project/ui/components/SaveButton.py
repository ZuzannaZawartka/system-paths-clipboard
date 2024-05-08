from logic.ClipboardManager import ClipboardManager
from .Button import Button


class SaveButton(Button):
    """
    Klasa reprezentująca przycisk do zapisu (SaveButton) w interfejsie użytkownika.

    Dziedziczy po klasie Button.

    Attributes:
        parent: Referencja do obiektu rodzica (widget nadrzędny).
        clipboard_manager (ClipboardManager): Instancja menedżera schowka.
    """

    def __init__(self, parent, text):
        """
        Inicjalizuje obiekt klasy SaveButton.

        Args:
            parent: Referencja do obiektu rodzica (widget nadrzędny).
            text (str): Tekst wyświetlany na przycisku.
        """
        super().__init__(parent, text)
        self.parent = parent
        self.clipboard_manager = ClipboardManager.get_instance()
        self.init_button(self.on_save_button)

    def on_save_button(self):
        """
        Obsługuje zdarzenie kliknięcia przycisku zapisu.

        Pobiera wartość z pola tekstowego (LineEdit) i wybraną wartość z listy.
        Jeśli pole wyboru (Checkbox) jest zaznaczone, dodaje nowy element do bazy danych.
        W przeciwnym razie aktualizuje wybrany element w bazie danych.
        """
        value = self.parent.line_edit.get_text()
        new_value = self.clipboard_manager.get_selected_item()

        if self.parent.checkbox.get_checkbox_value():
            # Zapisywanie do bazy danych jako nowy element
            self.clipboard_manager.add_to_database(value)
        else:
            # Zapisywanie do bazy danych jako aktualizacja elementu
            self.clipboard_manager.update_database(new_value, value)
