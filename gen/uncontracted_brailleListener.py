# Generated from /Users/johan/GitHub/SW6-Project/ANTLR4/uncontracted_braille.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .uncontracted_brailleParser import uncontracted_brailleParser
else:
    from uncontracted_brailleParser import uncontracted_brailleParser

# This class defines a complete listener for a parse tree produced by uncontracted_brailleParser.
class uncontracted_brailleListener(ParseTreeListener):

    # Enter a parse tree produced by uncontracted_brailleParser#text.
    def enterText(self, ctx:uncontracted_brailleParser.TextContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#text.
    def exitText(self, ctx:uncontracted_brailleParser.TextContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#nonword.
    def enterNonword(self, ctx:uncontracted_brailleParser.NonwordContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#nonword.
    def exitNonword(self, ctx:uncontracted_brailleParser.NonwordContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#word.
    def enterWord(self, ctx:uncontracted_brailleParser.WordContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#word.
    def exitWord(self, ctx:uncontracted_brailleParser.WordContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#sequence.
    def enterSequence(self, ctx:uncontracted_brailleParser.SequenceContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#sequence.
    def exitSequence(self, ctx:uncontracted_brailleParser.SequenceContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#capital_first_letter.
    def enterCapital_first_letter(self, ctx:uncontracted_brailleParser.Capital_first_letterContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#capital_first_letter.
    def exitCapital_first_letter(self, ctx:uncontracted_brailleParser.Capital_first_letterContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#capital_sequence.
    def enterCapital_sequence(self, ctx:uncontracted_brailleParser.Capital_sequenceContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#capital_sequence.
    def exitCapital_sequence(self, ctx:uncontracted_brailleParser.Capital_sequenceContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#numeral_sequence.
    def enterNumeral_sequence(self, ctx:uncontracted_brailleParser.Numeral_sequenceContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#numeral_sequence.
    def exitNumeral_sequence(self, ctx:uncontracted_brailleParser.Numeral_sequenceContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#capital_terminator.
    def enterCapital_terminator(self, ctx:uncontracted_brailleParser.Capital_terminatorContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#capital_terminator.
    def exitCapital_terminator(self, ctx:uncontracted_brailleParser.Capital_terminatorContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#lowercase_sequence.
    def enterLowercase_sequence(self, ctx:uncontracted_brailleParser.Lowercase_sequenceContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#lowercase_sequence.
    def exitLowercase_sequence(self, ctx:uncontracted_brailleParser.Lowercase_sequenceContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#punctuation.
    def enterPunctuation(self, ctx:uncontracted_brailleParser.PunctuationContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#punctuation.
    def exitPunctuation(self, ctx:uncontracted_brailleParser.PunctuationContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#grouping_punctuation.
    def enterGrouping_punctuation(self, ctx:uncontracted_brailleParser.Grouping_punctuationContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#grouping_punctuation.
    def exitGrouping_punctuation(self, ctx:uncontracted_brailleParser.Grouping_punctuationContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#op_and_comp.
    def enterOp_and_comp(self, ctx:uncontracted_brailleParser.Op_and_compContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#op_and_comp.
    def exitOp_and_comp(self, ctx:uncontracted_brailleParser.Op_and_compContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#currency_and_measurement.
    def enterCurrency_and_measurement(self, ctx:uncontracted_brailleParser.Currency_and_measurementContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#currency_and_measurement.
    def exitCurrency_and_measurement(self, ctx:uncontracted_brailleParser.Currency_and_measurementContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#lowercase.
    def enterLowercase(self, ctx:uncontracted_brailleParser.LowercaseContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#lowercase.
    def exitLowercase(self, ctx:uncontracted_brailleParser.LowercaseContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#uppercase.
    def enterUppercase(self, ctx:uncontracted_brailleParser.UppercaseContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#uppercase.
    def exitUppercase(self, ctx:uncontracted_brailleParser.UppercaseContext):
        pass


    # Enter a parse tree produced by uncontracted_brailleParser#digit.
    def enterDigit(self, ctx:uncontracted_brailleParser.DigitContext):
        pass

    # Exit a parse tree produced by uncontracted_brailleParser#digit.
    def exitDigit(self, ctx:uncontracted_brailleParser.DigitContext):
        pass



del uncontracted_brailleParser