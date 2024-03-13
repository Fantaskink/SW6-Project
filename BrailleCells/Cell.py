class Cell:
    def __init__(self, dots, character):
        self.dots = dots
        self.character = character

    def __str__(self):
        return f"Braille Cell: {self.character}"


class CapitalWordIndicator:
    def __init__(self):
        self.cells = [Cell([0, 0, 0, 0, 0, 1], ","), Cell([0, 0, 0, 0, 0, 1], ",")]

    def __str__(self):
        return f"Capital Word Indicator: {self.cells}"


class CapitalTerminator:
    def __init__(self):
        self.cells = [Cell([0, 0, 0, 0, 0, 1], ","), Cell([0, 0, 1, 0, 0, 0], "'")]

    def __str__(self):
        return f"Capital Terminator: {self.cells}"


class CapitalFirstLetter:
    def __init__(self):
        self.cells = [Cell([0, 0, 0, 0, 0, 1], ",")]

    def __str__(self):
        return f"Capital First Letter: {self.cells}"


class Alphabetic:
    def __init__(self, character):
        self.cells = [Cell(self.get_dots(character.lower()), character.lower())]

    def __str__(self):
        return f"Alphabetic: {self.cells}"

    def get_dots(self, character):
        binary_dict = {
            'a': [1, 0, 0, 0, 0, 0],
            'b': [1, 1, 0, 0, 0, 0],
            'c': [1, 0, 0, 1, 0, 0],
            'd': [1, 0, 0, 1, 1, 0],
            'e': [1, 0, 0, 0, 1, 0],
            'f': [1, 1, 0, 1, 0, 0],
            'g': [1, 1, 0, 1, 1, 0],
            'h': [1, 1, 0, 0, 1, 0],
            'i': [0, 1, 0, 1, 0, 0],
            'j': [0, 1, 0, 1, 1, 0],
            'k': [1, 0, 1, 0, 0, 0],
            'l': [1, 1, 1, 0, 0, 0],
            'm': [1, 0, 1, 1, 0, 0],
            'n': [1, 0, 1, 1, 1, 0],
            'o': [1, 0, 1, 0, 1, 0],
            'p': [1, 1, 1, 1, 0, 0],
            'q': [1, 1, 1, 1, 1, 0],
            'r': [1, 1, 1, 0, 1, 0],
            's': [0, 1, 1, 1, 0, 0],
            't': [0, 1, 1, 1, 1, 0],
            'u': [1, 0, 1, 0, 0, 1],
            'v': [1, 1, 1, 0, 0, 1],
            'w': [0, 1, 0, 1, 1, 1],
            'x': [1, 0, 1, 1, 0, 1],
            'y': [1, 0, 1, 1, 1, 1],
            'z': [1, 0, 1, 0, 1, 1]
        }

        return binary_dict[character]


class NumeralIndicator:
    def __init__(self):
        self.cells = [Cell([0, 0, 1, 1, 1, 1], "#")]

    def __str__(self):
        return f"Numeral Indicator: {self.cells}"


class Punctuation:
    def __init__(self, character):
        dots = self.get_dots(character)
        if isinstance(dots[0], list):
            self.cells = [Cell(dots[0], character), Cell(dots[1], character)]
        else:
            self.cells = [Cell(self.get_dots(character), character)]

    def __str__(self):
        return f"Punctuation Cell: {self.cells}"

    def get_dots(self, character):
        binary_dict = {
            " ": [0, 0, 0, 0, 0, 0],
            ",": [0, 1, 0, 0, 0, 0],
            ".": [0, 1, 0, 1, 1, 0],
            "‘": [0, 0, 1, 0, 0, 0],
            ":": [0, 1, 0, 0, 1, 0],
            "!": [0, 1, 1, 0, 1, 0],
            "-": [0, 0, 1, 0, 0, 1],
            "?": [0, 1, 1, 0, 0, 1],
            ";": [0, 1, 1, 0, 0, 0],
            "/": [[0, 0, 0, 1, 1, 1, ], [0, 0, 1, 1, 0, 0]],
            "\\": [[0, 0, 0, 1, 1, 1, ], [1, 0, 0, 0, 0, 1]]
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
            "(": [[0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1]],
            ")": [[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0]],
            "[": [[0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 1]],
            "]": [[0, 0, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0]],
            "{": [[0, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 1]],
            "}": [[0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0]],
        }
        return binary_dict[character]


class Numeral:
    def __init__(self, character):
        self.cells = [Cell(self.get_dots(character), character)]

    def __str__(self):
        return f"Numeral: {self.cells}"

    def get_dots(self, character):
        binary_dict = {
            '1': [1, 0, 0, 0, 0, 0],
            '2': [1, 1, 0, 0, 0, 0],
            '3': [1, 0, 0, 1, 0, 0],
            '4': [1, 0, 0, 1, 1, 0],
            '5': [1, 0, 0, 0, 1, 0],
            '6': [1, 1, 0, 1, 0, 0],
            '7': [1, 1, 0, 1, 1, 0],
            '8': [1, 1, 0, 0, 1, 0],
            '9': [0, 1, 0, 1, 0, 0],
            '0': [0, 1, 0, 1, 1, 0]
        }
        return binary_dict[character]
