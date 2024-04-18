import time
import pyperclip
from pynput import keyboard
from constants import SHORTCUTS, COPY_DELAY
from PyQt5.QtCore import QObject, pyqtSignal, QThread # pylint: disable = no-name-in-module

class KeyListener(QObject):
    """
    Klasa `KeyListener` reprezentuje obiekt do nasłuchiwania klawiatury
    i emitowania sygnałów w przypadku naciśnięcia odpowiednich skrótów.
    """
    # Sygnał emitowany przy naciśnięciu odpowiedniego skrótu
    key_pressed = pyqtSignal(str)

    def __init__(self,clipboard_manager):
        """
        Inicjalizuje obiekt `KeyListener`.
        """
        super().__init__()
        self.clipboard_manager = clipboard_manager
        self.selected_text = None

    def start_listening(self):
        """
        Rozpoczyna nasłuchiwanie klawiatury w oddzielnym wątku.
        """
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.listen_to_keyboard)
        self.thread.start()

    def listen_to_keyboard(self):
        """
        Funkcja nasłuchująca klawiatury.
        """
        with keyboard.Listener(on_press=self.on_press):
            self.thread.exec_()  # Uruchom pętlę wątku

    def on_press(self, key):
        """
        Obsługuje zdarzenie naciśnięcia klawisza.
        
        Sprawdza, czy naciśnięty klawisz odpowiada któremuś z zdefiniowanych skrótów.
        Jeśli tak, emituje sygnał `key_pressed` z zaznaczonym tekstem.
        
        :param key: Obiekt reprezentujący naciśnięty klawisz.
        """
        try:
            if key.char == SHORTCUTS['copy']:
                self.on_copy()
            if key.cahr ==  SHORTCUTS['paste']:
                self.on_paste()

        except AttributeError:
            pass  # Ignoruj klawisze specjalne

    def on_copy(self):
        """
        Funkcja wywoływana podczas naciśnięcia skrótu 'copy' (ctrl + c).

        Sprawdza czy tekst był już zaznaczony, a następnie jesli był wywołuje Opóźnienie.
        Następnie pobiera zaznaczony tekst i wywoluje funkcję na bazie danych.
        """
        if self.selected_text is not None:  # Jeśli tekst juz byl zaznaczony
            time.sleep(COPY_DELAY) # Poczekaj 0.1 sekundy aby poprawnie skopiować tekst
        self.selected_text = pyperclip.paste() # Pobierz zaznaczony tekst

        self.clipboard_manager.checkIsInDatabase(self.selected_text)

    def on_paste(self):
        """
        Funkcja wywoływana podczas naciśnięcia skrótu 'paste' (ctrl + v).    
        """
        pass
