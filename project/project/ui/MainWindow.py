from PyQt5.QtWidgets import QPushButton
from Window import Window

class MainWindow(Window):

    def __init__(self):
        super(MainWindow, self).__init__('Main Window')

        # Dodanie przycisku do przejścia do SettingsWindow
        self.button1 = QPushButton('Next to Settings')
        self.layout.addWidget(self.button1)
