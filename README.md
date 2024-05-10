
# System Paths Manager

Aplikacja **System Paths Manager** jest narzędziem rozszerzającym schowek systemowy. Pozwala użytkownikowi na przechowywanie, edycję i wygodne korzystanie z ostatnio kopiowanych ścieżek. Kopiując za pomocą skrótu klawiszowego Ctrl + C aplikacja zapisuje do bazy danych ścieżki systemowe ( Windows/Linux ) dzięki czemu w każdej chwili możemy się wrócić do ścieżek z których korzystaliśmy klikając w ikonkę i wyszukując danej ścieżki. Ścieżkę którą ostatnio skopiowaliśmy (domyślnie po skopiowaniu ścieżki, staje się ona wybraną do wklejenia ) lub wybraliśmy z okienka aplikacji możemy w każdej chwili wkleić za pomocą skrótu Ctrl+ B. Po wejściu w aplikację możemy edytować ścieżki, za pomocą checkboxa możemy wybrać tryb edycji (zapisz jako nowa ścieżka / edytuj ). Ścieżka edytowana (lub zapisana jako nowa) na ścieżkę która już istnieje zostaje przeniesiona na pierwsze miejsce w liście i nie zostaje dodana ponownie aby uniknąć duplikatów. 

## Komponenty aplikacji

### AppManager (Zarządca aplikacji)
- `MainWindow`: Zarządza interfejsem użytkownika, jest głównym oknem aplikacji.
- `KeyListener`: Zarządza działaniem skrótów klawiszowych oraz kopiowaniem i wklejaniem zawartości.
- `ClipboardManager`: Zarządza zawartością schowka, jest klasą która łączy UI z bazą danych.

## Wymagania

1. **Python**: Zainstaluj Pythona w wersji 3.x. Możesz pobrać Pythona ze strony [python.org](https://www.python.org/downloads/).
2. **Biblioteki**: Zainstaluj wymagane biblioteki za pomocą polecenia:
   ```
   pip install PyQt5 pyautogui pyperclip pynput
   ```

## Uruchomienie aplikacji

1. **Pobierz kod**: Skopiuj kod aplikacji Paths Manager do plików w odpowiednim układzie katalogowym. Upewnij się, że pliki są ułożone zgodnie z ich strukturą.
   
2. **Uruchomienie z terminala lub wiersza poleceń**:
   - Otwórz terminal (Linux/Mac) lub wiersz poleceń (Windows).
   - Przejdź do katalogu, w którym znajduje się plik `main.py` aplikacji Clipboard Manager.
   - Uruchom aplikację, wpisując polecenie:
     ```
      python -u "c:\github\DS\python-project\project\main.py" //popraw
     ```

## Jak korzystać z aplikacji

1. Uruchom aplikację.
2. Aplikacja pojawi się jako ikonka w prawym dolnym rogu ekranu
3. Używaj skrótów klawiaturowych (np. Ctrl+C, Ctrl+B) do zarządzania schowkiem. Każda skopiowana ścieżka za pomocą Ctrl+C pojawi się w oknie aplikacji.
4. Dodawaj, usuwaj i edytuj przechowywane elementy za pomocą interfejsu użytkownika.

## Dodatkowe informacje

- Aplikacja działa w tle, nasłuchując klawiaturę i zarządzając schowkiem systemowym.
- Baza danych jest możliwie zoptymalizowana dzięki czemu 
s