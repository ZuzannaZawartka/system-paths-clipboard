from logic.ClipboardManager import ClipboardManager
from .Button import Button

class SaveButton(Button):
    def __init__(self, parent,text):
        super().__init__(parent,text)
        self.parent = parent
        self.clipboard_manager = ClipboardManager.get_instance()
        self.init_button(self.on_save_button)
        
    def on_save_button(self):
        value = self.parent.line_edit.get_text()
        new_value = self.parent.get_current_selected_item()
        #Zapisywanie do bazy danych jako nowy element
        if(self.parent.checkbox.get_checkbox_value()):
            self.clipboard_manager.add_to_database(value)
        else:
            #Zapisywanie do bazy danych jako aktualizacja elementu
            self.clipboard_manager.update_database(new_value,value)
        # self.parent.line_edit.text_edit.setFocus()
        # self.parent.line_edit.text_edit.setPlaceholderText("Wpisz nową pozycję")