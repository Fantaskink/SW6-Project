grammar braille;

    text
        :   (word | nonword)* EOF
        ;

    nonword
        :   punctuation | grouping_punctuation | op_and_comp
        ;

    word
        :   sequence
        ;

    strong_contraction
        :   ('and' | 'for' | 'of' | 'the' | 'with') sequence?
        ;

    strong_groupsign
        :   ('ch' | 'gh' | 'sh' | 'th' | 'wh' | 'ed' | 'er' | 'ou' | 'ow' | 'st' | 'ing' | 'ar') sequence?
        ;

    sequence
        :   (strong_contraction | strong_groupsign
        | capital_sequence | capital_first_letter | numeral_sequence | lowercase_sequence)
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
             '?' | ';' | '...' | '/' | '\\' | '“' | '”' | '‘' | '’' | ' '
        ;

    grouping_punctuation
        :   '(' | ')' | '[' | ']' | '{' | '}' | '<' | '>'
        ;

    op_and_comp
        :   '+' | '='
        ;

    currency_and_measurement
        :   '€' | '$' | '£'
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