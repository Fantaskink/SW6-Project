lexer grammar contracted_braille_lexer;

@members {
def not_alnum(self, direction):
    target_char = chr(self._input.LA(direction)) if self._input.LA(direction) >= 0 else ''
    return not target_char.isalnum()

def is_space_or_eof(self, direction):
    target_char = chr(self._input.LA(direction)) if self._input.LA(direction) >= 0 else ''
    return target_char.isspace() or target_char == ''
}

ALPHABETIC_WORDSIGN_L
    :   {self.not_alnum(-1)}?
        ('but' | 'can' | 'do' | 'every' | 'from' | 'go' |
         'have' | 'just' | 'knowledge' | 'like' | 'more' |
         'not' | 'people' | 'quite' | 'rather' | 'so' |
         'that' | 'us' | 'very' | 'will' | 'it' | 'you' | 'as')
        {self.not_alnum(1)}?
    ;

ALPHABETIC_WORDSIGN_C
    :   {self.not_alnum(-1)}?
        ('BUT' | 'CAN' | 'DO' | 'EVERY' | 'FROM' | 'GO' |
         'HAVE' | 'JUST' | 'KNOWLEDGE' | 'LIKE' | 'MORE' |
         'NOT' | 'PEOPLE' | 'QUITE' | 'RATHER' | 'SO' |
         'THAT' | 'US' | 'VERY' | 'WILL' | 'IT' | 'YOU' | 'AS')
        {self.not_alnum(1)}?
    ;

ALPHABETIC_WORDSIGN_F
    :   {self.not_alnum(-1)}?
        ('But' | 'Can' | 'Do' | 'Every' | 'From' | 'Go' |
         'Have' | 'Just' | 'Knowledge' | 'Like' | 'More' |
         'Not' | 'People' | 'Quite' | 'Rather' | 'So' |
         'That' | 'Us' | 'Very' | 'Will' | 'It' | 'You' | 'As')
        {self.not_alnum(1)}?
    ;

STRONG_WORDSIGN_L
    :   {self.not_alnum(-1)}?
        ('child' | 'shall' | 'this' | 'which' | 'out' | 'still')
        {self.not_alnum(1)}?
    ;

STRONG_WORDSIGN_C
    :   {self.not_alnum(-1)}?
        ('CHILD' | 'SHALL' | 'THIS' | 'WHICH' | 'OUT' | 'STILL')
        {self.not_alnum(1)}?
    ;

STRONG_WORDSIGN_F
    :   {self.not_alnum(-1)}?
        ('Child' | 'Shall' | 'This' | 'Which' | 'Out' | 'Still')
        {self.not_alnum(1)}?
    ;

LOWER_WORDSIGN_L
    :   {self.is_space_or_eof(-1)}?
        ('be' |  'were' | 'his' | 'was')
        {self.is_space_or_eof(1)}?
        |
        {self.not_alnum(-1)}?
        ('in' | 'enough')
        {self.not_alnum(1)}?
    ;

LOWER_WORDSIGN_C
    :   {self.is_space_or_eof(-1)}?
        ('BE' |  'WERE' | 'HIS' | 'WAS')
        {self.is_space_or_eof(1)}?
        |
        {self.not_alnum(-1)}?
        ('IN' | 'ENOUGH')
        {self.not_alnum(1)}?
    ;

LOWER_WORDSIGN_F
    :   {self.is_space_or_eof(-1)}?
        ('Be' |  'Were' | 'His' | 'Was')
        {self.is_space_or_eof(1)}?
        |
        {self.not_alnum(-1)}?
        ('In' | 'Enough')
        {self.not_alnum(1)}?
    ;

STRONG_CONTRACTION_L
    :
        'and' | 'for' | 'of' | 'the' | 'with'
    ;

STRONG_CONTRACTION_C
    :
        'AND' | 'FOR' | 'OF' | 'THE' | 'WITH'
    ;

STRONG_CONTRACTION_F
    :
        'And' | 'For' | 'Of' | 'The' | 'With'
    ;

SHORTFORM_L
    :   {self.not_alnum(-1)}?
        ('about' | 'above' | 'according' | 'across' | 'after' | 'afternoon' | 'afterward' | 'again' | 'against' | 'also' | 'almost' | 'already' | 'altogether' | 'although' | 'always' | 'blind' | 'braille' | 'could' | 'declare' | 'declaring' | 'deceive' | 'deceiving' | 'either' | 'friend' | 'first' | 'good' | 'great' | 'him' | 'himself' | 'herself' | 'immediate' | 'little' | 'letter' | 'myself' | 'much' | 'must' | 'necessary' | 'neither' | 'paid' | 'perceive' | 'perceiving' | 'perhaps' | 'quick' | 'receive' | 'receiving' | 'rejoice' | 'rejoicing' | 'said' | 'such' | 'today' | 'together' | 'tomorrow' | 'tonight' | 'itself' | 'its' | 'your' | 'yourself' | 'yourselves' | 'themselves' | 'children' | 'should' | 'thyself' | 'ourselves' | 'would' | 'because' | 'before' | 'behind' | 'below' | 'beneath' | 'beside' | 'between' | 'beyond' | 'conceive' | 'conceiving' | 'oneself')
        {self.not_alnum(1)}?
    ;

