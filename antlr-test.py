from gen.contracted_braille_lexer import contracted_braille_lexer
from gen.contracted_braille_parser import contracted_braille_parser
from antlr4 import *


class MyLexer(contracted_braille_lexer):
    def emit(self):
        t = self._factory.create(self._tokenFactorySourcePair, self._type, self._text, self._channel,
                                 self._tokenStartCharIndex,
                                 self.getCharIndex() - 1, self._tokenStartLine, self._tokenStartColumn)

        if t.type == self.ALPHABETIC_WORDSIGN:
            word = t.text
            length = len(t.text)
            next_token = self._input.LA(1)
            prev_token = self._input.LA(-(1+length))
            space = 32
            eof = -1
            valid_separators = [eof, space]
            print(f"Next token: {next_token}")
            print(f"Prev token: {prev_token}")

            if next_token not in valid_separators or prev_token not in valid_separators:
                t = self._factory.create(self._tokenFactorySourcePair, 48, word[0], self._channel,
                                         self._tokenStartCharIndex,
                                         self._tokenStartCharIndex, self._tokenStartLine, self._tokenStartColumn)
                print("start index:", self._tokenStartCharIndex)
                self._input.seek(self._tokenStartCharIndex + 1)

        self.emitToken(t)
        print(t)
        return t


string = " but"

input_stream = InputStream(string)
lexer = MyLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# print tokens
token_stream.fill()
print(" ")
for token in token_stream.tokens:
    token: Token
    print(token.type, token.text)
