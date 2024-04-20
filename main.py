import tkinter as tk
from antlr4 import *
from gen.uncontracted_brailleLexer import uncontracted_brailleLexer
from gen.uncontracted_brailleParser import uncontracted_brailleParser
from CellGenerator import CellGenerator
from tts import pronounce_letters
import socket
import threading

PORT = 12345
MAX_ROWS = 1
MAX_COLUMNS = 20


class SocketHandler:
    def __init__(self, shared_string, main_window):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', PORT))
        self.sock.listen(1)

        self.shared_string = shared_string
        self.main_window = main_window

    def listen_for_data(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                data = conn.recv(1024)
                if not data:
                    break
                string = data.decode('utf-8')
                if len(string) > 0:
                    print(string)
                    self.shared_string = string
                    self.main_window.render_braille_cells(string)
            except Exception as e:
                print(f"Error: {e}")
                print("Attempting to reconnect...")
                continue
            finally:
                conn.close()



def get_cells(string):
    input_stream = InputStream(string)
    lexer = uncontracted_brailleLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = uncontracted_brailleParser(token_stream)
    ast = parser.text()
    cell_generator = CellGenerator()

    cells = cell_generator.generate_cells(ast)
    return cells


def convert_to_widgets(cells):
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

    def create_labels(self):
        # Create labels for each dot
        self.dot_labels = []
        for i in range(6):
            label = tk.Label(self, text="○", font=("Arial", 20))
            label.grid(row=i % 3, column=i // 3)
            self.dot_labels.append(label)

        # Create label for character
        character_label = tk.Label(self, text=self.character, width=5)
        character_label.grid(row=3, column=0, columnspan=2)  # Span two columns

    def update_display(self):
        # Update the display based on the state of the dots
        dot_symbols = ["○", "●"]  # Not raised and raised dot symbols
        for i in range(6):
            if i + 1 in self.dots:
                self.dot_labels[i]["text"] = dot_symbols[1]
            else:
                self.dot_labels[i]["text"] = dot_symbols[0]

    def __str__(self):
        return f"Braille Cell: {self.character} {self.dots}"


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Braille Cells")
        self.geometry("1100x200")
        self.cell_pages = []
        self.cells_on_page = []
        self.current_page = 0

        self.updates_blocked = False

        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=1, column=0, columnspan=MAX_COLUMNS)

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

        self.shared_string = ""

        self.socket_handler = SocketHandler(self.shared_string, self)
        threading.Thread(target=self.socket_handler.listen_for_data).start()

        self.render_braille_cells(self.shared_string)

    def get_empty_widgets(self):
        widgets = []
        for i in range(MAX_ROWS):
            for j in range(MAX_COLUMNS):
                cell = BrailleCellWidget(self, [], " ")
                cell.grid(row=i, column=j)
                widgets.append(cell)
        return widgets

    def render_braille_cells(self, string):
        if self.updates_blocked:
            return
        self.label.config(text=string)

        self.current_page = 0

        # Convert the string to a list of Braille cells
        cells = get_cells(string)
        cell_widgets = convert_to_widgets(cells)

        if not cell_widgets:
            cell_widgets = self.get_empty_widgets()

        max_cells = MAX_ROWS * MAX_COLUMNS

        # Create a list of pages, each page containing max_cells number of cells
        self.cell_pages = [cell_widgets[i:i + max_cells] for i in range(0, len(cell_widgets), max_cells)]

        # Create next and previous buttons
        self.cells_on_page = self.cell_pages[self.current_page]

        # Place the Braille cells on the window
        self.update_display()

    def next_page(self):
        self.current_page = min(self.current_page + 1, len(self.cell_pages) - 1)
        self.update_display()

    def previous_page(self):
        self.current_page = max(0, self.current_page - 1)
        self.update_display()

    def text_to_speech(self):
        text = self.label.cget("text")
        if len(text) == 0:
            return
        threading.Thread(target=pronounce_letters, args=(text,)).start()

    def block_updates(self):
        self.updates_blocked = not self.updates_blocked
        self.block_updates_button.config(text="Locked" if self.updates_blocked else "Unlocked")

    def update_display(self):
        # Remove all cells from the grid
        for widget in self.grid_slaves():
            if isinstance(widget, BrailleCellWidget):
                widget.grid_forget()

        # Update the cells on the current page
        self.cells_on_page = self.cell_pages[self.current_page]

        # Update the display of each cell
        for index, cell in enumerate(self.cells_on_page):
            row_index = index // MAX_COLUMNS
            column_index = index % MAX_COLUMNS
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
