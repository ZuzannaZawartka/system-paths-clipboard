# System Paths Manager

The **System Paths Manager** application is an extended clipboard tool that allows users to store, edit, and conveniently use recently copied file paths. By utilizing the keyboard shortcut Ctrl + C, the application saves system paths (Windows/Linux) into a database, enabling users to easily access and paste them later by clicking on the application icon (the application can also be opened with the Ctrl + left Shift shortcut) and searching for the desired path. The most recently copied path (by default, after copying a path, it becomes the selected one for pasting) or a path chosen from the application window can be pasted at any time using the shortcut Ctrl + B. Within the application, paths can be edited. Using a checkbox, users can choose between edit modes (save as a new path / edit). An edited path (or a newly saved one) that matches an existing path is moved to the top of the list and is not added again to avoid duplicates. 

## Screenshots

![2](https://github.com/ZuzannaZawartka/system-paths-manager/assets/60311564/bdc94a49-7783-4061-bc95-6c0b3efff573)


![1](https://github.com/ZuzannaZawartka/system-paths-manager/assets/60311564/10043f46-88ee-4aa8-a6bf-d8b524a0e805)


## Application Components

### AppManager (Application Manager)

- `MainWindow`: Manages the user interface and serves as the main window of the application.

- `KeyListener`: Manages keyboard shortcuts and the copying and pasting of content.

- `ClipboardManager`: Manages clipboard content and acts as a bridge between the UI and the database.

## Requirements

1. **Python**: Install Python 3.x. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Libraries**: Install required libraries using the following command:

   ```bash
   cd project
   pip install -r requirements.txt
   ```
   
	Application required:
	- pynput
	- pyperclip
	- PyQt5

	- PyAutoGui
## Running the Application

1. **Download the code**: Copy the Paths Manager application code.
   ```bash
     git clone https://github.com/ZuzannaZawartka/system-paths-manager.git
     ```
2. **Run from Terminal or Command Prompt**:

   - Open a terminal (Linux/Mac) or command prompt (Windows).

   - Navigate to the directory containing the `main.py` file of the Clipboard Manager application
     ```bash
     cd project
     ```

   - Install required libraries 
		```bash
	   pip install -r requirements.txt
     ```
   - Run the application by entering the command:

     ```bash
     python main.py
     ```

## How to Use the Application

1. Launch the application.

2. The application will appear as an icon in the bottom right corner of the screen (Open the application by clicking the icon or using the Ctrl + Left Shift shortcut )

3. Use keyboard shortcuts (e.g., Ctrl+C, Ctrl+B) to manage the clipboard. Each path copied using Ctrl+C will appear in the application window.

4. Add, remove, and edit stored items using the user interface.
