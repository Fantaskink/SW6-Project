import tkinter as tk
from antlr4 import *
from gen.uncontracted_brailleLexer import uncontracted_brailleLexer
from gen.uncontracted_brailleParser import uncontracted_brailleParser
from gen.contracted_braille_lexer import contracted_braille_lexer
from gen.contracted_braille_parser import contracted_braille_parser
from UncontractedCellGenerator import UncontractedCellGenerator
from ContractedCellGenerator import ContractedCellGenerator
from tts import read_text
import socket
import threading
import json

PORT = 12345
MAX_ROWS = 1
MAX_COLUMNS = 20
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 250

TEXT = 0
VSCODE = 1


def get_target_string(json_data: dict) -> str:
    data_type = json_data['type']

    if data_type == 'vscode':
        line_number = json_data['line_number']
        line_text = json_data['line_text']
        target_string = f"{line_number}: {line_text}"
        return target_string
    elif data_type == 'text':
        return json_data['content']


class SocketHandler:
    def __init__(self, main_window):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('localhost', PORT))
        self.sock.listen(1)

        self.main_window = main_window

    def listen_for_data(self):
        try:
            conn, addr = self.sock.accept()
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                json_data = json.loads(data.decode('utf-8'))
                if json_data:
                    self.main_window.render_braille_cells(json_data)
        except Exception as e:
            print(f"Error: {e}")
            print("Attempting to reconnect...")
        finally:
            if conn:
                conn.close()
            self.sock.close()


def get_cells(data: dict) -> list:
    string = get_target_string(data)
    is_contracted = data['is_contracted']

    input_stream = InputStream(string)

    if is_contracted:
        cell_generator = ContractedCellGenerator()
        lexer = contracted_braille_lexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = contracted_braille_parser(token_stream)
    else:
        cell_generator = UncontractedCellGenerator()
        lexer = uncontracted_brailleLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = uncontracted_brailleParser(token_stream)

    ast = parser.text()

    cells = cell_generator.generate_cells(ast)
    return cells


def convert_to_widgets(cells: list) -> list:
    widgets = []
    for cell in cells:
        widgets.append(BrailleCellWidget(None, cell.dots, cell.character))
    return widgets


