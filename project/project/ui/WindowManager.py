# import tkinter as tk
# from pynput import keyboard

# def on_press(key):
#     # Obsługa zdarzenia naciśnięcia klawisza
#     try:
#         # Pobierz nazwę klawisza
#         key_name = key.char
#     except AttributeError:
#         # Jeśli nie można pobrać nazwy (np. klawisz specjalny), użyj opisu
#         key_name = str(key)

#     # Wyświetl informację o naciśniętym klawiszu
#     print(f'Key {key_name} pressed')

# def start_key_listener():
#     # Rozpocznij nasłuchiwanie zdarzeń klawiatury
#     listener = keyboard.Listener(on_press=on_press)
#     listener.start()

# def main():
#     # Tworzenie głównego okna aplikacji tkinter
#     root = tk.Tk()
#     root.title("Global Keyboard Listener")

#     # Przycisk rozpoczynający nasłuchiwanie klawiatury
#     start_button = tk.Button(root, text="Start Listening", command=start_key_listener)
#     start_button.pack(pady=20)

#     # Uruchomienie głównej pętli aplikacji tkinterdfsffdddd
#     root.mainloop()

# if __name__ == "__main__":
#     main()
import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from SettingsWindow import SettingsWindow



class WindowManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.settings_window = SettingsWindow()

        # Połączenie przycisku w MainWindow z przejściem do SettingsWindow
        self.main_window.button1.clicked.connect(lambda: self.main_window.switchWindow(self.settings_window, self.main_window))

        # Połączenie przycisku w SettingsWindow z powrotem do MainWindow
        self.settings_window.button_back.clicked.connect(lambda: self.settings_window.switchWindow(self.main_window, self.settings_window))

        # Połączenie sygnału z okna z metodą obsługi w WindowManager
        self.main_window.windowSizeChanged.connect(self.handleWindowSize)
        self.settings_window.windowSizeChanged.connect(self.handleWindowSize)

        self.window_size = None

    def handleWindowSize(self, size):
        # Obsługa zmiany rozmiaru okna
        print("Received window size:", size)
        # Tutaj możesz dodać logikę obsługi zmiany rozmiaru okna


    def run(self):
        # Uruchom główne okno
        self.main_window.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    app_manager = WindowManager()
    app_manager.run()
