parser grammar contracted_braille_parser;

options {
    tokenVocab = contracted_braille_lexer;
}

    text
        :   (space* word (space+ word?)*)? EOF
        ;

    word
        :    standing_alone | sequence
        ;

    standing_alone
        :   standing_alone_connector* standing_alone_part (standing_alone_connector standing_alone_part?)*
        ;

    standing_alone_part
        :   single_letter | lowercase_sequence | standing_alone_letter  | capitals_sequence |
            alphabetic_wordsign | lower_wordsign | strong_wordsign |
            numeral_sequence
        ;

    single_letter
        :   Uppercase | Lowercase
        ;

    single_capital_letter
        :   Uppercase
        ;


    lower_wordsign
        :   LOWER_WORDSIGN_L | LOWER_WORDSIGN_F | LOWER_WORDSIGN_C
        ;

    standing_alone_connector
        :   HYPHEN | DASH | LONG_DASH
        ;

    standing_alone_letter
        :   capital_letter | lowercase
        ;

    alphabetic_wordsign
        :   (ALPHABETIC_WORDSIGN_L | ALPHABETIC_WORDSIGN_F | ALPHABETIC_WORDSIGN_C)
        ;

    strong_wordsign
        :   STRONG_WORDSIGN_L | STRONG_WORDSIGN_F | STRONG_WORDSIGN_C
        ;

    //shortform
    //    :   SHORTFORM_L | SHORTFORM_F | SHORTFORM_C
    //    ;

    sequence
        :   (capitals_sequence | numeral_sequence | lowercase_sequence | symbol_sequence)
        ;

    capital_letter
        :   uppercase (lowercase_sequence | numeral_sequence |symbol_sequence)?
        ;

    capitals_sequence
        :   ((uppercase uppercase+) | (uppercase* (strong_contraction_c | strong_groupsign_c)+ uppercase*)) capitals_terminator?
        ;

    capitals_terminator
        :   lowercase_sequence
        ;

    numeral_sequence
        :   digit+ (numeral_separator digit+)* grade_1_terminator?
        ;

    numeral_separator
        :   COMMA | DOT
        ;

    grade_1_terminator
        :   lowercase_sequence
        ;

    lowercase_sequence
        :   (strong_contraction_l | lowercase | strong_groupsign_l)+
        ;

    strong_contraction_l
        :   STRONG_CONTRACTION_L
        ;

    strong_contraction_f
        :   STRONG_CONTRACTION_F
        ;

    strong_contraction_c
        :   STRONG_CONTRACTION_C
        ;

    strong_groupsign_l
        :   STRONG_GROUPSIGN_L
        ;

    strong_groupsign_f
        :   STRONG_GROUPSIGN_F
        ;

    strong_groupsign_c
        :   STRONG_GROUPSIGN_C
        ;


    symbol_sequence
        :   (punctuation | grouping_punctuation | op_and_comp | currency_and_measurement)+
        ;

    punctuation
        :   DOT | COMMA | APOSTROPHE | COLON | UNDERSCORE | DASH | EXCLAMATION | HYPHEN |
            QUESTION | SEMICOLON | SLASH | BACKSLASH | QUOTATION_OPEN | QUOTATION_CLOSE |
            SINGLE_QUOTE_OPEN | SINGLE_QUOTE_CLOSE | DOUBLE_QUOTE | LONG_DASH
        ;

    space
        :   Space
        ;

    grouping_punctuation
        :   LPAREN | RPAREN | LBRACK | RBRACK | LCURLY | RCURLY | LANGLE | RANGLE
        ;

    op_and_comp
        :   PLUS | EQUALS | STAR | CARET
        ;

    currency_and_measurement
        :   EURO | DOLLAR | POUND
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








