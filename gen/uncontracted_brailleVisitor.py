# Generated from /Users/johan/GitHub/SW6-Project/ANTLR4/uncontracted_braille.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .uncontracted_brailleParser import uncontracted_brailleParser
else:
    from uncontracted_brailleParser import uncontracted_brailleParser

# This class defines a complete generic visitor for a parse tree produced by uncontracted_brailleParser.

class uncontracted_brailleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by uncontracted_brailleParser#text.
    def visitText(self, ctx:uncontracted_brailleParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#nonword.
    def visitNonword(self, ctx:uncontracted_brailleParser.NonwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#word.
    def visitWord(self, ctx:uncontracted_brailleParser.WordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#sequence.
    def visitSequence(self, ctx:uncontracted_brailleParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#capital_first_letter.
    def visitCapital_first_letter(self, ctx:uncontracted_brailleParser.Capital_first_letterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#capital_sequence.
    def visitCapital_sequence(self, ctx:uncontracted_brailleParser.Capital_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#numeral_sequence.
    def visitNumeral_sequence(self, ctx:uncontracted_brailleParser.Numeral_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#capital_terminator.
    def visitCapital_terminator(self, ctx:uncontracted_brailleParser.Capital_terminatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#lowercase_sequence.
    def visitLowercase_sequence(self, ctx:uncontracted_brailleParser.Lowercase_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#punctuation.
    def visitPunctuation(self, ctx:uncontracted_brailleParser.PunctuationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#grouping_punctuation.
    def visitGrouping_punctuation(self, ctx:uncontracted_brailleParser.Grouping_punctuationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#op_and_comp.
    def visitOp_and_comp(self, ctx:uncontracted_brailleParser.Op_and_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#currency_and_measurement.
    def visitCurrency_and_measurement(self, ctx:uncontracted_brailleParser.Currency_and_measurementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#lowercase.
    def visitLowercase(self, ctx:uncontracted_brailleParser.LowercaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#uppercase.
    def visitUppercase(self, ctx:uncontracted_brailleParser.UppercaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by uncontracted_brailleParser#digit.
    def visitDigit(self, ctx:uncontracted_brailleParser.DigitContext):
        return self.visitChildren(ctx)



del uncontracted_brailleParser