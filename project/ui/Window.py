from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize

class Window(QWidget):

    def __init__(self, title):
        super(Window, self).__init__()

        # Ustawienie tytułu okna
        self.setWindowTitle(title)

        # Ustawienie układu pionowego dla okna
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)



    def switchWindow(self, window_instance_to_show, window_instance_to_hide):
        # Ustawienie minimalnego rozmiaru okna
        window_instance_to_hide.setMinimumSize(self.size())
        window_instance_to_show.setMinimumSize(self.size())

        # Ukrycie bieżącego okna i pokazanie nowego okna
        window_instance_to_show.show()
        window_instance_to_hide.hide()
        

