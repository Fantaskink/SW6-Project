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
        :   lowercase | uppercase
        ;

    capital_sequence
        :   uppercase uppercase+
        ;

    numeral_sequence
        :   digit digit+
        ;

    lowercase_sequence
        :   lowercase lowercase+
        ;

    symbol_sequence
        :   punctuation | grouping_punctuation | op_and_comp | currency_and_measurement
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
        :   '+' | '=' | '*'
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