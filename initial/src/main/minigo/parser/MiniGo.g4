grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
    language=Python3;
}

// Lexical structure
VAR: 'var';
FUNC: 'func';
INT: 'int';
LP: '(';
RP: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ADD: '+';
ASSIGN: '=';
PRINT: 'print';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

INT_LIT: [0-9]+;

COMMENTS: '##' ~[\n]* -> skip; // Comments
WS: [ \t\r\f\b\n]+ -> skip; // skip spaces, tabs

ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise IllegalEscape(self.text)};
UNCLOSE_STRING: . {raise UncloseString(self.text)};

// Parser structure
program: decl+ EOF;

decl: funcdecl | vardecl;

vardecl: VAR ID INT SEMI;

funcdecl: FUNC ID LP RP LBRACE RBRACE SEMI;

// Statements
statement: (declaration_statement | call_statement);
declaration_statement: INT ID ASSIGN expression SEMI;
call_statement: PRINT LP expression RP SEMI;

// Expression
expression: expression1 ADD expression | expression1;
expression1: ID | INT_LIT;