from .Button import Button

class SaveButton(Button):
    def __init__(self, parent,text):
        super().__init__(parent,text)
        self.parent = parent
        self.init_button(self.on_save_button)
        
    def on_save_button(self):
        print("AAASave Button clicked")
        # self.parent.line_edit.text_edit.setFocus()
        # self.parent.line_edit.text_edit.setPlaceholderText("Wpisz nową pozycję")