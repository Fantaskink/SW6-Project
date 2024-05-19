grammar uncontracted_braille;

    text
        :   (word | space)* EOF
        ;

    word
        :   (sequence | single)+
        ;

    sequence
        :   (capital_sequence | numeral_sequence | lowercase_sequence | symbol_sequence)
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
        :   lowercase_sequence
        ;

    numeral_sequence
        :   digit+ grade_1_mode?
        ;

    grade_1_mode
        :   lowercase_sequence
        ;

    lowercase_sequence
        :   lowercase+
        ;

    symbol_sequence
        :   (punctuation | grouping_punctuation | op_and_comp | currency_and_measurement)+
        ;

    punctuation
        :    ',' | '.' | '\'' | ':' | '_' | '—' | '!' | '-' |
             '?' | ';' | '...' | '/' | '\\' | '“' | '”' | '‘' | '’'
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