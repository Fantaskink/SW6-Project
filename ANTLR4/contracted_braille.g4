grammar contracted_braille;

    text
        :   (word (space word)*)?  EOF
        ;

    word
        :   (standing_alone | (sequence | single)+)
        ;

    standing_alone
        :   standing_alone_letters_sequence | standing_alone_single
        ;

    standing_alone_letters_sequence
        :   standing_alone_connector? single (standing_alone_connector single)+
        ;

    standing_alone_single
        :   single | alphabetic_wordsign
        ;

    standing_alone_connector
        :   '-' | '–' | '—'
        ;

    alphabetic_wordsign
        :   'but' | 'can' | 'do' | 'every' | 'from' | 'go' |
            'have' | 'just' | 'knowledge' | 'like' | 'more' |
            'not' | 'people' | 'quite' | 'rather' | 'so' |
            'that' | 'us' | 'very' | 'will' | 'it' | 'you' | 'as'
        ;

    sequence
        :   (capital_sequence | numeral_sequence | lowercase_sequence | symbol_sequence)
        ;

    single
        :   capital_letter | lowercase_letter
        ;

    capital_letter
        :   uppercase
        ;

    lowercase_letter
        :   lowercase
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