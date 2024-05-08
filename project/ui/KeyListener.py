import re
import time
import pyautogui  # pylint: disable = import-error
import pyperclip
from logic.ClipboardManager import ClipboardManager
from pynput import keyboard
from constants import SHORTCUTS, COPY_DELAY
from PyQt5.QtCore import QObject, QThread  # pylint: disable = no-name-in-module


class KeyListener(QObject):
    """
    Klasa `KeyListener` reprezentuje obiekt do nasłuchiwania klawiatury
    i emitowania sygnałów w przypadku naciśnięcia odpowiednich skrótów.
    """

    def __init__(self):
        """
        Inicjalizuje obiekt `KeyListener`.
        """
        super().__init__()
        self.clipboard_manager = ClipboardManager.get_instance()
        self.selected_text = None
        self.thread = None

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

        :param key: Obiekt reprezentujący naciśnięty klawisz.
        """
        try:
            if key.char == SHORTCUTS["copy"]:
                self.on_copy()
            elif key.char == SHORTCUTS["paste"]:
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
            time.sleep(COPY_DELAY)  # Poczekaj 0.1 sekundy aby poprawnie skopiować tekst
        self.selected_text = pyperclip.paste()  # Pobierz zaznaczony tekst

        if self.is_valid_path(self.selected_text):
            self.clipboard_manager.add_to_database(self.selected_text)
        else:
            print("Niepoprawna ścieżka pliku : ", self.selected_text)

    def on_paste(self):
        """
        Funkcja wywoływana podczas naciśnięcia skrótu 'paste' (ctrl + v).
        """
        selected_data = (
            self.clipboard_manager.get_selected_item()
        )  # sprawdzic co jesli nie ma nic
        if selected_data is not None:
            pyperclip.copy(selected_data)
            pyautogui.hotkey("ctrl", "v")

    def is_valid_path(self, path):
        """
        Sprawdza czy ścieżka pliku jest mniej więcej poprawna.
        """
        regex = r'(\/.*|[a-zA-Z]:\\(?:([^<>:"\/\\|?*]*[^<>:"\/\\|?*.]\\|..\\)*([^<>:"\/\\|?*]*[^<>:"\/\\|?*.]\\?|..\\))?)'

        # Sprawdź czy podany path pasuje do regexa
        return re.match(regex, path) is not None
