from PyQt5.QtWidgets import QLineEdit # pylint: disable = no-name-in-module


class MainWindowLineEdit:
    def __init__(self, parent):
        self.parent = parent

    def init_line_edit(self):
        # Pole do wprowadzania tekstu
        self.text_edit = QLineEdit()
        self.parent.layout.addWidget(self.text_edit)

    def set_text(self,text):
        self.text_edit.setText(text)