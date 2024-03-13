# Generated from /Users/johan/GitHub/SW6-Project/ANTLR4/uncontracted_braille.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,3,1,3,1,3,1,3,3,3,54,8,3,1,
        4,1,4,5,4,58,8,4,10,4,12,4,61,9,4,1,4,1,4,1,4,3,4,66,8,4,1,5,1,5,
        4,5,70,8,5,11,5,12,5,71,1,5,1,5,3,5,76,8,5,1,6,4,6,79,8,6,11,6,12,
        6,80,1,6,1,6,1,6,3,6,86,8,6,1,7,1,7,1,8,4,8,91,8,8,11,8,12,8,92,
        1,8,1,8,1,8,3,8,98,8,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,
        1,13,1,14,1,14,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,0,4,1,0,1,18,1,0,19,26,1,0,27,29,1,0,30,32,120,0,
        36,1,0,0,0,2,45,1,0,0,0,4,47,1,0,0,0,6,53,1,0,0,0,8,55,1,0,0,0,10,
        67,1,0,0,0,12,78,1,0,0,0,14,87,1,0,0,0,16,90,1,0,0,0,18,99,1,0,0,
        0,20,101,1,0,0,0,22,103,1,0,0,0,24,105,1,0,0,0,26,107,1,0,0,0,28,
        109,1,0,0,0,30,111,1,0,0,0,32,35,3,4,2,0,33,35,3,2,1,0,34,32,1,0,
        0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,
        1,0,0,0,38,36,1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,46,3,18,9,0,
        42,46,3,20,10,0,43,46,3,22,11,0,44,46,3,24,12,0,45,41,1,0,0,0,45,
        42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,3,1,0,0,0,47,48,3,6,3,
        0,48,5,1,0,0,0,49,54,3,10,5,0,50,54,3,8,4,0,51,54,3,12,6,0,52,54,
        3,16,8,0,53,49,1,0,0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,
        54,7,1,0,0,0,55,59,3,28,14,0,56,58,3,26,13,0,57,56,1,0,0,0,58,61,
        1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,65,1,0,0,0,61,59,1,0,0,0,
        62,66,3,10,5,0,63,66,3,8,4,0,64,66,3,12,6,0,65,62,1,0,0,0,65,63,
        1,0,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,69,3,28,14,0,
        68,70,3,28,14,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,
        1,0,0,0,72,75,1,0,0,0,73,76,3,12,6,0,74,76,3,14,7,0,75,73,1,0,0,
        0,75,74,1,0,0,0,75,76,1,0,0,0,76,11,1,0,0,0,77,79,3,30,15,0,78,77,
        1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,85,1,0,0,0,
        82,86,3,8,4,0,83,86,3,10,5,0,84,86,3,16,8,0,85,82,1,0,0,0,85,83,
        1,0,0,0,85,84,1,0,0,0,85,86,1,0,0,0,86,13,1,0,0,0,87,88,3,16,8,0,
        88,15,1,0,0,0,89,91,3,26,13,0,90,89,1,0,0,0,91,92,1,0,0,0,92,90,
        1,0,0,0,92,93,1,0,0,0,93,97,1,0,0,0,94,98,3,8,4,0,95,98,3,10,5,0,
        96,98,3,12,6,0,97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,0,0,0,97,98,1,
        0,0,0,98,17,1,0,0,0,99,100,7,0,0,0,100,19,1,0,0,0,101,102,7,1,0,
        0,102,21,1,0,0,0,103,104,7,2,0,0,104,23,1,0,0,0,105,106,7,3,0,0,
        106,25,1,0,0,0,107,108,5,33,0,0,108,27,1,0,0,0,109,110,5,34,0,0,
        110,29,1,0,0,0,111,112,5,35,0,0,112,31,1,0,0,0,12,34,36,45,53,59,
        65,71,75,80,85,92,97
    ]

