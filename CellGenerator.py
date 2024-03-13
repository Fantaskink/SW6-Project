from gen.uncontracted_brailleVisitor import uncontracted_brailleVisitor
from gen.uncontracted_brailleParser import uncontracted_brailleParser

from BrailleCells.Cell import *


class CellGenerator(uncontracted_brailleVisitor):
    def __init__(self):
        self.symbols = []

    def generate_cells(self, text):
        self.visitText(text)

        cells = []

        for symbol in self.symbols:
            for cell in symbol.cells:
                cells.append(cell)
        return cells

    def visitCapital_first_letter(self, ctx: uncontracted_brailleParser.Capital_first_letterContext):
        self.symbols.append(CapitalFirstLetter())
        return self.visitChildren(ctx)

    def visitCapital_sequence(self, ctx: uncontracted_brailleParser.Capital_sequenceContext):
        self.symbols.append(CapitalWordIndicator())
        return self.visitChildren(ctx)

    def visitCapital_terminator(self, ctx: uncontracted_brailleParser.Capital_terminatorContext):
        self.symbols.append(CapitalTerminator())
        return self.visitChildren(ctx)

    def visitNumeral_sequence(self, ctx:uncontracted_brailleParser.Numeral_sequenceContext):
        self.symbols.append(NumeralIndicator())
        return self.visitChildren(ctx)

    def visitPunctuation(self, ctx:uncontracted_brailleParser.PunctuationContext):
        self.symbols.append(Punctuation(ctx.getChild(0).getText()))
        return

    def visitGrouping_punctuation(self, ctx:uncontracted_brailleParser.Grouping_punctuationContext):
        self.symbols.append(GroupingPunctuation(ctx.getChild(0).getText()))
        return

    def visitUppercase(self, ctx:uncontracted_brailleParser.UppercaseContext):
        self.symbols.append(Alphabetic(ctx.getChild(0).getText()))
        return

    def visitLowercase(self, ctx:uncontracted_brailleParser.LowercaseContext):
        self.symbols.append(Alphabetic(ctx.getChild(0).getText()))
        return

    def visitDigit(self, ctx:uncontracted_brailleParser.DigitContext):
        self.symbols.append(Numeral(ctx.getChild(0).getText()))
        return





