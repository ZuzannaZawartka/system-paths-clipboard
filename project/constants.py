SHORTCUTS = {
    "copy": r"'\x03'",  # Skrót 'copy' (Ctrl+C)
    "paste": r"'\x02'",  # Skrót 'paste' (Ctrl+V)
    "window_show_hide_action": [
        "Key.shift",
        "Key.ctrl_l",
    ],  # Skrót 'window_show_hide_action' (Alt + Left Shift )
}
"""
Słownik zawierający skróty klawiszowe do operacji kopiowania i wklejania.
Wartości takie jaki '\x03' to wartosci key z biblioteki pynput.keyboard dla skrótów klawiszowych w tym przypadku dla ctr+c.
Klucze:
- 'copy': '\x03' (Ctrl+C) - Skrót do operacji kopiowania.
- 'paste': '\x02' (Ctrl+B) - Skrót do operacji wklejania.
"""

COPY_DELAY = float(0.1)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
DIFFERENCE_FROM_BOTTOM = 60


BUTTON_SAVE_NAME = "SAVE"
BUTTON_DELETE_NAME = "DELETE"
CHECKBOX_NAME = "Save as new path"
WINDOW_NAME = "System Paths Manager"
