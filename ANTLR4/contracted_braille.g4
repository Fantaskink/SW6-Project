grammar contracted_braille;

    text
        :   (space* word (space+ word?)*)? EOF
        ;

    word
        :   standing_alone | sequence+ | single+
        ;

    standing_alone
        :   standing_alone_letters_sequence | standing_alone_single
        ;

    standing_alone_letters_sequence
        :   standing_alone_connector? standing_alone_sequence_part+ (standing_alone_connector standing_alone_sequence_part+)* symbol_sequence?
        ;

    standing_alone_sequence_part
        :   lowercase_sequence
        |   capital_sequence
        ;

    standing_alone_single
        :   single | wordsign | StrongContractionL
        ;

    standing_alone_connector
        :   '-' | '–' | '—'
        ;

    sequence
        : capital_sequence
        | numeral_sequence
        | lowercase_sequence
        | symbol_sequence
        ;

    single
        :   StrongContractionF | CapitalLetter
        ;

    StrongContractionL
        :   'and' | 'for' | 'of' | 'the' | 'with'
        ;

    StrongContractionC
        :   'AND' | 'FOR' | 'OF' | 'THE' | 'WITH'
        ;

    StrongContractionF
        :   'And' | 'For' | 'Of' | 'The' | 'With'
        ;

    CapitalLetter
        :   Uppercase
        ;

    LowercaseLetter
        :   Lowercase
        ;

    capital_sequence
        :   (StrongContractionC | CapitalLetter) (StrongContractionC | CapitalLetter)+ capitals_terminator?
        ;



    //StrongWordsigns
        //:   'child' | 'shall' | 'this' | 'which' | 'out' | 'still'
        //;

    //StrongGroupsign
        //:   'ch' | 'gh' | 'sh' | 'th' | 'wh' | 'ed' | 'er' | 'ou' |
        //    'ow' | 'st' | 'ing' | 'ar'
        //;

    capitals_terminator
        :   lowercase_sequence
        ;

    numeral_sequence
        :   digit+ ('.' digit+)* grade_1_mode?
        ;

    grade_1_mode
        :   lowercase_sequence
        ;

    lowercase_sequence
        :  (LowercaseLetter | StrongContractionL)+
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

    wordsign
        :   AlphabeticWordsign
        ;


    AlphabeticWordsign
        :   'but' | 'can' | 'do' | 'every' | 'from' | 'go' |
            'have' | 'just' | 'knowledge' | 'like' | 'more' |
            'not' | 'people' | 'quite' | 'rather' | 'so' |
            'that' | 'us' | 'very' | 'will' | 'it' | 'you' | 'as'
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