from PyQt5.QtWidgets import QPushButton # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement


class Button(WidgetElement):
    def __init__(self, parent,text):
        super().__init__(parent)
        self.parent = parent
        self.text = text
        self.button = QPushButton(self.text)

    def init_button(self,function):
        # Przycisk
        self.button.setText(self.text)
        self.button.setObjectName(self.text) 
        self.button.clicked.connect(function)
        # self.parent.layout.addWidget(self.button)
        self.load_stylesheet(self.button)
