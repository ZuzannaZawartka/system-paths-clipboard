from PyQt5.QtWidgets import QPushButton
from Window import Window
from MainWindow import MainWindow

class SettingsWindow(Window):

    def __init__(self):
        super(SettingsWindow, self).__init__('Settings Window')

        # Dodanie przycisku do powrotu do MainWindow
        self.button_back = QPushButton('Back to Main')
        self.layout.addWidget(self.button_back)
