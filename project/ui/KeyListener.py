from pynput import keyboard
import pyperclip,time
from PyQt5.QtCore import QObject, pyqtSignal, QThread

shortcuts = {
    'copy': '\x03',  # Skrót 'copy' (Ctrl+C)
    'paste': '\x16',  # Skrót 'paste' (Ctrl+V)
}

class KeyListener(QObject):
    """
    Klasa `KeyListener` reprezentuje obiekt do nasłuchiwania klawiatury
    i emitowania sygnałów w przypadku naciśnięcia odpowiednich skrótów.
    """

    # Sygnał emitowany przy naciśnięciu odpowiedniego skrótu
    key_pressed = pyqtSignal(str)

    def __init__(self):
        """
        Inicjalizuje obiekt `KeyListener`.
        """
        super().__init__()
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
        with keyboard.Listener(on_press=self.on_press) as listener:
            self.thread.exec_()  # Uruchom pętlę wątku

    def on_press(self, key):
        """
        Obsługuje zdarzenie naciśnięcia klawisza.
        
        Sprawdza, czy naciśnięty klawisz odpowiada któremuś z zdefiniowanych skrótów.
        Jeśli tak, emituje sygnał `key_pressed` z zaznaczonym tekstem.
        
        :param key: Obiekt reprezentujący naciśnięty klawisz.
        """
        try:
            for action, value in shortcuts.items():
                if key.char == value:
                    if self.selected_text != None:  # Jeśli tekst juz byl zaznaczony
                        time.sleep(0.1) # Poczekaj 0.1 sekundy aby poprawnie skopiować tekst
                    self.selected_text = pyperclip.paste() # Pobierz zaznaczony tekst
                    self.key_pressed.emit(self.selected_text) # Wyemituj sygnał key_pressed

        except AttributeError:
            pass  # Ignoruj klawisze specjalne
