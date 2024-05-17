grammar contracted_braille;

    text
        :   (space* word (space+ word?)*)? EOF
        ;

    word
        :   (standing_alone | sequence | single)+
        ;

    standing_alone
        :   standing_alone_letters_sequence | standing_alone_single
        ;

    standing_alone_letters_sequence
        :   standing_alone_connector? (StrongContraction+ | lowercase_sequence | capital_sequence)+ (standing_alone_connector standing_alone+)*
        ;

    standing_alone_single
        :   single | AlphabeticWordsign | StrongContraction
        ;

    standing_alone_connector
        :   '-' | '–' | '—'
        ;

    sequence
        : StrongContraction
        | capital_sequence
        | numeral_sequence
        | lowercase_sequence
        | symbol_sequence
        ;

    single
        :   CapitalLetter | LowercaseLetter
        ;

    StrongContraction
        :   'and' | 'for' | 'of' | 'the' | 'with'
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



    StrongGroupsign
        :   'ch' | 'gh' | 'sh' | 'th' | 'wh' | 'ed' | 'er' | 'ou' |
            'ow' | 'st' | 'ing' | 'ar'
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
        :  LowercaseLetter+
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