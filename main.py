import tkinter as tk
from antlr4 import *
from gen.uncontracted_brailleLexer import uncontracted_brailleLexer
from gen.uncontracted_brailleParser import uncontracted_brailleParser
from CellGenerator import CellGenerator
import socket
import threading


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
            self.dot_labels[i]["text"] = dot_symbols[self.dots[i]]

    def __str__(self):
        return f"Braille Cell: {self.character} {self.dots}"


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Braille Cells")
        self.geometry("1150x200")
        self.cell_pages = []
        self.cells_on_page = []
        self.current_page = 0

        self.max_rows = 1
        self.max_columns = 20

        self.next_button = tk.Button(self, text=">", command=self.next_page)
        self.previous_button = tk.Button(self, text="<", command=self.previous_page)
        self.next_button.grid(row=self.max_rows + 1, column=self.max_columns - 1)
        self.previous_button.grid(row=self.max_rows + 1, column=0)

        self.label = tk.Label(self, text="")
        self.label.grid(row=self.max_rows + 2, column=0, columnspan=20, padx=10, pady=10)

        self.render_braille_cells("")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', 12345))
        self.sock.listen(1)

        threading.Thread(target=self.listen_for_data).start()

    def listen_for_data(self):
        conn, addr = self.sock.accept()

        while True:
            data = conn.recv(1024)

            if not data:
                break

            string = data.decode('utf-8')

            if len(string) > 0:
                print(string)

            self.render_braille_cells(string)
        conn.close()

    def get_empty_widgets(self):
        widgets = []
        for i in range(self.max_rows):
            for j in range(self.max_columns):
                cell = BrailleCellWidget(self, [False] * 6, " ")
                cell.grid(row=i, column=j)
                widgets.append(cell)
        return widgets

    def render_braille_cells(self, string):
        self.label.config(text=string)

        self.current_page = 0

        # Convert the string to a list of Braille cells
        cells = get_cells(string)
        cell_widgets = convert_to_widgets(cells)

        if not cell_widgets:
            cell_widgets = self.get_empty_widgets()

        max_cells = self.max_rows * self.max_columns

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

    def update_display(self):
        for widget in self.winfo_children():
            if widget not in (self.next_button, self.previous_button, self.label):
                widget.grid_forget()

        self.cells_on_page = self.cell_pages[self.current_page]

        for index, cell in enumerate(self.cells_on_page):
            row_index = index // self.max_columns
            column_index = index % self.max_columns
            cell.grid(row=row_index, column=column_index)
            cell.update_display()  # Update the display of the Braille cell widget
            # cell.update()

        max_cells = self.max_rows * self.max_columns

        if len(self.cells_on_page) < max_cells:
            for i in range(len(self.cells_on_page), max_cells):
                row_index = i // self.max_columns
                column_index = i % self.max_columns
                empty_cell = BrailleCellWidget(self, [False] * 6, " ")
                empty_cell.grid(row=row_index, column=column_index)


def main():
    window = MainWindow()
    window.mainloop()


if __name__ == "__main__":
    main()
