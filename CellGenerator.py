from gen.uncontracted_brailleVisitor import uncontracted_brailleVisitor
from gen.uncontracted_brailleParser import uncontracted_brailleParser

from BrailleCells.Cell import *


class CellGenerator(uncontracted_brailleVisitor):
    def __init__(self):
        self.signs = []

    def generate_cells(self, text):
        self.visitText(text)

        cells = []

        for sign in self.signs:
            for cell in sign.cells:
                cells.append(cell)
        return cells

    def visitSpace(self, ctx: uncontracted_brailleParser.SpaceContext):
        self.signs.append(Punctuation(ctx.getChild(0).getText()))
        return

    def visitCapital_sequence(self, ctx: uncontracted_brailleParser.Capital_sequenceContext):
        self.signs.append(CapitalWordIndicator())
        return self.visitChildren(ctx)

    def visitCapitals_terminator(self, ctx: uncontracted_brailleParser.Capitals_terminatorContext):
        self.signs.append(CapitalsTerminator())
        return self.visitChildren(ctx)

    def visitNumeral_sequence(self, ctx: uncontracted_brailleParser.Numeral_sequenceContext):
        self.signs.append(NumeralIndicator())
        return self.visitChildren(ctx)

    def visitPunctuation(self, ctx: uncontracted_brailleParser.PunctuationContext):
        self.signs.append(Punctuation(ctx.getChild(0).getText()))
        return

    def visitGrouping_punctuation(self, ctx: uncontracted_brailleParser.Grouping_punctuationContext):
        self.signs.append(GroupingPunctuation(ctx.getChild(0).getText()))
        return

    def visitOp_and_comp(self, ctx: uncontracted_brailleParser.Op_and_compContext):
        self.signs.append(OpAndComp(ctx.getChild(0).getText()))
        return

    def visitUppercase(self, ctx: uncontracted_brailleParser.UppercaseContext):
        self.signs.append(Alphabetic(ctx.getChild(0).getText()))
        return

    def visitLowercase(self, ctx: uncontracted_brailleParser.LowercaseContext):
        self.signs.append(Alphabetic(ctx.getChild(0).getText()))
        return

    def visitDigit(self, ctx: uncontracted_brailleParser.DigitContext):
        self.signs.append(Numeral(ctx.getChild(0).getText()))
        return