SHORTFORM_C
    :   {self.not_alnum(-1)}?
        ('ABOUT' | 'ABOVE' | 'ACCORDING' | 'ACROSS' | 'AFTER' | 'AFTERNOON' | 'AFTERWARD' | 'AGAIN' | 'AGAINST' | 'ALSO' | 'ALMOST' | 'ALREADY' | 'ALTOGETHER' | 'ALTHOUGH' | 'ALWAYS' | 'BLIND' | 'BRAILLE' | 'COULD' | 'DECLARE' | 'DECLARING' | 'DECEIVE' | 'DECEIVING' | 'EITHER' | 'FRIEND' | 'FIRST' | 'GOOD' | 'GREAT' | 'HIM' | 'HIMSELF' | 'HERSELF' | 'IMMEDIATE' | 'LITTLE' | 'LETTER' | 'MYSELF' | 'MUCH' | 'MUST' | 'NECESSARY' | 'NEITHER' | 'PAID' | 'PERCEIVE' | 'PERCEIVING' | 'PERHAPS' | 'QUICK' | 'RECEIVE' | 'RECEIVING' | 'REJOICE' | 'REJOICING' | 'SAID' | 'SUCH' | 'TODAY' | 'TOGETHER' | 'TOMORROW' | 'TONIGHT' | 'ITSELF' | 'ITS' | 'YOUR' | 'YOURSELF' | 'YOURSELVES' | 'THEMSELVES' | 'CHILDREN' | 'SHOULD' | 'THYSELF' | 'OURSELVES' | 'WOULD' | 'BECAUSE' | 'BEFORE' | 'BEHIND' | 'BELOW' | 'BENEATH' | 'BESIDE' | 'BETWEEN' | 'BEYOND' | 'CONCEIVE' | 'CONCEIVING' | 'ONESELF')
        {self.not_alnum(1)}?
    ;

SHORTFORM_F
    :   {self.not_alnum(-1)}?
        ('About' | 'Above' | 'According' | 'Across' | 'After' | 'Afternoon' | 'Afterward' | 'Again' | 'Against' | 'Also' | 'Almost' | 'Already' | 'Altogether' | 'Although' | 'Always' | 'Blind' | 'Braille' | 'Could' | 'Declare' | 'Declaring' | 'Deceive' | 'Deceiving' | 'Either' | 'Friend' | 'First' | 'Good' | 'Great' | 'Him' | 'Himself' | 'Herself' | 'Immediate' | 'Little' | 'Letter' | 'Myself' | 'Much' | 'Must' | 'Necessary' | 'Neither' | 'Paid' | 'Perceive' | 'Perceiving' | 'Perhaps' | 'Quick' | 'Receive' | 'Receiving' | 'Rejoice' | 'Rejoicing' | 'Said' | 'Such' | 'Today' | 'Together' | 'Tomorrow' | 'Tonight' | 'Itself' | 'Its' | 'Your' | 'Yourself' | 'Yourselves' | 'Themselves' | 'Children' | 'Should' | 'Thyself' | 'Ourselves' | 'Would' | 'Because' | 'Before' | 'Behind' | 'Below' | 'Beneath' | 'Beside' | 'Between' | 'Beyond' | 'Conceive' | 'Conceiving' | 'Oneself')
        {self.not_alnum(1)}?
    ;

STRONG_GROUPSIGN_L
    :
        'ch' | 'gh' | 'sh' | 'th' | 'wh' | 'ed' | 'er' | 'ou' | 'ow' | 'st' | 'ing' | 'ar'
    ;

STRONG_GROUPSIGN_C
    :
        'CH' | 'GH' | 'SH' | 'TH' | 'WH' | 'ED' | 'ER' | 'OU' | 'OW' | 'ST' | 'ING' | 'AR'
    ;

STRONG_GROUPSIGN_F
    :
        'Ch' | 'Gh' | 'Sh' | 'Th' | 'Wh' | 'Ed' | 'Er' | 'Ou' | 'Ow' | 'St' | 'Ing' | 'Ar'
    ;

DOT : '.';
COMMA : ',';
APOSTROPHE : '\'';
COLON : ':';
UNDERSCORE : '_';
LONG_DASH : '—';
DASH : '–';
EXCLAMATION : '!';
HYPHEN : '-';
QUESTION : '?';
SEMICOLON : ';';
SLASH : '/';
BACKSLASH : '\\';
QUOTATION_OPEN : '“';
QUOTATION_CLOSE : '”';
SINGLE_QUOTE_OPEN : '‘';
SINGLE_QUOTE_CLOSE : '’';
DOUBLE_QUOTE : '"';

LPAREN : '(';
RPAREN : ')';
LBRACK : '[';
RBRACK : ']';
LCURLY : '{';
RCURLY : '}';
LANGLE : '<';
RANGLE : '>';

PLUS : '+';
EQUALS : '=';
STAR : '*';
CARET : '^';

EURO : '€';
DOLLAR : '$';
POUND : '£';


    Lowercase
            :   [a-z]
            ;

    Uppercase
        :   [A-Z]
        ;

    Digit
        :   [0-9]
        ;

    Space
        :   ' '
        ;

    Newline
        :   (   '\r' '\n'?
            |   '\n'
            )
            -> skip
        ;





