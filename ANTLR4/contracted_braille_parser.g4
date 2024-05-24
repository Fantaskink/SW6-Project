parser grammar contracted_braille_parser;

options {
    tokenVocab = contracted_braille_lexer;
}

    text
        :   (space* word (space+ word?)*)? EOF
        ;

    word
        :    standing_alone | (sequence | single)+
        ;

    standing_alone
        :   standing_alone_single | standing_alone_sequence
        ;

    standing_alone_single
        :   standing_alone_letter | standing_alone_wordsign | lower_wordsign
        ;

    standing_alone_wordsign
        :   symbol_sequence? (wordsign | lower_wordsign) symbol_sequence?
        ;

    lower_wordsign
        :   LOWER_WORDSIGN_L | LOWER_WORDSIGN_F | LOWER_WORDSIGN_C
        ;

    standing_alone_connector
        :   HYPHEN | DASH
        ;

    standing_alone_letter
        :   capital_letter | lowercase
        ;

    standing_alone_sequence
        :   standing_alone_connector? (wordsign | lowercase_sequence | numeral_sequence) ((standing_alone_connector sequence)* | standing_alone_connector)
        ;

    wordsign
        :   alphabetic_wordsign | strong_wordsign
        ;

    alphabetic_wordsign
        :   ALPHABETIC_WORDSIGN_L | ALPHABETIC_WORDSIGN_F | ALPHABETIC_WORDSIGN_C
        ;

    strong_wordsign
        :   STRONG_WORDSIGN_L | STRONG_WORDSIGN_F | STRONG_WORDSIGN_C
        ;

    sequence
        :   (capital_sequence | numeral_sequence | lowercase_sequence | symbol_sequence)
        ;

    single
        :   capital_letter | strong_contraction_f
        ;

    capital_letter
        :   uppercase
        ;

    capital_sequence
        :   (uppercase uppercase+) | (uppercase* strong_contraction_c+ uppercase*) capitals_terminator?
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
        :   strong_contraction_l+ | lowercase+
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

    symbol_sequence
        :   (punctuation | grouping_punctuation | op_and_comp | currency_and_measurement)+ (lowercase_sequence | capital_sequence | single)?
        ;

    punctuation
        :   DOT | COMMA | APOSTROPHE | COLON | UNDERSCORE | DASH | EXCLAMATION | HYPHEN |
            QUESTION | SEMICOLON | SLASH | BACKSLASH | QUOTATION_OPEN | QUOTATION_CLOSE |
            SINGLE_QUOTE_OPEN | SINGLE_QUOTE_CLOSE
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








