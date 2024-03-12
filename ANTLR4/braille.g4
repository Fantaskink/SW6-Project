grammar braille;

    text
        :   word (' '+ word)* EOF
        ;

    word
        :   sequence
        ;

    sequence
        :   (capital_sequence | capital_first_letter | numeral_sequence | lowercase_sequence)
        ;


    capital_first_letter
        :   Uppercase Lowercase* (capital_sequence | capital_first_letter | numeral_sequence)?
        ;

    capital_sequence
        :   Uppercase Uppercase+ (numeral_sequence | capital_terminator )?
        ;

    numeral_sequence
        :   Digit+ (capital_first_letter | capital_sequence | lowercase_sequence)?
        ;

    capital_terminator
        :   lowercase_sequence
        ;

    lowercase_sequence
        :   Lowercase+ (capital_first_letter | capital_sequence | numeral_sequence)?
        ;

    punctuation
        :    ',' | '.' | '\'' | ':' | '_' | '—' | '!' | '-' |
             '?' | ';' | '...' | '/' | '\\' | '“' | '”' | '‘' | '’'
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