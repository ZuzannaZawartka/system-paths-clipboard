from PyQt5.QtWidgets import QPushButton,QLineEdit,QLabel,QListWidget
from Window import Window

class MainWindow(Window):

    def __init__(self):
        super(MainWindow, self).__init__('Main Window')
        self.setUpUI()


    def setUpUI(self):
        # # Dodanie przycisku do przejścia do SettingsWindow
        # self.button1 = QPushButton('Settings')
        # self.layout.addWidget(self.button1)

       # Etykieta i pole do wprowadzania tekstu
        self.label = QLabel('Edit :')
        self.layout.addWidget(self.label)

        # Dodanie przycisku do przejścia do SettingsWindow
        self.text_edit = QLineEdit()
        self.layout.addWidget(self.text_edit)

        # Lista opcji
        self.list_widget = QListWidget()
        self.list_widget.addItems(['Opcja 1', 'Opcja 2', 'Opcja 3', 'Opcja 4'])
        self.list_widget.itemSelectionChanged.connect(self.on_item_selected)
        self.layout.addWidget(self.list_widget)

    def on_item_selected(self):
        self.text_edit.setText(self.list_widget.currentItem().text())
    
