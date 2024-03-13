grammar uncontracted_braille;

    text
        :   (word | nonword)* EOF
        ;

    nonword
        :   punctuation | grouping_punctuation | op_and_comp | currency_and_measurement
        ;

    word
        :   sequence
        ;

    sequence
        :   (capital_sequence | capital_first_letter | numeral_sequence | lowercase_sequence)
        ;


    capital_first_letter
        :   uppercase lowercase* (capital_sequence | capital_first_letter | numeral_sequence)?
        ;

    capital_sequence
        :   uppercase uppercase+ (numeral_sequence | capital_terminator )?
        ;

    numeral_sequence
        :   digit+ (capital_first_letter | capital_sequence | lowercase_sequence)?
        ;

    capital_terminator
        :   lowercase_sequence
        ;

    lowercase_sequence
        :   lowercase+ (capital_first_letter | capital_sequence | numeral_sequence)?
        ;

    punctuation
        :    ',' | '.' | '\'' | ':' | '_' | '—' | '!' | '-' |
             '?' | ';' | '...' | '/' | '\\' | '“' | '”' | '‘' | '’' | ' '
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