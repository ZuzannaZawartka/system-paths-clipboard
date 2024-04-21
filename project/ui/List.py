from logic.ClipboardManager import ClipboardManager # pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QListWidget # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement

class List(WidgetElement):

    def __init__(self, parent,main_window_line_edit):
        super().__init__(parent)
        self.clipboard_manager = ClipboardManager.get_instance() # Pobranie instancji singletona
        
        self.parent = parent
        self.list_widget = QListWidget()
        self.line_edit = main_window_line_edit

        self.init_list_widget()
       

    def init_list_widget(self):

        new_items = self.clipboard_manager.on_init_fetch_data_from_database_to_ui()
        self.list_widget.addItems(new_items)
        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)

        self.load_stylesheet(self.list_widget)

        if(len(new_items) > 0):
           self.parent.set_current_selected_item(new_items[0])


        # W momencie gdy dojdzie do zmiany danych w bazie danych, lista w oknie głównym zostaje zaktualizowana
        self.clipboard_manager.all_list_updated.connect(self.refresh_list_widget)
        self.clipboard_manager.one_element_list_updated.connect(self.add_item_to_list_widget)

    def refresh_list_widget(self,new_items):
        # Usunięcie istniejących elementów
        self.list_widget.clear()

        # Dodanie nowych elementów
        self.list_widget.addItems(new_items)

        self.parent.set_current_selected_item(new_items[0])

        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)

    def add_item_to_list_widget(self,new_item):
        # Dodanie nowego elementu na pozycję 0
        self.list_widget.insertItem(0, new_item)

        # Połączenie sygnału zmiany wyboru elementu
        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)


    def on_item_selected(self):
        """
        Obsługuje zdarzenie wyboru elementu z listy.

        Ustawia tekst pola do wprowadzania tekstu na wybrany element z listy.
        """
        value = self.list_widget.currentItem().text()
        self.parent.set_current_selected_item(value)
        
