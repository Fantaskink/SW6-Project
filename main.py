import tkinter as tk
from antlr4 import *
from gen.uncontracted_brailleLexer import uncontracted_brailleLexer
from gen.uncontracted_brailleParser import uncontracted_brailleParser
from CellGenerator import CellGenerator


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
        self.geometry("800x600")
        self.cell_pages = []
        self.current_page = 0
        self.render_braille_cells()

    def render_braille_cells(self):
        test_string = "This is a test of [ and ] and 123 and / : lorem ipsum dolor sit amet consectetur adipiscing elit"

        # Convert the string to a list of Braille cells
        cells = get_cells(test_string)
        cell_widgets = convert_to_widgets(cells)

        max_columns = 20
        max_rows = 1
        max_cells = max_columns * max_rows

        # Create a list of pages, each page containing max_cells number of cells
        self.cell_pages = [cell_widgets[i:i + max_cells] for i in range(0, len(cell_widgets), max_cells)]

        # Create next and previous buttons
        self.next_button = tk.Button(self, text=">", command=self.next_page)
        self.previous_button = tk.Button(self, text="<", command=self.previous_page)

        self.cells_on_page = self.cell_pages[self.current_page]

        # Place the Braille cells on the window
        self.update_display()

        self.next_button.grid(row=max_rows + 1, column=9)
        self.previous_button.grid(row=max_rows + 1, column=0)

    def next_page(self):
        self.current_page = min(self.current_page + 1, len(self.cell_pages) - 1)
        self.update_display()

    def previous_page(self):
        self.current_page = max(0, self.current_page - 1)
        self.update_display()

    def update_display(self):
        for widget in self.winfo_children():
            if widget not in (self.next_button, self.previous_button):
                widget.grid_forget()

        max_columns = 20
        max_rows = 1
        max_cells = max_columns * max_rows

        self.cells_on_page = self.cell_pages[self.current_page]

        for index, cell in enumerate(self.cells_on_page):
            row_index = index // max_columns
            column_index = index % max_columns
            cell.grid(row=row_index, column=column_index)
            cell.update_display()  # Update the display of the Braille cell widget
            cell.update()

        if len(self.cells_on_page) < max_cells:
            for i in range(len(self.cells_on_page), max_cells):
                row_index = i // max_columns
                column_index = i % max_columns
                empty_cell = BrailleCellWidget(self, [False] * 6, " ")
                empty_cell.grid(row=row_index, column=column_index)


def main():
    window = MainWindow()
    window.mainloop()


if __name__ == "__main__":
    main()
