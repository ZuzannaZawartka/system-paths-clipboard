from ui.components.Button import Button
from logic.ClipboardManager import ClipboardManager


class DeleteButton(Button):
    """
    Klasa reprezentująca przycisk do usuwania elementu z bazy danych.

    Dziedziczy po klasie Button.

    Attributes:
        parent: Referencja do obiektu rodzica (widget nadrzędny).
        text (str): Tekst wyświetlany na przycisku.
        clipboard_manager (ClipboardManager): Instancja menedżera schowka.
    """

    def __init__(self, parent, text):
        """
        Inicjalizuje obiekt klasy DeleteButton.

        Args:
            parent: Referencja do obiektu rodzica (widget nadrzędny).
            text (str): Tekst wyświetlany na przycisku.
        """
        super().__init__(parent, text)
        self.parent = parent
        self.clipboard_manager = ClipboardManager.get_instance()
        self.init_button(self.on_delete_button)

    def on_delete_button(self):
        """
        Metoda wywoływana po kliknięciu przycisku usuwania.

        Pobiera zaznaczony element z menedżera schowka i usuwa go z bazy danych.
        """
        data = self.clipboard_manager.get_selected_item()
        self.clipboard_manager.delete_from_database(data)
