from .Window import Window
from .List import List # pylint: disable = no-name-in-module
from .LineEdit import LineEdit # pylint: disable = no-name-in-module
from .Button import Button # pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QCheckBox # pylint: disable = no-name-in-module
from PyQt5.QtCore import Qt # pylint: disable = no-name-in-module

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

    _instance = None  # Przechowuje instancję singletona

    @classmethod
    def get_instance(cls):
        """
        Zwraca instancję singletona.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        """
        Inicjalizacja głównego okna (`MainWindow`).

        Ustawia tytuł okna i inicjuje interfejs użytkownika.
        """
        if MainWindow._instance is not None:
            raise Exception("This class is a singleton!")

        super(MainWindow, self).__init__("Main Window")
        self.line_edit = LineEdit(self)
        self.list = List(self,self.line_edit)
        self.save_button = Button(self,"save")
        self.delete_button = Button(self,"delete")
    
        self.init_ui()

        self.current_selected_item = None # Przechowuje aktualnie wybrany element z listy

        MainWindow._instance = self # Przypisanie instancji do zmiennej klasy

    def init_ui(self):
        """
        Ustawia interfejs użytkownika dla głównego okna.

        """


        #sektor 1 , input i przycisk zatwierdzający
        # Tworzenie układu poziomego dla QLineEdit i QPushButton
        self.horizontal_layout = QHBoxLayout()


        # Lista opcji wyświetlana w oknie
        self.line_edit.init_line_edit()
        self.horizontal_layout.addWidget(self.line_edit.text_edit)

        # Przycisk
        self.horizontal_layout.addWidget(self.save_button.button)

    
        # Dodanie układu poziomego do układu pionowego
        self.layout.addLayout(self.horizontal_layout)


        ##sektor 2 , checkbox , input na number ile ma byc wyświetlanych pozycji
        checkbox = QCheckBox('Opcja 1')
        checkbox.setChecked(True)  # Ustawienie stanu początkowego
        self.layout.addWidget(checkbox)
        
       
        # sektor 2 , lista i obok przycisk usuwania
        # Tworzenie układu poziomego dla QList i QPushButton
        self.horizontal_layout2 = QHBoxLayout()

        #Inicjalizajca listy opcji wyświetlana w oknie
        self.list.init_list_widget()
        self.horizontal_layout2.addWidget(self.list.list_widget)

        # Przycisk
        self.horizontal_layout2.addWidget(self.delete_button.button)
        self.horizontal_layout2.setAlignment(self.delete_button.button, Qt.AlignTop)


        # Dodanie układu poziomego do układu pionowego
        self.layout.addLayout(self.horizontal_layout2)


    def set_current_selected_item(self,value):
        """
        Ustawia aktualnie wybrany element z listy.
        """
        self.current_selected_item = value