from logic.ClipboardManager import (
    ClipboardManager,
)  # pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QListWidget  # pylint: disable = no-name-in-module
from PyQt5.QtCore import pyqtSignal  # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement


class List(WidgetElement):
    """
    Klasa reprezentująca listę (QListWidget) w interfejsie użytkownika.

    Dziedziczy po klasie WidgetElement.

    Attributes:
        item_selected: Sygnał emitowany po wybraniu elementu z listy (str).
        clipboard_manager (ClipboardManager): Instancja menedżera schowka.
        parent: Referencja do obiektu rodzica (widget nadrzędny).
        list_widget (QListWidget): Obiekt listy PyQt.
        line_edit: Referencja do pola tekstowego w głównym oknie.
    """

    item_selected = pyqtSignal(str)

    def __init__(self, parent, main_window_line_edit):
        """
        Inicjalizuje obiekt klasy List.

        Args:
            parent: Referencja do obiektu rodzica (widget nadrzędny).
            main_window_line_edit: Referencja do pola tekstowego w głównym oknie.
        """
        super().__init__(parent)

        self.clipboard_manager = (
            ClipboardManager.get_instance()
        )  # Pobranie instancji singletona
        self.parent = parent
        self.list_widget = QListWidget()
        self.line_edit = main_window_line_edit

        self.init_list_widget()
        self.setup_connections()

    def init_list_widget(self):
        """
        Inicjalizuje listę (QListWidget) i ładuje dane z bazy danych do interfejsu użytkownika.
        """
        self.load_new_items()
        self.load_stylesheet(self.list_widget)

    def setup_connections(self):
        """
        Ustawia połączenia sygnałów i slotów.
        """
        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)
        self.clipboard_manager.all_list_updated.connect(self.refresh_list_widget)
        self.clipboard_manager.one_element_list_updated.connect(
            self.add_item_to_list_widget
        )

    def refresh_list_widget(self):
        """
        Odświeża listę (QListWidget) po aktualizacji danych w bazie.
        """
        self.list_widget.clear()
        self.load_new_items()

    def add_item_to_list_widget(self, new_item):
        """
        Dodaje nowy element do listy (QListWidget).

        Args:
            new_item (str): Nowy element do dodania do listy.
        """
        self.list_widget.insertItem(0, new_item)
        self.parent.set_current_selected_item(new_item)
        self.refresh_highlight_on_item_in_list()

    def load_new_items(self):
        """
        Ładuje nowe elementy do listy.
        """
        new_items = self.clipboard_manager.on_init_fetch_data_from_database_to_ui()
        self.list_widget.addItems(new_items)

        if new_items:
            self.parent.set_current_selected_item(new_items[0])
        else:
            self.parent.set_current_selected_item("")

        self.refresh_highlight_on_item_in_list()

    def on_item_selected(self):
        """
        Obsługuje zdarzenie wyboru elementu z listy.

        Ustawia tekst pola do wprowadzania tekstu na wybrany element z listy.
        """
        if self.list_widget.currentItem() is not None:
            value = self.list_widget.currentItem().text()
            self.parent.set_current_selected_item(value)

    def refresh_highlight_on_item_in_list(self):
        """
        Odświeża podświetlenie na liście.
        """
        self.list_widget.setCurrentRow(0)
