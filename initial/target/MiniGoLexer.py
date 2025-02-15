# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("o\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\7\rK\n\r\f\r\16\r")
        buf.write("N\13\r\3\16\6\16Q\n\16\r\16\16\16R\3\17\3\17\3\17\3\17")
        buf.write("\7\17Y\n\17\f\17\16\17\\\13\17\3\17\3\17\3\20\6\20a\n")
        buf.write("\20\r\20\16\20b\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\f\f\5\2\n")
        buf.write("\f\16\17\"\"\2r\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5+\3\2\2\2\7\60\3")
        buf.write("\2\2\2\t\64\3\2\2\2\13\66\3\2\2\2\r8\3\2\2\2\17:\3\2\2")
        buf.write("\2\21<\3\2\2\2\23>\3\2\2\2\25@\3\2\2\2\27B\3\2\2\2\31")
        buf.write("H\3\2\2\2\33P\3\2\2\2\35T\3\2\2\2\37`\3\2\2\2!f\3\2\2")
        buf.write("\2#i\3\2\2\2%l\3\2\2\2\'(\7x\2\2()\7c\2\2)*\7t\2\2*\4")
        buf.write("\3\2\2\2+,\7h\2\2,-\7w\2\2-.\7p\2\2./\7e\2\2/\6\3\2\2")
        buf.write("\2\60\61\7k\2\2\61\62\7p\2\2\62\63\7v\2\2\63\b\3\2\2\2")
        buf.write("\64\65\7*\2\2\65\n\3\2\2\2\66\67\7+\2\2\67\f\3\2\2\28")
        buf.write("9\7}\2\29\16\3\2\2\2:;\7\177\2\2;\20\3\2\2\2<=\7=\2\2")
        buf.write("=\22\3\2\2\2>?\7-\2\2?\24\3\2\2\2@A\7?\2\2A\26\3\2\2\2")
        buf.write("BC\7r\2\2CD\7t\2\2DE\7k\2\2EF\7p\2\2FG\7v\2\2G\30\3\2")
        buf.write("\2\2HL\t\2\2\2IK\t\3\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2")
        buf.write("LM\3\2\2\2M\32\3\2\2\2NL\3\2\2\2OQ\t\4\2\2PO\3\2\2\2Q")
        buf.write("R\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\34\3\2\2\2TU\7%\2\2UV\7")
        buf.write("%\2\2VZ\3\2\2\2WY\n\5\2\2XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2")
        buf.write("\2Z[\3\2\2\2[]\3\2\2\2\\Z\3\2\2\2]^\b\17\2\2^\36\3\2\2")
        buf.write("\2_a\t\6\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c")
        buf.write("d\3\2\2\2de\b\20\2\2e \3\2\2\2fg\13\2\2\2gh\b\21\3\2h")
        buf.write("\"\3\2\2\2ij\13\2\2\2jk\b\22\4\2k$\3\2\2\2lm\13\2\2\2")
        buf.write("mn\b\23\5\2n&\3\2\2\2\7\2LRZb\6\b\2\2\3\21\2\3\22\3\3")
        buf.write("\23\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAR = 1
    FUNC = 2
    INT = 3
    LP = 4
    RP = 5
    LBRACE = 6
    RBRACE = 7
    SEMI = 8
    ADD = 9
    ASSIGN = 10
    PRINT = 11
    ID = 12
    INT_LIT = 13
    COMMENTS = 14
    WS = 15
    ERROR_CHAR = 16
    ILLEGAL_ESCAPE = 17
    UNCLOSE_STRING = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'func'", "'int'", "'('", "')'", "'{'", "'}'", "';'", 
            "'+'", "'='", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "FUNC", "INT", "LP", "RP", "LBRACE", "RBRACE", "SEMI", 
            "ADD", "ASSIGN", "PRINT", "ID", "INT_LIT", "COMMENTS", "WS", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "VAR", "FUNC", "INT", "LP", "RP", "LBRACE", "RBRACE", 
                  "SEMI", "ADD", "ASSIGN", "PRINT", "ID", "INT_LIT", "COMMENTS", 
                  "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[15] = self.ERROR_CHAR_action 
            actions[16] = self.ILLEGAL_ESCAPE_action 
            actions[17] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text)
     


