from .Window import Window
from .MainWindowList import MainWindowList # pylint: disable = no-name-in-module
from .MainWindowLineEdit import MainWindowLineEdit # pylint: disable = no-name-in-module

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
        self.main_window_line_edit = MainWindowLineEdit(self)
        self.main_window_list = MainWindowList(self,self.main_window_line_edit)
    
        self.init_ui()

    def init_ui(self):
        """
        Ustawia interfejs użytkownika dla głównego okna.

        """
        # Lista opcji wyświetlana w oknie
        self.main_window_line_edit.init_line_edit()

        # Lista opcji wyświetlana w oknie
        self.main_window_list.init_list_widget()


    