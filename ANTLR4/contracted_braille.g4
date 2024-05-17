grammar contracted_braille;

    text
        :   space* (word (space word?)*)?  EOF
        ;

    word
        :   standing_alone | sequence | single+
        ;

    standing_alone
        :   standing_alone_letters_sequence | standing_alone_single
        ;

    standing_alone_letters_sequence
        :   standing_alone_connector? Lowercase_sequence | (standing_alone_connector Lowercase_sequence)*
        ;

    standing_alone_single
        :   single | Alphabetic_wordsign
        ;

    standing_alone_connector
        :   '-' | '–' | '—'
        ;

    sequence
        : Capital_sequence
        | numeral_sequence
        | Lowercase_sequence
        | symbol_sequence
        ;

    single
        :   Capital_letter | Lowercase_letter
        ;

    Capital_letter
        :   Uppercase
        ;

    Lowercase_letter
        :   Lowercase
        ;

    Capital_sequence
        :   Uppercase Uppercase+ Capitals_terminator?
        ;

    Alphabetic_wordsign
        :   'but' | 'can' | 'do' | 'every' | 'from' | 'go' |
            'have' | 'just' | 'knowledge' | 'like' | 'more' |
            'not' | 'people' | 'quite' | 'rather' | 'so' |
            'that' | 'us' | 'very' | 'will' | 'it' | 'you' | 'as'
        ;

    StrongWordsigns
        :   'child' | 'shall' | 'this' | 'which' | 'out' | 'still'
        ;

    fragment Capitals_terminator
        :   Lowercase_sequence
        ;

    numeral_sequence
        :   digit+ grade_1_mode?
        ;

    grade_1_mode
        :   Lowercase_sequence
        ;

    Lowercase_sequence
        :  Lowercase+
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

    digit
        :   Digit
        ;

    fragment Lowercase
        :   [a-z]
        ;

    fragment Uppercase
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