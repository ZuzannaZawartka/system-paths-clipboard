import tkinter as tk
from pynput import keyboard

def on_press(key):
    # Obsługa zdarzenia naciśnięcia klawisza
    try:
        # Pobierz nazwę klawisza
        key_name = key.char
    except AttributeError:
        # Jeśli nie można pobrać nazwy (np. klawisz specjalny), użyj opisu
        key_name = str(key)

    # Wyświetl informację o naciśniętym klawiszu
    print(f'Key {key_name} pressed')

def start_key_listener():
    # Rozpocznij nasłuchiwanie zdarzeń klawiatury
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def main():
    # Tworzenie głównego okna aplikacji tkinter
    root = tk.Tk()
    root.title("Global Keyboard Listener")

    # Przycisk rozpoczynający nasłuchiwanie klawiatury
    start_button = tk.Button(root, text="Start Listening", command=start_key_listener)
    start_button.pack(pady=20)

    # Uruchomienie głównej pętli aplikacji tkinterdfsffdddd
    root.mainloop()

if __name__ == "__main__":
    main()
