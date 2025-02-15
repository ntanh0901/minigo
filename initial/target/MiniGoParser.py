# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6/\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\tB\n\t\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3")
        buf.write("\2\16\17\2@\2\25\3\2\2\2\4\35\3\2\2\2\6\37\3\2\2\2\b$")
        buf.write("\3\2\2\2\n.\3\2\2\2\f\60\3\2\2\2\16\66\3\2\2\2\20A\3\2")
        buf.write("\2\2\22C\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32\7")
        buf.write("\2\2\3\32\3\3\2\2\2\33\36\5\b\5\2\34\36\5\6\4\2\35\33")
        buf.write("\3\2\2\2\35\34\3\2\2\2\36\5\3\2\2\2\37 \7\3\2\2 !\7\16")
        buf.write("\2\2!\"\7\5\2\2\"#\7\n\2\2#\7\3\2\2\2$%\7\4\2\2%&\7\16")
        buf.write("\2\2&\'\7\6\2\2\'(\7\7\2\2()\7\b\2\2)*\7\t\2\2*+\7\n\2")
        buf.write("\2+\t\3\2\2\2,/\5\f\7\2-/\5\16\b\2.,\3\2\2\2.-\3\2\2\2")
        buf.write("/\13\3\2\2\2\60\61\7\5\2\2\61\62\7\16\2\2\62\63\7\f\2")
        buf.write("\2\63\64\5\20\t\2\64\65\7\n\2\2\65\r\3\2\2\2\66\67\7\r")
        buf.write("\2\2\678\7\6\2\289\5\20\t\29:\7\7\2\2:;\7\n\2\2;\17\3")
        buf.write("\2\2\2<=\5\22\n\2=>\7\13\2\2>?\5\20\t\2?B\3\2\2\2@B\5")
        buf.write("\22\n\2A<\3\2\2\2A@\3\2\2\2B\21\3\2\2\2CD\t\2\2\2D\23")
        buf.write("\3\2\2\2\6\27\35.A")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'func'", "'int'", "'('", "')'", 
                     "'{'", "'}'", "';'", "'+'", "'='", "'print'" ]

    symbolicNames = [ "<INVALID>", "VAR", "FUNC", "INT", "LP", "RP", "LBRACE", 
                      "RBRACE", "SEMI", "ADD", "ASSIGN", "PRINT", "ID", 
                      "INT_LIT", "COMMENTS", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3
    RULE_statement = 4
    RULE_declaration_statement = 5
    RULE_call_statement = 6
    RULE_expression = 7
    RULE_expression1 = 8

    ruleNames =  [ "program", "decl", "vardecl", "funcdecl", "statement", 
                   "declaration_statement", "call_statement", "expression", 
                   "expression1" ]

    EOF = Token.EOF
    VAR=1
    FUNC=2
    INT=3
    LP=4
    RP=5
    LBRACE=6
    RBRACE=7
    SEMI=8
    ADD=9
    ASSIGN=10
    PRINT=11
    ID=12
    INT_LIT=13
    COMMENTS=14
    WS=15
    ERROR_CHAR=16
    ILLEGAL_ESCAPE=17
    UNCLOSE_STRING=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.decl()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.VAR or _la==MiniGoParser.FUNC):
                    break

            self.state = 23
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.funcdecl()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MiniGoParser.VAR)
            self.state = 30
            self.match(MiniGoParser.ID)
            self.state = 31
            self.match(MiniGoParser.INT)
            self.state = 32
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MiniGoParser.FUNC)
            self.state = 35
            self.match(MiniGoParser.ID)
            self.state = 36
            self.match(MiniGoParser.LP)
            self.state = 37
            self.match(MiniGoParser.RP)
            self.state = 38
            self.match(MiniGoParser.LBRACE)
            self.state = 39
            self.match(MiniGoParser.RBRACE)
            self.state = 40
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declaration_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.state = 42
                self.declaration_statement()
                pass
            elif token in [MiniGoParser.PRINT]:
                self.state = 43
                self.call_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = MiniGoParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MiniGoParser.INT)
            self.state = 47
            self.match(MiniGoParser.ID)
            self.state = 48
            self.match(MiniGoParser.ASSIGN)
            self.state = 49
            self.expression()
            self.state = 50
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MiniGoParser.PRINT, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MiniGoParser.PRINT)
            self.state = 53
            self.match(MiniGoParser.LP)
            self.state = 54
            self.expression()
            self.state = 55
            self.match(MiniGoParser.RP)
            self.state = 56
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.expression1()
                self.state = 59
                self.match(MiniGoParser.ADD)
                self.state = 60
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = MiniGoParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





