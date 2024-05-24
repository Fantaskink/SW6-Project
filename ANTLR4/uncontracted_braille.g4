grammar uncontracted_braille;

    text
        :   (space* word (space+ word?)*)* EOF
        ;

    word
        :   (sequence | single)+
        ;

    sequence
        :   (capital_sequence | numeral_sequence | lowercase_sequence | symbols_sequence)
        ;

    single
        :   capital_letter
        ;

    capital_letter
        :   uppercase
        ;

    capital_sequence
        :   uppercase uppercase+ capitals_terminator?
        ;

    capitals_terminator
        :   lowercase_sequence | symbols_sequence
        ;

    numeral_sequence
        :   digit+ (numeral_separator digit+)* grade_1_terminator?
        ;

    numeral_separator
        :   ',' | '.'
        ;

    grade_1_terminator
        :   lowercase_sequence
        ;

    lowercase_sequence
        :   lowercase+
        ;

    symbols_sequence
        :   (punctuation | grouping_punctuation | op_and_comp | currency_and_measurement | special)+
        ;

    punctuation
        :    ',' | '.' | '\'' | ':' | '_' | '—' | '!' | '-' |
             '?' | ';' | '...' | '/' | '\\' | '“' | '”' | '‘' | '’' |
             '"'
        ;

    space
        :   ' '
        ;

    grouping_punctuation
        :   '(' | ')' | '[' | ']' | '{' | '}' | '<' | '>'
        ;

    op_and_comp
        :   '+' | '=' | '*' | '^'
        ;

    currency_and_measurement
        :   '€' | '$' | '£'
        ;

    special
        :   '@'
        ;

    lowercase
        :   Lowercase
        ;

    uppercase
        :   Uppercase
        ;

    digit
        :   Digit
        ;

    Lowercase
        :   [a-z]
        ;

    Uppercase
        :   [A-Z]
        ;

    Digit
        :   [0-9]
        ;

    Newline
        :   (   '\r' '\n'?
            |   '\n'
            )
            -> skip
        ;