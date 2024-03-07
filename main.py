import tkinter as tk
import csv


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


def create_and_place_braille_cells(master, braille_cells, max_columns):
    for i, cell in enumerate(braille_cells):
        row_index = int(i / max_columns)
        column_index = i % max_columns
        cell.grid(row=row_index, column=column_index)


# Function to load Braille character configurations from a CSV file
def load_braille_configurations(file_path):
    braille_configurations = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            char = row[0]
            dots = [bool(int(dot)) for dot in row[1:]]
            braille_configurations[char] = dots
    return braille_configurations


# Convert character to single or multiple Braille cells
def char_to_braille(char, braille_configurations):
    sequence = []
    if char.isalpha() and char.isupper():  # Check if the character is an uppercase letter
        sequence.append({"braille_letter": braille_configurations['Capital'],
                         "symbol": "Capital"})  # Add the capital indicator

        sequence.append({"braille_letter": braille_configurations[char.lower()],
                         "symbol": char.lower()})  # Add the lowercase letter

    elif char.isdigit():  # Check if the character is a digit
        sequence.append({"braille_letter": braille_configurations['#'],
                         "symbol": "#"})  # Add the number indicator
        sequence.append({"braille_letter": braille_configurations[char],
                         "symbol": char})  # Add the digit

    elif char in braille_configurations:  # If character fits none of the above categories, but is in the alphabet
        sequence.append({"braille_letter": braille_configurations[char],
                         "symbol": char})

    return sequence


# Function to convert a string to a list of Braille cells using data from CSV file
def string_to_braille_cells(string, braille_configurations):
    braille_cells = []
    for char in string:
        sequence = char_to_braille(char, braille_configurations)
        for letter in sequence:
            cell = BrailleCellWidget(root, letter["braille_letter"], letter["symbol"])
            cell.update_display()
            braille_cells.append(cell)
    return braille_cells


braille_alphabet = load_braille_configurations('braille/alphabet.csv')
special_characters = load_braille_configurations('braille/special_characters.csv')
combined_alphabet = {**braille_alphabet, **special_characters}

# Create a Tkinter window
root = tk.Tk()
root.title("Braille Cells")

test_string = "Hi! This is a test of numbers 12345"

max_columns = 20

# Convert the string to a list of Braille cells
cells = string_to_braille_cells(test_string, combined_alphabet)
create_and_place_braille_cells(root, cells, max_columns)

# Run the Tkinter event loop
root.mainloop()
