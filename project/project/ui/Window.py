from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize, pyqtSignal

class Window(QWidget):
      # Dodajemy sygnał, który będzie emitowany z danymi rozmiaru okna
    windowSizeChanged = pyqtSignal(QSize)

    def __init__(self, title):
        super(Window, self).__init__()
        self.setWindowTitle(title)

        # Ustawienie minimalnego rozmiaru okna
        self.setMinimumSize(QSize(300, 400))

        # Ustawienie układu pionowego dla okna
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        print(self.parent())


    def switchWindow(self, window_instance_to_show, window_instance_to_hide):
        # Ukrycie bieżącego okna i pokazanie nowego okna
        window_instance_to_show.show()
        window_instance_to_hide.hide()
        
