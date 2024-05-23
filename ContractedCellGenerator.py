from gen.contracted_braille_parserVisitor import contracted_braille_parserVisitor
from gen.contracted_braille_parser import contracted_braille_parser

from BrailleCells.Cell import *


class ContractedCellGenerator(contracted_braille_parserVisitor):
    def __init__(self):
        self.signs = []

    def generate_cells(self, text):
        self.visitText(text)

        cells = []

        for sign in self.signs:
            for cell in sign.cells:
                cells.append(cell)
        return cells

    def visitSpace(self, ctx: contracted_braille_parser.SpaceContext):
        self.signs.append(Punctuation(ctx.getChild(0).getText()))
        return

    def visitCapital_sequence(self, ctx: contracted_braille_parser.Capital_sequenceContext):
        self.signs.append(CapitalWordIndicator())
        return self.visitChildren(ctx)

    def visitCapital_letter(self, ctx: contracted_braille_parser.Capital_letterContext):
        self.signs.append(CapitalFirstLetter())
        return self.visitChildren(ctx)

    def visitCapitals_terminator(self, ctx: contracted_braille_parser.Capitals_terminatorContext):
        self.signs.append(CapitalsTerminator())
        return self.visitChildren(ctx)

    def visitGrade_1_terminator(self, ctx: contracted_braille_parser.Grade_1_terminatorContext):
        self.signs.append(Grade1Terminator())
        return self.visitChildren(ctx)

    def visitNumeral_sequence(self, ctx: contracted_braille_parser.Numeral_sequenceContext):
        self.signs.append(NumeralIndicator())
        return self.visitChildren(ctx)

    def visitNumeral_separator(self, ctx: contracted_braille_parser.Numeral_separatorContext):
        self.signs.append(Punctuation(ctx.getChild(0).getText()))

    def visitPunctuation(self, ctx: contracted_braille_parser.PunctuationContext):
        self.signs.append(Punctuation(ctx.getChild(0).getText()))
        return

    def visitGrouping_punctuation(self, ctx: contracted_braille_parser.Grouping_punctuationContext):
        self.signs.append(GroupingPunctuation(ctx.getChild(0).getText()))
        return

    def visitAlphabetic_wordsign(self, ctx:contracted_braille_parser.Alphabetic_wordsignContext):
        self.signs.append(AlphabeticWordSign(ctx.getChild(0).getText()))
        return

    def visitOp_and_comp(self, ctx: contracted_braille_parser.Op_and_compContext):
        self.signs.append(OpAndComp(ctx.getChild(0).getText()))
        return

    def visitUppercase(self, ctx: contracted_braille_parser.UppercaseContext):
        self.signs.append(Alphabetic(ctx.getChild(0).getText()))
        return

    def visitLowercase(self, ctx: contracted_braille_parser.LowercaseContext):
        self.signs.append(Alphabetic(ctx.getChild(0).getText()))
        return

    def visitDigit(self, ctx: contracted_braille_parser.DigitContext):
        self.signs.append(Numeral(ctx.getChild(0).getText()))
        return
