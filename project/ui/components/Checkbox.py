from PyQt5.QtWidgets import QCheckBox # pylint: disable = no-name-in-module
from .WidgetElement import WidgetElement


class Checkbox(WidgetElement):
    def __init__(self, parent,text):
        super().__init__(parent)
        self.parent = parent
        self.text = text
        self.is_checked = True
        self.checkbox = QCheckBox()

        self.init_checkbox()


    def init_checkbox(self):
        # Przycisk
        self.checkbox.setText(self.text)
        self.checkbox.setChecked(self.is_checked) 
        self.checkbox.setObjectName(self.text) 
        self.checkbox.clicked.connect(self.on_change_checkbox)
        self.load_stylesheet(self.checkbox)


    def on_change_checkbox(self):
        if self.checkbox.isChecked():
            print(f"Checkbox '{self.text}' is checked")
            # Perform actions when checkbox is checked
            # Example: self.parent.line_edit.setPlaceholderText("Enter new item")
        else:
            print(f"Checkbox '{self.text}' is unchecked")
            # Perform actions when checkbox is unchecked
            # Example: self.parent.line_edit.setPlaceholderText("")
        
        self.is_checked = self.checkbox.isChecked()

    def get_checkbox_value(self):
        return self.is_checked