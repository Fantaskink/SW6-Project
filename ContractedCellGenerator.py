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

    def visitAlphabetic_wordsign(self, ctx: contracted_braille_parser.Alphabetic_wordsignContext):
        if ctx.ALPHABETIC_WORDSIGN_F():
            self.signs.append(CapitalFirstLetter())
        if ctx.ALPHABETIC_WORDSIGN_C():
            self.signs.append(CapitalWordIndicator())
        self.signs.append(AlphabeticWordSign(ctx.getChild(0).getText()))
        return

    def visitStrong_wordsign(self, ctx: contracted_braille_parser.Strong_wordsignContext):
        if ctx.STRONG_WORDSIGN_F():
            self.signs.append(CapitalFirstLetter())
        if ctx.STRONG_WORDSIGN_C():
            self.signs.append(CapitalWordIndicator())
        self.signs.append(StrongWordsign(ctx.getChild(0).getText()))
        return

    def visitStrong_contraction_f(self, ctx: contracted_braille_parser.Strong_contraction_fContext):
        self.signs.append(CapitalFirstLetter())
        self.signs.append(StrongContraction(ctx.getChild(0).getText()))
        return

    def visitStrong_contraction_c(self, ctx: contracted_braille_parser.Strong_contraction_cContext):
        self.signs.append(StrongContraction(ctx.getChild(0).getText()))
        return

    def visitStrong_contraction_l(self, ctx: contracted_braille_parser.Strong_contraction_lContext):
        self.signs.append(StrongContraction(ctx.getChild(0).getText()))
        return

    def visitLower_wordsign(self, ctx:contracted_braille_parser.Lower_wordsignContext):
        if ctx.LOWER_WORDSIGN_F():
            self.signs.append(CapitalFirstLetter())
        if ctx.LOWER_WORDSIGN_C():
            self.signs.append(CapitalWordIndicator())
        self.signs.append(LowerWordsign(ctx.getChild(0).getText()))
        return

    def visitShortform(self, ctx:contracted_braille_parser.ShortformContext):
        if ctx.SHORTFORM_F():
            self.signs.append(CapitalFirstLetter())
        if ctx.SHORTFORM_C():
            self.signs.append(CapitalWordIndicator())
        self.signs.append(Shortform(ctx.getChild(0).getText()))
        return

    def visitStrong_groupsign_c(self, ctx:contracted_braille_parser.Strong_groupsign_cContext):
        self.signs.append(StrongGroupsign(ctx.getChild(0).getText()))
        return

    def visitStrong_groupsign_f(self, ctx:contracted_braille_parser.Strong_groupsign_fContext):
        self.signs.append(CapitalFirstLetter())
        self.signs.append(StrongGroupsign(ctx.getChild(0).getText()))
        return

    def visitStrong_groupsign_l(self, ctx:contracted_braille_parser.Strong_groupsign_lContext):
        self.signs.append(StrongGroupsign(ctx.getChild(0).getText()))
        return

    def visitStanding_alone_letter(self, ctx:contracted_braille_parser.Standing_alone_letterContext):
        # the dots for a, i and o do not have alphabetic wordsign meanings
        if ctx.getText().lower() not in ['a', 'i', 'o']:
            self.signs.append(Grade1SymbolIndicator())
        return self.visitChildren(ctx)

    def visitStanding_alone_connector(self, ctx:contracted_braille_parser.Standing_alone_connectorContext):
        self.signs.append(Punctuation(ctx.getChild(0).getText()))
        return

    def visitOp_and_comp(self, ctx: contracted_braille_parser.Op_and_compContext):
        self.signs.append(OpAndComp(ctx.getChild(0).getText()))
        return

    def visitLowercase_sequence(self, ctx:contracted_braille_parser.Lowercase_sequenceContext):
        string = ""
        for letter in ctx.children:
            string += letter.getText()

        shortform_letters = ['ab', 'ac', 'af', 'afw', 'alm', 'alt', 'alw']

        if string in shortform_letters:
            self.signs.append(Grade1SymbolIndicator())

        return self.visitChildren(ctx)

    def visitUppercase(self, ctx: contracted_braille_parser.UppercaseContext):
        self.signs.append(Alphabetic(ctx.getChild(0).getText()))
        return

    def visitLowercase(self, ctx: contracted_braille_parser.LowercaseContext):
        self.signs.append(Alphabetic(ctx.getChild(0).getText()))
        return

    def visitDigit(self, ctx: contracted_braille_parser.DigitContext):
        self.signs.append(Numeral(ctx.getChild(0).getText()))
        return
