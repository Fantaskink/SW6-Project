class Cell:
    def __init__(self, dots, character):
        self.dots = dots
        self.character = character

    def __str__(self):
        return f"Braille Cell: {self.character}"


class CapitalWordIndicator:
    def __init__(self):
        self.cells = [Cell([6], ","), Cell([6], ",")]

    def __str__(self):
        return f"Capital Word Indicator: {self.cells}"


class CapitalsTerminator:
    def __init__(self):
        self.cells = [Cell([6], ","), Cell([3], "'")]

    def __str__(self):
        return f"Capital Terminator: {self.cells}"


class CapitalFirstLetter:
    def __init__(self):
        self.cells = [Cell([6], ",")]

    def __str__(self):
        return f"Capital First Letter: {self.cells}"


class Alphabetic:
    def __init__(self, character):
        self.cells = [Cell(self.get_dots(character.lower()), character.lower())]

    def __str__(self):
        return f"Alphabetic: {self.cells}"

    def get_dots(self, character):
        binary_dict = {
            'a': [1],
            'b': [1, 2],
            'c': [1, 4],
            'd': [1, 4, 5],
            'e': [1, 5],
            'f': [1, 2, 4],
            'g': [1, 2, 4, 5],
            'h': [1, 2, 5],
            'i': [2, 4],
            'j': [2, 4, 5],
            'k': [1, 3],
            'l': [1, 2, 3],
            'm': [1, 3, 4],
            'n': [1, 3, 4, 5],
            'o': [1, 3, 5],
            'p': [1, 2, 3, 4],
            'q': [1, 2, 3, 4, 5],
            'r': [1, 2, 3, 5],
            's': [2, 3, 4],
            't': [2, 3, 4, 5],
            'u': [1, 3, 6],
            'v': [1, 2, 3, 6],
            'w': [2, 4, 5, 6],
            'x': [1, 3, 4, 6],
            'y': [1, 3, 4, 5, 6],
            'z': [1, 3, 5, 6]
        }

        return binary_dict[character]


class NumeralIndicator:
    def __init__(self):
        self.cells = [Cell([3, 4, 5, 6], "#")]

    def __str__(self):
        return f"Numeral Indicator: {self.cells}"


class Grade1Indicator:
    def __init__(self):
        self.cells = [Cell([5, 6], "")]

    def __str__(self):
        return f"Grade 1 Indicator: {self.cells}"


class Punctuation:
    def __init__(self, character):
        dots = self.get_dots(character)
        if not dots: # If character is a space
            self.cells = [Cell([], character)]
        elif isinstance(dots[0], list): # If character has multiple cells
            self.cells = [Cell(dots[0], character), Cell(dots[1], character)]
        else: # If character has only one cell
            self.cells = [Cell(self.get_dots(character), character)]

    def __str__(self):
        return f"Punctuation Cell: {self.cells}"

    def get_dots(self, character):
        binary_dict = {
            " ": [],
            ",": [2],
            ".": [2, 4, 5],
            "'": [3],
            "‘": [3],
            ":": [2, 5],
            "!": [2, 3, 5],
            "-": [3, 6],
            "_": [[4, 6], [3, 6]],
            "?": [2, 3, 6],
            ";": [2, 3],
            "/": [[4, 5, 6], [3, 4]],
            "\\": [[4, 5, 6], [1, 6]]
        }
        return binary_dict[character]


class GroupingPunctuation:
    def __init__(self, character):
        dots = self.get_dots(character)
        if isinstance(dots[0], list):
            self.cells = [Cell(dots[0], character), Cell(dots[1], character)]
        else:
            self.cells = [Cell(self.get_dots(character), character)]

    def __str__(self):
        return f"Grouping Punctuation: {self.cells}"

    def get_dots(self, character):
        binary_dict = {
            "(": [[5], [1, 2, 6]],
            ")": [[5], [3, 4, 5]],
            "[": [[4, 6], [1, 2, 6]],
            "]": [[4, 6], [3, 4, 5]],
            "{": [[4, 5, 6], [1, 2, 6]],
            "}": [[4, 5, 6], [3, 4, 5]],
            "<": [[4], [1, 2, 6]],
            ">": [[4], [3, 4, 5]],
        }
        return binary_dict[character]


class Numeral:
    def __init__(self, character):
        self.cells = [Cell(self.get_dots(character), character)]

    def __str__(self):
        return f"Numeral: {self.cells}"

    def get_dots(self, character):
        binary_dict = {
            '1': [1],
            '2': [1, 2],
            '3': [1, 4],
            '4': [1, 4, 5],
            '5': [1, 5],
            '6': [1, 2, 4],
            '7': [1, 2, 4, 5],
            '8': [1, 2, 5],
            '9': [2, 4],
            '0': [2, 4, 5]
        }
        return binary_dict[character]


class OpAndComp:
    def __init__(self, character):
        dots = self.get_dots(character)
        if isinstance(dots[0], list):
            self.cells = [Cell(dots[0], character), Cell(dots[1], character)]
        else:
            self.cells = [Cell(self.get_dots(character), character)]

    def __str__(self):
        return f"OpAndComp: {self.cells}"

    def get_dots(self, character):
        binary_dict = {
            '+': [[5], [2, 3, 5]],
            '*': [[5], [3, 5]],
            '=': [[5], [2, 3, 5, 6]]
        }
        return binary_dict[character]
