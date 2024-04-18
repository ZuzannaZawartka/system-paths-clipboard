from pynput import keyboard

shortcuts = {
    'copy': '\x03',  # Skrót 'copy' (Ctrl+C)
    'paste': '\x16',  # Skrót 'paste' (Ctrl+V)
}

class KeyListener:
    def __init__(self):
        # Uruchom słuchacza zdarzeń klawiatury
        self.listener_keyboard = keyboard.Listener(on_press=self.on_press)
        self.listener_keyboard.start()

    def run(self):
        # Rozpocznij nasłuchiwanie klawiatury
        self.listener_keyboard.join()

    def isPrintableKey(self, key):
        print(key)
        # Sprawdź, czy klawisz jest klawiszem znakowym (literą, cyfrą lub spacją)
        return hasattr(key, 'char') and key.char is not None and len(key.char) == 1

    def on_press(self, key):
        if self.isPrintableKey(key):
            # Sprawdź, czy naciśnięty klawisz jest skrótem klawiszowym
            for action, value in shortcuts.items():
                if key.char == value:
                    print(f"Skrót '{action}' został naciśnięty.")

if __name__ == "__main__":
    key_listener = KeyListener()
    key_listener.run()
