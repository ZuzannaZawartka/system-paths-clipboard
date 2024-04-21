from ui.components.Button import Button
from logic.ClipboardManager import ClipboardManager

class DeleteButton(Button):
    def __init__(self, parent,text):
        super().__init__(parent,text)
        self.parent = parent
        self.clipboard_manager = ClipboardManager.get_instance()
        self.init_button(self.on_delete_button)

        
    def on_delete_button(self):
        print(self.parent.get_current_selected_item())
        data = self.parent.get_current_selected_item()
        self.clipboard_manager.delete_from_database(data)