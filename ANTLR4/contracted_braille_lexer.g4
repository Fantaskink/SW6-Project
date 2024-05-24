lexer grammar contracted_braille_lexer;

@members {
def not_alnum(self, direction):
    target_char = chr(self._input.LA(direction)) if self._input.LA(direction) >= 0 else ''
    return not target_char.isalnum()

def is_space_or_eof(self, direction):
    target_char = chr(self._input.LA(direction)) if self._input.LA(direction) >= 0 else ''
    return target_char.isspace() or target_char == ''
}

ALPHABETIC_WORDSIGN_L
    :   {self.not_alnum(-1)}?
        ('but' | 'can' | 'do' | 'every' | 'from' | 'go' |
         'have' | 'just' | 'knowledge' | 'like' | 'more' |
         'not' | 'people' | 'quite' | 'rather' | 'so' |
         'that' | 'us' | 'very' | 'will' | 'it' | 'you' | 'as')
        {self.not_alnum(1)}?
    ;

ALPHABETIC_WORDSIGN_C
    :   {self.not_alnum(-1)}?
        ('BUT' | 'CAN' | 'DO' | 'EVERY' | 'FROM' | 'GO' |
         'HAVE' | 'JUST' | 'KNOWLEDGE' | 'LIKE' | 'MORE' |
         'NOT' | 'PEOPLE' | 'QUITE' | 'RATHER' | 'SO' |
         'THAT' | 'US' | 'VERY' | 'WILL' | 'IT' | 'YOU' | 'AS')
        {self.not_alnum(1)}?
    ;

ALPHABETIC_WORDSIGN_F
    :   {self.not_alnum(-1)}?
        ('But' | 'Can' | 'Do' | 'Every' | 'From' | 'Go' |
         'Have' | 'Just' | 'Knowledge' | 'Like' | 'More' |
         'Not' | 'People' | 'Quite' | 'Rather' | 'So' |
         'That' | 'Us' | 'Very' | 'Will' | 'It' | 'You' | 'As')
        {self.not_alnum(1)}?
    ;

STRONG_WORDSIGN_L
    :   {self.not_alnum(-1)}?
        ('child' | 'shall' | 'this' | 'which' | 'out' | 'still')
        {self.not_alnum(1)}?
    ;

STRONG_WORDSIGN_C
    :   {self.not_alnum(-1)}?
        ('CHILD' | 'SHALL' | 'THIS' | 'WHICH' | 'OUT' | 'STILL')
        {self.not_alnum(1)}?
    ;

STRONG_WORDSIGN_F
    :   {self.not_alnum(-1)}?
        ('Child' | 'Shall' | 'This' | 'Which' | 'Out' | 'Still')
        {self.not_alnum(1)}?
    ;

LOWER_WORDSIGN_L
    :   {self.is_space_or_eof(-1)}?
        ('be' |  'were' | 'his' | 'was')
        {self.is_space_or_eof(1)}?
        |
        {self.not_alnum(-1)}?
        ('in' | 'enough')
        {self.not_alnum(1)}?
    ;

LOWER_WORDSIGN_C
    :   {self.is_space_or_eof(-1)}?
        ('BE' |  'WERE' | 'HIS' | 'WAS')
        {self.is_space_or_eof(1)}?
        |
        {self.not_alnum(-1)}?
        ('IN' | 'ENOUGH')
        {self.not_alnum(1)}?
    ;

LOWER_WORDSIGN_F
    :   {self.is_space_or_eof(-1)}?
        ('Be' |  'Were' | 'His' | 'Was')
        {self.is_space_or_eof(1)}?
        |
        {self.not_alnum(-1)}?
        ('In' | 'Enough')
        {self.not_alnum(1)}?
    ;

STRONG_CONTRACTION_L
    :
        'and' | 'for' | 'of' | 'the' | 'with'
    ;

STRONG_CONTRACTION_C
    :
        'AND' | 'FOR' | 'OF' | 'THE' | 'WITH'
    ;

STRONG_CONTRACTION_F
    :
        'And' | 'For' | 'Of' | 'The' | 'With'
    ;

DOT : '.';
COMMA : ',';
APOSTROPHE : '\'';
COLON : ':';
UNDERSCORE : '_';
DASH : '—';
EXCLAMATION : '!';
HYPHEN : '-';
QUESTION : '?';
SEMICOLON : ';';
SLASH : '/';
BACKSLASH : '\\';
QUOTATION_OPEN : '“';
QUOTATION_CLOSE : '”';
SINGLE_QUOTE_OPEN : '‘';
SINGLE_QUOTE_CLOSE : '’';

LPAREN : '(';
RPAREN : ')';
LBRACK : '[';
RBRACK : ']';
LCURLY : '{';
RCURLY : '}';
LANGLE : '<';
RANGLE : '>';

PLUS : '+';
EQUALS : '=';
STAR : '*';
CARET : '^';

EURO : '€';
DOLLAR : '$';
POUND : '£';


    Lowercase
            :   [a-z]
            ;

    Uppercase
        :   [A-Z]
        ;

    Digit
        :   [0-9]
        ;

    Space
        :   ' '
        ;

    Newline
        :   (   '\r' '\n'?
            |   '\n'
            )
            -> skip
        ;





