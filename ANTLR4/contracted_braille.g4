grammar contracted_braille;

    text
        :   space* (word (space+ word?)*)?  EOF
        ;

    word
        :   standing_alone | sequence | single
        ;

    standing_alone
        :   standing_alone_letters_sequence | standing_alone_single
        ;

    standing_alone_letters_sequence
        :   standing_alone_connector? (LowercaseSequence | capital_sequence) (standing_alone_connector standing_alone+)*
        ;

    standing_alone_single
        :   single | AlphabeticWordsign
        ;

    standing_alone_connector
        :   '-' | '–' | '—'
        ;

    sequence
        : capital_sequence
        | numeral_sequence
        | LowercaseSequence
        | symbol_sequence
        ;

    single
        :   CapitalLetter | LowercaseLetter
        ;

    CapitalLetter
        :   Uppercase
        ;

    LowercaseLetter
        :   Lowercase
        ;

    capital_sequence
        :   CapitalLetter CapitalLetter+ capitals_terminator?
        ;

    AlphabeticWordsign
        :   'but' | 'can' | 'do' | 'every' | 'from' | 'go' |
            'have' | 'just' | 'knowledge' | 'like' | 'more' |
            'not' | 'people' | 'quite' | 'rather' | 'so' |
            'that' | 'us' | 'very' | 'will' | 'it' | 'you' | 'as'
        ;

    StrongWordsigns
        :   'child' | 'shall' | 'this' | 'which' | 'out' | 'still'
        ;

    capitals_terminator
        :   LowercaseSequence
        ;

    numeral_sequence
        :   digit+ grade_1_mode?
        ;

    grade_1_mode
        :   LowercaseSequence
        ;

    LowercaseSequence
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