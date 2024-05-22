lexer grammar contracted_braille_lexer;

ALPHABETIC_WORDSIGN
    :
        'but' | 'can' | 'do' | 'every' | 'from' | 'go' |
         'have' | 'just' | 'knowledge' | 'like' | 'more' |
         'not' | 'people' | 'quite' | 'rather' | 'so' |
         'that' | 'us' | 'very' | 'will' | 'it' | 'you' | 'as'
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

SC_L_AND : 'and';
SC_L_FOR : 'for';
SC_L_OF : 'of';
SC_L_THE : 'the';
SC_L_WITH : 'with';

SC_F_AND : 'And';
SC_F_FOR : 'For';
SC_F_OF : 'Of';
SC_F_THE : 'The';
SC_F_WITH : 'With';

SC_C_AND : 'AND';
SC_C_FOR : 'FOR';
SC_C_OF : 'OF';
SC_C_THE : 'THE';
SC_C_WITH : 'WITH';


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





