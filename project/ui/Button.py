from PyQt5.QtWidgets import QPushButton # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement


class Button(WidgetElement):
    def __init__(self, parent,text):
        super().__init__(parent)
        self.parent = parent
        self.text = text
      
        self.init_button()

    def init_button(self):
        # Przycisk
        self.button = QPushButton(self.text)
        self.button.setText(self.text)
        self.button.setObjectName(self.text) 
        self.button.clicked.connect(self.save_button)
        # self.parent.layout.addWidget(self.button)
        self.load_stylesheet(self.button)

    def save_button(self):
        print("Button clicked")
        # self.clipboard_manager.getAllDataFromDatabase()