class uncontracted_brailleParser ( Parser ):

    grammarFileName = "uncontracted_braille.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'.'", "'''", "':'", "'_'", "'\\u2014'", 
                     "'!'", "'-'", "'?'", "';'", "'...'", "'/'", "'\\'", 
                     "'\\u201C'", "'\\u201D'", "'\\u2018'", "'\\u2019'", 
                     "' '", "'('", "')'", "'['", "']'", "'{'", "'}'", "'<'", 
                     "'>'", "'+'", "'='", "'*'", "'\\u20AC'", "'$'", "'\\u00A3'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Lowercase", "Uppercase", "Digit" ]

    RULE_text = 0
    RULE_nonword = 1
    RULE_word = 2
    RULE_sequence = 3
    RULE_capital_first_letter = 4
    RULE_capital_sequence = 5
    RULE_numeral_sequence = 6
    RULE_capital_terminator = 7
    RULE_lowercase_sequence = 8
    RULE_punctuation = 9
    RULE_grouping_punctuation = 10
    RULE_op_and_comp = 11
    RULE_currency_and_measurement = 12
    RULE_lowercase = 13
    RULE_uppercase = 14
    RULE_digit = 15

    ruleNames =  [ "text", "nonword", "word", "sequence", "capital_first_letter", 
                   "capital_sequence", "numeral_sequence", "capital_terminator", 
                   "lowercase_sequence", "punctuation", "grouping_punctuation", 
                   "op_and_comp", "currency_and_measurement", "lowercase", 
                   "uppercase", "digit" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    Lowercase=33
    Uppercase=34
    Digit=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(uncontracted_brailleParser.EOF, 0)

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uncontracted_brailleParser.WordContext)
            else:
                return self.getTypedRuleContext(uncontracted_brailleParser.WordContext,i)


        def nonword(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uncontracted_brailleParser.NonwordContext)
            else:
                return self.getTypedRuleContext(uncontracted_brailleParser.NonwordContext,i)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = uncontracted_brailleParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68719476734) != 0):
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33, 34, 35]:
                    self.state = 32
                    self.word()
                    pass
                elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]:
                    self.state = 33
                    self.nonword()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(uncontracted_brailleParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonwordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def punctuation(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.PunctuationContext,0)


        def grouping_punctuation(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Grouping_punctuationContext,0)


        def op_and_comp(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Op_and_compContext,0)


        def currency_and_measurement(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Currency_and_measurementContext,0)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_nonword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonword" ):
                listener.enterNonword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonword" ):
                listener.exitNonword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonword" ):
                return visitor.visitNonword(self)
            else:
                return visitor.visitChildren(self)




    def nonword(self):

        localctx = uncontracted_brailleParser.NonwordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nonword)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.punctuation()
                pass
            elif token in [19, 20, 21, 22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.grouping_punctuation()
                pass
            elif token in [27, 28, 29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.op_and_comp()
                pass
            elif token in [30, 31, 32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.currency_and_measurement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.SequenceContext,0)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWord" ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWord" ):
                listener.exitWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWord" ):
                return visitor.visitWord(self)
            else:
                return visitor.visitChildren(self)




    def word(self):

        localctx = uncontracted_brailleParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def capital_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_sequenceContext,0)


        def capital_first_letter(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_first_letterContext,0)


        def numeral_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Numeral_sequenceContext,0)


        def lowercase_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Lowercase_sequenceContext,0)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = uncontracted_brailleParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 49
                self.capital_sequence()
                pass

            elif la_ == 2:
                self.state = 50
                self.capital_first_letter()
                pass

            elif la_ == 3:
                self.state = 51
                self.numeral_sequence()
                pass

            elif la_ == 4:
                self.state = 52
                self.lowercase_sequence()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Capital_first_letterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uppercase(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.UppercaseContext,0)


        def lowercase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uncontracted_brailleParser.LowercaseContext)
            else:
                return self.getTypedRuleContext(uncontracted_brailleParser.LowercaseContext,i)


        def capital_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_sequenceContext,0)


        def capital_first_letter(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_first_letterContext,0)


        def numeral_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Numeral_sequenceContext,0)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_capital_first_letter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapital_first_letter" ):
                listener.enterCapital_first_letter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapital_first_letter" ):
                listener.exitCapital_first_letter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapital_first_letter" ):
                return visitor.visitCapital_first_letter(self)
            else:
                return visitor.visitChildren(self)




    def capital_first_letter(self):

        localctx = uncontracted_brailleParser.Capital_first_letterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_capital_first_letter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.uppercase()
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 56
                    self.lowercase() 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 62
                self.capital_sequence()

            elif la_ == 2:
                self.state = 63
                self.capital_first_letter()

            elif la_ == 3:
                self.state = 64
                self.numeral_sequence()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Capital_sequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uppercase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uncontracted_brailleParser.UppercaseContext)
            else:
                return self.getTypedRuleContext(uncontracted_brailleParser.UppercaseContext,i)


        def numeral_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Numeral_sequenceContext,0)


        def capital_terminator(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_terminatorContext,0)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_capital_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapital_sequence" ):
                listener.enterCapital_sequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapital_sequence" ):
                listener.exitCapital_sequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapital_sequence" ):
                return visitor.visitCapital_sequence(self)
            else:
                return visitor.visitChildren(self)




    def capital_sequence(self):

        localctx = uncontracted_brailleParser.Capital_sequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_capital_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.uppercase()
            self.state = 69 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 68
                    self.uppercase()

                else:
                    raise NoViableAltException(self)
                self.state = 71 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 73
                self.numeral_sequence()

            elif la_ == 2:
                self.state = 74
                self.capital_terminator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeral_sequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uncontracted_brailleParser.DigitContext)
            else:
                return self.getTypedRuleContext(uncontracted_brailleParser.DigitContext,i)


        def capital_first_letter(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_first_letterContext,0)


        def capital_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_sequenceContext,0)


        def lowercase_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Lowercase_sequenceContext,0)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_numeral_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeral_sequence" ):
                listener.enterNumeral_sequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeral_sequence" ):
                listener.exitNumeral_sequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeral_sequence" ):
                return visitor.visitNumeral_sequence(self)
            else:
                return visitor.visitChildren(self)




    def numeral_sequence(self):

        localctx = uncontracted_brailleParser.Numeral_sequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numeral_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 77
                    self.digit()

                else:
                    raise NoViableAltException(self)
                self.state = 80 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 82
                self.capital_first_letter()

            elif la_ == 2:
                self.state = 83
                self.capital_sequence()

            elif la_ == 3:
                self.state = 84
                self.lowercase_sequence()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Capital_terminatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lowercase_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Lowercase_sequenceContext,0)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_capital_terminator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapital_terminator" ):
                listener.enterCapital_terminator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapital_terminator" ):
                listener.exitCapital_terminator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapital_terminator" ):
                return visitor.visitCapital_terminator(self)
            else:
                return visitor.visitChildren(self)




    def capital_terminator(self):

        localctx = uncontracted_brailleParser.Capital_terminatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_capital_terminator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.lowercase_sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lowercase_sequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lowercase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uncontracted_brailleParser.LowercaseContext)
            else:
                return self.getTypedRuleContext(uncontracted_brailleParser.LowercaseContext,i)


        def capital_first_letter(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_first_letterContext,0)


        def capital_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Capital_sequenceContext,0)


        def numeral_sequence(self):
            return self.getTypedRuleContext(uncontracted_brailleParser.Numeral_sequenceContext,0)


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_lowercase_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowercase_sequence" ):
                listener.enterLowercase_sequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowercase_sequence" ):
                listener.exitLowercase_sequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLowercase_sequence" ):
                return visitor.visitLowercase_sequence(self)
            else:
                return visitor.visitChildren(self)




    def lowercase_sequence(self):

        localctx = uncontracted_brailleParser.Lowercase_sequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lowercase_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 89
                    self.lowercase()

                else:
                    raise NoViableAltException(self)
                self.state = 92 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 94
                self.capital_first_letter()

            elif la_ == 2:
                self.state = 95
                self.capital_sequence()

            elif la_ == 3:
                self.state = 96
                self.numeral_sequence()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PunctuationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_punctuation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPunctuation" ):
                listener.enterPunctuation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPunctuation" ):
                listener.exitPunctuation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPunctuation" ):
                return visitor.visitPunctuation(self)
            else:
                return visitor.visitChildren(self)




    def punctuation(self):

        localctx = uncontracted_brailleParser.PunctuationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_punctuation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 524286) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grouping_punctuationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_grouping_punctuation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouping_punctuation" ):
                listener.enterGrouping_punctuation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouping_punctuation" ):
                listener.exitGrouping_punctuation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouping_punctuation" ):
                return visitor.visitGrouping_punctuation(self)
            else:
                return visitor.visitChildren(self)




    def grouping_punctuation(self):

        localctx = uncontracted_brailleParser.Grouping_punctuationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_grouping_punctuation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133693440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_and_compContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_op_and_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_and_comp" ):
                listener.enterOp_and_comp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_and_comp" ):
                listener.exitOp_and_comp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_and_comp" ):
                return visitor.visitOp_and_comp(self)
            else:
                return visitor.visitChildren(self)




    def op_and_comp(self):

        localctx = uncontracted_brailleParser.Op_and_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_op_and_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Currency_and_measurementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_currency_and_measurement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCurrency_and_measurement" ):
                listener.enterCurrency_and_measurement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCurrency_and_measurement" ):
                listener.exitCurrency_and_measurement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCurrency_and_measurement" ):
                return visitor.visitCurrency_and_measurement(self)
            else:
                return visitor.visitChildren(self)




    def currency_and_measurement(self):

        localctx = uncontracted_brailleParser.Currency_and_measurementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_currency_and_measurement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LowercaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lowercase(self):
            return self.getToken(uncontracted_brailleParser.Lowercase, 0)

        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_lowercase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowercase" ):
                listener.enterLowercase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowercase" ):
                listener.exitLowercase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLowercase" ):
                return visitor.visitLowercase(self)
            else:
                return visitor.visitChildren(self)




    def lowercase(self):

        localctx = uncontracted_brailleParser.LowercaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lowercase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(uncontracted_brailleParser.Lowercase)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UppercaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Uppercase(self):
            return self.getToken(uncontracted_brailleParser.Uppercase, 0)

        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_uppercase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUppercase" ):
                listener.enterUppercase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUppercase" ):
                listener.exitUppercase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUppercase" ):
                return visitor.visitUppercase(self)
            else:
                return visitor.visitChildren(self)




    def uppercase(self):

        localctx = uncontracted_brailleParser.UppercaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_uppercase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(uncontracted_brailleParser.Uppercase)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digit(self):
            return self.getToken(uncontracted_brailleParser.Digit, 0)

        def getRuleIndex(self):
            return uncontracted_brailleParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigit" ):
                return visitor.visitDigit(self)
            else:
                return visitor.visitChildren(self)




    def digit(self):

        localctx = uncontracted_brailleParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(uncontracted_brailleParser.Digit)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





