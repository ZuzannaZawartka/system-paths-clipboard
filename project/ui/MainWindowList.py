from PyQt5.QtWidgets import QListWidget # pylint: disable = no-name-in-module

class MainWindowList:
    def __init__(self, parent):
        self.parent = parent
        self.list_widget = QListWidget()
       

    def init_list_widget(self,new_items = []):

        self.list_widget.addItems(new_items)
        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)
        self.parent.layout.addWidget(self.list_widget)

        if(len(new_items) > 0):
           self.parent.text_edit.setText(new_items[0])

    def refresh_list_widget(self, new_items):
        # Usunięcie istniejących elementów
        self.list_widget.clear()

        # Dodanie nowych elementów
        self.list_widget.addItems(new_items)
        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)

    def add_item_to_list_widget(self, new_item):
        # Dodanie nowego elementu na pozycję 0
        self.list_widget.insertItem(0, new_item)

        # Połączenie sygnału zmiany wyboru elementu
        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)


    def on_item_selected(self):
        """
        Obsługuje zdarzenie wyboru elementu z listy.

        Ustawia tekst pola do wprowadzania tekstu na wybrany element z listy.
        """
        self.parent.text_edit.setText(self.list_widget.currentItem().text())
