grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    # Use the token type to raise appropriate exceptions, as per spec.
    if tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text)
    elif tk == self.UNCLOSE_STRING:
        result = super().emit()
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscapeInString(result.text)
    else:
        return super().emit()
}

options {
    language=Python3;
}

/*-------------------------------------------------------------------
  LEXER RULES
  Update string rules for correct handling of unclosed strings
  and illegal escapes, as indicated by the spec.
-------------------------------------------------------------------*/

/*
  A valid string allows sequences of:
   - Any character except backslash, newline, double-quote
   - Certain recognized escape sequences
*/
STRING_LIT
  : '"' (ESC_SEQ | SAFECODEPOINT)* '"'
  ;

/*
  Detect unclosed strings by encountering a newline (or EOF) before
  encountering a closing quote.
*/
UNCLOSE_STRING
  : '"' (ESC_SEQ | SAFECODEPOINT)* ([\r\n] | EOF)
  ;

/*
  Detect illegal escape by encountering a backslash followed by something
  that is not in the recognized escapes. We separate this out so
  that 'emit' can raise IllegalEscapeInString.
*/
ILLEGAL_ESCAPE
  : '"' ( (ESC_SEQ | SAFECODEPOINT)* ILLEGAL_ESC_CHAR .* )?
    { /* We'll rely on the emit function to raise the exception. */ }
  ;

/*
  Fragment for recognized (legal) escapes.
  Adjust as needed based on your language specs: b, f, n, r, t, etc.
*/
fragment ESC_SEQ
  : '\\' [bfnrt\"\\]
  ;

/*
  Fragment for characters in a string that are not escapes.
*/
fragment SAFECODEPOINT
  : ~["\\\r\n]
  ;

/*
  Fragment for detecting unrecognized escape usage. 
  For example: "\z" or "\&" that should raise error.
*/
fragment ILLEGAL_ESC_CHAR
  : '\\' ~( [bfnrt\"\\] )
  ;

/*
  Single unrecognized character outside of string coverage
*/
ERROR_CHAR
  : .
  ;

/*-------------------------------------------------------------------
  KEYWORDS/TOKENS
-------------------------------------------------------------------*/
VAR   : 'var';
FUNC  : 'func';
INT   : 'int';
LP    : '(';
RP    : ')';
LBRACE: '{';
RBRACE: '}';
SEMI  : ';';
ADD   : '+';
ASSIGN: '=';
PRINT : 'print';

/*-------------------------------------------------------------------
  IDENTIFIERS & LITERALS
-------------------------------------------------------------------*/
ID
  : [a-zA-Z_] [a-zA-Z0-9_]*
  ;

INT_LIT
  : [0-9]+
  ;

/*-------------------------------------------------------------------
  COMMENTS & WHITESPACE
-------------------------------------------------------------------*/
COMMENTS
  : '##' ~[\n]* -> skip
  ;

WS
  : [ \t\r\f\b\n]+ -> skip
  ;

/*-------------------------------------------------------------------
  PARSER RULES
-------------------------------------------------------------------*/
program
  : decl+ EOF
  ;

decl
  : funcdecl
  | vardecl
  ;

vardecl
  : VAR ID INT SEMI
  ;

funcdecl
  : FUNC ID LP RP LBRACE RBRACE SEMI
  ;

// Statements
statement
  : declaration_statement
  | call_statement
  ;

declaration_statement
  : INT ID ASSIGN expression SEMI
  ;

call_statement
  : PRINT LP expression RP SEMI
  ;

// Expression
expression
  : expression ADD expression1
  | expression1
  ;

expression1
  : ID
  | INT_LIT
  | STRING_LIT
  ;