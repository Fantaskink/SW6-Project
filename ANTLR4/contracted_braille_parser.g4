parser grammar contracted_braille_parser;

options {
    tokenVocab = contracted_braille_lexer;
}

    text
        :   (space* word (space+ word?)*)? EOF
        ;

    word
        :    (sequence | single)+ | alphabetic_wordsign
        ;

    alphabetic_wordsign
        :   ALPHABETIC_WORDSIGN
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
        :   SC_L_AND | SC_L_FOR | SC_L_OF | SC_L_THE | SC_L_WITH
        ;

    strong_contraction_f
        :   SC_F_AND | SC_F_FOR | SC_F_OF | SC_F_THE | SC_F_WITH
        ;

    strong_contraction_c
        :   SC_C_AND | SC_C_FOR | SC_C_OF | SC_C_THE | SC_C_WITH
        ;

    symbol_sequence
        :   (punctuation | grouping_punctuation | op_and_comp | currency_and_measurement)+
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








