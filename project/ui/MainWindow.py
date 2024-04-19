from .Window import Window
from .List import List # pylint: disable = no-name-in-module
from .LineEdit import LineEdit # pylint: disable = no-name-in-module
from .Button import Button # pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout # pylint: disable = no-name-in-module

class MainWindow(Window):
    """
    Klasa `MainWindow` reprezentuje główne okno aplikacji.

    Dziedziczy po klasie `Window` i dostarcza funkcjonalności
    interfejsu użytkownika dla głównego okna aplikacji.

    Attributes:
        label (QLabel): Etykieta do wyświetlania tekstu.
        text_edit (QLineEdit): Pole do wprowadzania tekstu.
        list_widget (QListWidget): Lista opcji wyświetlana w oknie.
    """

    def __init__(self):
        """
        Inicjalizacja głównego okna (`MainWindow`).

        Ustawia tytuł okna i inicjuje interfejs użytkownika.
        """
        super(MainWindow, self).__init__("Main Window")
        self.line_edit = LineEdit(self)
        self.list = List(self,self.line_edit)
        self.save_button = Button(self,"save")
    
        self.init_ui()

    def init_ui(self):
        """
        Ustawia interfejs użytkownika dla głównego okna.

        """
        # Tworzenie układu poziomego dla QLineEdit i QPushButton
        self.horizontal_layout = QHBoxLayout()


        # Lista opcji wyświetlana w oknie
        self.line_edit.init_line_edit()
        self.horizontal_layout.addWidget(self.line_edit.text_edit)

        # Przycisk
        self.button = QPushButton("Przycisk")
        self.horizontal_layout.addWidget(self.button)
    
        # Dodanie układu poziomego do układu pionowego
        self.layout.addLayout(self.horizontal_layout)

        #Inicjalizajca listy opcji wyświetlana w oknie
        self.list.init_list_widget()



    