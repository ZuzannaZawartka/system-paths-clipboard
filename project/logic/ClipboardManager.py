class ClipboardManager:
    def __init__(self):
        self.clipboard = None

    def checkIsInDatabase(self, clipboard):
        self.clipboard = clipboard
        #TO DO
        # Sprawdź czy wartość znajduje się w bazie danych

    def getDataFromDatabase(self):
        #TO DO
        return self.clipboard
    
if __name__ == '__main__':
    clipboard_manager = ClipboardManager()
    clipboard_manager.checkIsInDatabase("Hello World")
    print(clipboard_manager.getDataFromDatabase())