class BrailleCellWidget(tk.Frame):
    def __init__(self, master, dots, character):
        super().__init__(master, borderwidth=2, relief="solid")
        self.dot_labels = None
        self.dots = dots
        self.character = character
        self.create_labels()

    def create_labels(self) -> None:
        # Create labels for each dot
        self.dot_labels = []
        for i in range(6):
            label = tk.Label(self, text="○", font=("Arial", 20))
            label.grid(row=i % 3, column=i // 3)
            self.dot_labels.append(label)

        # Create label for character
        character_label = tk.Label(self, text=self.character, width=5)
        character_label.grid(row=3, column=0, columnspan=2)  # Span two columns

    def update_display(self) -> None:
        # Update the display based on the state of the dots
        dot_symbols = ["○", "●"]  # Not raised and raised dot symbols
        for i in range(6):
            if i + 1 in self.dots:
                self.dot_labels[i]["text"] = dot_symbols[1]
            else:
                self.dot_labels[i]["text"] = dot_symbols[0]

    def __str__(self) -> str:
        return f"Braille Cell: {self.character} {self.dots}"


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulated Braille Display")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.cell_pages = []
        self.cells_on_page = []
        self.current_page = 0

        self.updates_blocked = False

        self.context = TEXT

        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=MAX_ROWS + 1, column=0, columnspan=MAX_COLUMNS)

        self.next_button = tk.Button(self.button_frame, text=">", command=self.next_page)
        self.previous_button = tk.Button(self.button_frame, text="<", command=self.previous_page)
        self.next_button.grid(row=MAX_ROWS + 1, column=MAX_COLUMNS - 1, sticky=tk.W)
        self.previous_button.grid(row=MAX_ROWS + 1, column=0, sticky=tk.E)

        self.tts_button = tk.Button(self.button_frame, text="TTS", command=self.text_to_speech)
        self.tts_button.grid(row=MAX_ROWS + 1, column=MAX_COLUMNS // 2, sticky=tk.W)

        self.block_updates_button = tk.Button(self.button_frame, text="Unlocked", command=self.block_updates)
        self.block_updates_button.grid(row=MAX_ROWS + 1, column=MAX_COLUMNS // 2 + 1, sticky=tk.E)

        self.label = tk.Label(self, text="")
        self.label.grid(row=MAX_ROWS + 2, column=0, columnspan=20, padx=10, pady=10)

        self.socket_handler = SocketHandler(self)
        threading.Thread(target=self.socket_handler.listen_for_data).start()

        empty_object = {
            "type": "text",
            "content": "",
            "is_contracted": False
        }

        self.render_braille_cells(empty_object)

    def get_empty_widgets(self) -> list:
        widgets = []
        for i in range(MAX_ROWS):
            for j in range(MAX_COLUMNS):
                cell = BrailleCellWidget(self, [], " ")
                cell.grid(row=i, column=j)
                widgets.append(cell)
        return widgets

    def render_braille_cells(self, data: dict) -> None:
        string = get_target_string(data)
        type = data['type']

        if type == 'vscode':
            self.context = VSCODE
        elif type == 'text':
            self.context = TEXT

        if self.updates_blocked:
            return
        self.label.config(text=string)

        self.current_page = 0

        # Convert the string to a list of Braille cells
        cells = get_cells(data)
        cell_widgets = convert_to_widgets(cells)

        if not cell_widgets:
            cell_widgets = self.get_empty_widgets()

        max_cells = MAX_ROWS * MAX_COLUMNS

        # Create a list of pages, each page containing max_cells number of cells
        self.cell_pages = [cell_widgets[i:i + max_cells] for i in range(0, len(cell_widgets), max_cells)]

        # Set the current page to the first page
        self.cells_on_page = self.cell_pages[self.current_page]

        # Place the Braille cells on the window
        self.update_display()

    def next_page(self) -> None:
        self.current_page = min(self.current_page + 1, len(self.cell_pages) - 1)
        self.update_display()

    def previous_page(self) -> None:
        self.current_page = max(0, self.current_page - 1)
        self.update_display()

    def text_to_speech(self) -> None:
        text = self.label.cget("text")

        phonetic = False

        if self.context == VSCODE:
            phonetic = True

        if len(text) == 0:
            return
        threading.Thread(target=read_text, args=(text, phonetic)).start()

    def block_updates(self) -> None:
        self.updates_blocked = not self.updates_blocked
        self.block_updates_button.config(text="Locked" if self.updates_blocked else "Unlocked")

    def update_display(self) -> None:
        # Remove all cells from the grid
        for widget in self.grid_slaves():
            if isinstance(widget, BrailleCellWidget):
                widget.grid_forget()

        # Update the cells on the current page
        self.cells_on_page = self.cell_pages[self.current_page]

        # Place the cells on the grid
        for cell_index, cell in enumerate(self.cells_on_page):
            row_index = cell_index // MAX_COLUMNS
            column_index = cell_index % MAX_COLUMNS
            cell.grid(row=row_index, column=column_index)
            cell.update_display()  # Update the display of the Braille cell widget

        # If there are fewer cells on the page than the maximum number of cells,
        # fill the rest of the page with empty cells
        max_cells = MAX_ROWS * MAX_COLUMNS
        if len(self.cells_on_page) < max_cells:
            for i in range(len(self.cells_on_page), max_cells):
                row_index = i // MAX_COLUMNS
                column_index = i % MAX_COLUMNS
                empty_cell = BrailleCellWidget(self, [False] * 6, " ")
                empty_cell.grid(row=row_index, column=column_index)

        # Update the window immediately
        self.update_idletasks()


def main():
    window = MainWindow()
    window.mainloop()


if __name__ == "__main__":
    main()
