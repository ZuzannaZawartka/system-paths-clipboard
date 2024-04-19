import os
from PyQt5.QtWidgets import QLineEdit,QWidget # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement

class LineEdit(WidgetElement):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent      

    def init_line_edit(self):
        # Pole do wprowadzania tekstu
        self.text_edit = QLineEdit()
        #element.layout.addWidget(self.text_edit)
        self.load_stylesheet(self.text_edit)

    def set_text(self,text):
        self.text_edit.setText(text)

