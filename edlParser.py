# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .edlListener import edlListener
else:
    from edlListener import edlListener

#package de.blinkenlicht.helloworld.parsers;
                
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\21|\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4")
        buf.write(u"\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write(u"\t\23\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write(u"\3\b\3\b\3\b\6\b\66\n\b\r\b\16\b\67\3\b\5\b;\n\b\3\t")
        buf.write(u"\3\t\3\t\3\t\5\tA\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write(u"\3\n\3\n\3\13\6\13N\n\13\r\13\16\13O\3\f\6\fS\n\f\r\f")
        buf.write(u"\16\fT\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\5\21i\n\21\3\22")
        buf.write(u"\3\22\7\22m\n\22\f\22\16\22p\13\22\6\22r\n\22\r\22\16")
        buf.write(u"\22s\3\23\3\23\3\23\3\23\5\23z\n\23\3\23\2\2\24\2\4\6")
        buf.write(u"\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\2r\2&\3\2\2\2")
        buf.write(u"\4(\3\2\2\2\6*\3\2\2\2\b,\3\2\2\2\n.\3\2\2\2\f\60\3\2")
        buf.write(u"\2\2\16:\3\2\2\2\20@\3\2\2\2\22B\3\2\2\2\24M\3\2\2\2")
        buf.write(u"\26R\3\2\2\2\30V\3\2\2\2\32\\\3\2\2\2\34^\3\2\2\2\36")
        buf.write(u"`\3\2\2\2 h\3\2\2\2\"q\3\2\2\2$u\3\2\2\2&\'\7\20\2\2")
        buf.write(u"\'\3\3\2\2\2()\7\20\2\2)\5\3\2\2\2*+\7\20\2\2+\7\3\2")
        buf.write(u"\2\2,-\7\20\2\2-\t\3\2\2\2./\7\20\2\2/\13\3\2\2\2\60")
        buf.write(u"\61\7\17\2\2\61\r\3\2\2\2\62\63\7\3\2\2\63\65\7\7\2\2")
        buf.write(u"\64\66\7\17\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2")
        buf.write(u"\2\2\678\3\2\2\289\3\2\2\29;\7\13\2\2:\62\3\2\2\2:;\3")
        buf.write(u"\2\2\2;\17\3\2\2\2<=\7\4\2\2=>\7\7\2\2>?\7\f\2\2?A\7")
        buf.write(u"\13\2\2@<\3\2\2\2@A\3\2\2\2A\21\3\2\2\2BC\7\16\2\2CD")
        buf.write(u"\5\f\7\2DE\7\b\2\2EF\7\t\2\2FG\5\2\2\2GH\5\4\3\2HI\5")
        buf.write(u"\6\4\2IJ\5\b\5\2JK\7\13\2\2K\23\3\2\2\2LN\7\17\2\2ML")
        buf.write(u"\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\25\3\2\2\2QS")
        buf.write(u"\7\17\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\27")
        buf.write(u"\3\2\2\2VW\7\n\2\2WX\5\24\13\2XY\7\7\2\2YZ\5\26\f\2Z")
        buf.write(u"[\7\13\2\2[\31\3\2\2\2\\]\7\17\2\2]\33\3\2\2\2^_\7\r")
        buf.write(u"\2\2_\35\3\2\2\2`a\7\5\2\2ab\5\32\16\2bc\5\34\17\2cd")
        buf.write(u"\5\n\6\2de\7\13\2\2e\37\3\2\2\2fi\5\36\20\2gi\5\30\r")
        buf.write(u"\2hf\3\2\2\2hg\3\2\2\2i!\3\2\2\2jn\5\22\n\2km\5 \21\2")
        buf.write(u"lk\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2or\3\2\2\2pn")
        buf.write(u"\3\2\2\2qj\3\2\2\2rs\3\2\2\2sq\3\2\2\2st\3\2\2\2t#\3")
        buf.write(u"\2\2\2uv\5\16\b\2vw\5\20\t\2wy\5\"\22\2xz\7\21\2\2yx")
        buf.write(u"\3\2\2\2yz\3\2\2\2z%\3\2\2\2\13\67:@OThnsy")
        return buf.getvalue()


class edlParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'TITLE'", u"'FCM'", u"'M2'", u"<INVALID>", 
                     u"':'", u"<INVALID>", u"<INVALID>", u"'*'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"WS", u"ASSIGN", u"EVCHANNEL", u"EVTYPE", u"EVCOMMENTSIGN", 
                      u"NL", u"FCMODE", u"SPEED", u"EVNR", u"WORD", u"TIMECODE", 
                      u"FOOTER" ]

    RULE_srcin = 0
    RULE_srcout = 1
    RULE_dstin = 2
    RULE_dstout = 3
    RULE_motionin = 4
    RULE_reel = 5
    RULE_title = 6
    RULE_fcm = 7
    RULE_event = 8
    RULE_commentkey = 9
    RULE_commentvalue = 10
    RULE_comment = 11
    RULE_motionreel = 12
    RULE_motionspeed = 13
    RULE_motion = 14
    RULE_event_modifier = 15
    RULE_events = 16
    RULE_edl = 17

    ruleNames =  [ u"srcin", u"srcout", u"dstin", u"dstout", u"motionin", 
                   u"reel", u"title", u"fcm", u"event", u"commentkey", u"commentvalue", 
                   u"comment", u"motionreel", u"motionspeed", u"motion", 
                   u"event_modifier", u"events", u"edl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4
    ASSIGN=5
    EVCHANNEL=6
    EVTYPE=7
    EVCOMMENTSIGN=8
    NL=9
    FCMODE=10
    SPEED=11
    EVNR=12
    WORD=13
    TIMECODE=14
    FOOTER=15

    def __init__(self, input):
        super(edlParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SrcinContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.SrcinContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIMECODE(self):
            return self.getToken(edlParser.TIMECODE, 0)

        def getRuleIndex(self):
            return edlParser.RULE_srcin

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterSrcin(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitSrcin(self)




    def srcin(self):

        localctx = edlParser.SrcinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_srcin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(edlParser.TIMECODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SrcoutContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.SrcoutContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIMECODE(self):
            return self.getToken(edlParser.TIMECODE, 0)

        def getRuleIndex(self):
            return edlParser.RULE_srcout

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterSrcout(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitSrcout(self)




    def srcout(self):

        localctx = edlParser.SrcoutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_srcout)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(edlParser.TIMECODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DstinContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.DstinContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIMECODE(self):
            return self.getToken(edlParser.TIMECODE, 0)

        def getRuleIndex(self):
            return edlParser.RULE_dstin

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterDstin(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitDstin(self)




    def dstin(self):

        localctx = edlParser.DstinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dstin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(edlParser.TIMECODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DstoutContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.DstoutContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIMECODE(self):
            return self.getToken(edlParser.TIMECODE, 0)

        def getRuleIndex(self):
            return edlParser.RULE_dstout

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterDstout(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitDstout(self)




    def dstout(self):

        localctx = edlParser.DstoutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dstout)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(edlParser.TIMECODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MotioninContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.MotioninContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIMECODE(self):
            return self.getToken(edlParser.TIMECODE, 0)

        def getRuleIndex(self):
            return edlParser.RULE_motionin

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterMotionin(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitMotionin(self)




    def motionin(self):

        localctx = edlParser.MotioninContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_motionin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(edlParser.TIMECODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.ReelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(edlParser.WORD, 0)

        def getRuleIndex(self):
            return edlParser.RULE_reel

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterReel(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitReel(self)




    def reel(self):

        localctx = edlParser.ReelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_reel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(edlParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TitleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.TitleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(edlParser.ASSIGN, 0)

        def NL(self):
            return self.getToken(edlParser.NL, 0)

        def WORD(self, i=None):
            if i is None:
                return self.getTokens(edlParser.WORD)
            else:
                return self.getToken(edlParser.WORD, i)

        def getRuleIndex(self):
            return edlParser.RULE_title

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterTitle(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitTitle(self)




    def title(self):

        localctx = edlParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_title)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if _la==edlParser.T__0:
                self.state = 48
                self.match(edlParser.T__0)
                self.state = 49
                self.match(edlParser.ASSIGN)
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 50
                    self.match(edlParser.WORD)
                    self.state = 53 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==edlParser.WORD):
                        break

                self.state = 55
                self.match(edlParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FcmContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.FcmContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(edlParser.ASSIGN, 0)

        def FCMODE(self):
            return self.getToken(edlParser.FCMODE, 0)

        def NL(self):
            return self.getToken(edlParser.NL, 0)

        def getRuleIndex(self):
            return edlParser.RULE_fcm

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterFcm(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitFcm(self)




    def fcm(self):

        localctx = edlParser.FcmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fcm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if _la==edlParser.T__1:
                self.state = 58
                self.match(edlParser.T__1)
                self.state = 59
                self.match(edlParser.ASSIGN)
                self.state = 60
                self.match(edlParser.FCMODE)
                self.state = 61
                self.match(edlParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.EventContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EVNR(self):
            return self.getToken(edlParser.EVNR, 0)

        def reel(self):
            return self.getTypedRuleContext(edlParser.ReelContext,0)


        def EVCHANNEL(self):
            return self.getToken(edlParser.EVCHANNEL, 0)

        def EVTYPE(self):
            return self.getToken(edlParser.EVTYPE, 0)

        def srcin(self):
            return self.getTypedRuleContext(edlParser.SrcinContext,0)


        def srcout(self):
            return self.getTypedRuleContext(edlParser.SrcoutContext,0)


        def dstin(self):
            return self.getTypedRuleContext(edlParser.DstinContext,0)


        def dstout(self):
            return self.getTypedRuleContext(edlParser.DstoutContext,0)


        def NL(self):
            return self.getToken(edlParser.NL, 0)

        def getRuleIndex(self):
            return edlParser.RULE_event

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterEvent(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitEvent(self)




    def event(self):

        localctx = edlParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_event)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(edlParser.EVNR)
            self.state = 65
            self.reel()
            self.state = 66
            self.match(edlParser.EVCHANNEL)
            self.state = 67
            self.match(edlParser.EVTYPE)
            self.state = 68
            self.srcin()
            self.state = 69
            self.srcout()
            self.state = 70
            self.dstin()
            self.state = 71
            self.dstout()
            self.state = 72
            self.match(edlParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentkeyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.CommentkeyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i=None):
            if i is None:
                return self.getTokens(edlParser.WORD)
            else:
                return self.getToken(edlParser.WORD, i)

        def getRuleIndex(self):
            return edlParser.RULE_commentkey

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterCommentkey(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitCommentkey(self)




    def commentkey(self):

        localctx = edlParser.CommentkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_commentkey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.match(edlParser.WORD)
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==edlParser.WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentvalueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.CommentvalueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i=None):
            if i is None:
                return self.getTokens(edlParser.WORD)
            else:
                return self.getToken(edlParser.WORD, i)

        def getRuleIndex(self):
            return edlParser.RULE_commentvalue

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterCommentvalue(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitCommentvalue(self)




    def commentvalue(self):

        localctx = edlParser.CommentvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_commentvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self.match(edlParser.WORD)
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==edlParser.WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.CommentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EVCOMMENTSIGN(self):
            return self.getToken(edlParser.EVCOMMENTSIGN, 0)

        def commentkey(self):
            return self.getTypedRuleContext(edlParser.CommentkeyContext,0)


        def ASSIGN(self):
            return self.getToken(edlParser.ASSIGN, 0)

        def commentvalue(self):
            return self.getTypedRuleContext(edlParser.CommentvalueContext,0)


        def NL(self):
            return self.getToken(edlParser.NL, 0)

        def getRuleIndex(self):
            return edlParser.RULE_comment

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterComment(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitComment(self)




    def comment(self):

        localctx = edlParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(edlParser.EVCOMMENTSIGN)
            self.state = 85
            self.commentkey()
            self.state = 86
            self.match(edlParser.ASSIGN)
            self.state = 87
            self.commentvalue()
            self.state = 88
            self.match(edlParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MotionreelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.MotionreelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(edlParser.WORD, 0)

        def getRuleIndex(self):
            return edlParser.RULE_motionreel

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterMotionreel(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitMotionreel(self)




    def motionreel(self):

        localctx = edlParser.MotionreelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_motionreel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(edlParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MotionspeedContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.MotionspeedContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SPEED(self):
            return self.getToken(edlParser.SPEED, 0)

        def getRuleIndex(self):
            return edlParser.RULE_motionspeed

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterMotionspeed(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitMotionspeed(self)




    def motionspeed(self):

        localctx = edlParser.MotionspeedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_motionspeed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(edlParser.SPEED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MotionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.MotionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def motionreel(self):
            return self.getTypedRuleContext(edlParser.MotionreelContext,0)


        def motionspeed(self):
            return self.getTypedRuleContext(edlParser.MotionspeedContext,0)


        def motionin(self):
            return self.getTypedRuleContext(edlParser.MotioninContext,0)


        def NL(self):
            return self.getToken(edlParser.NL, 0)

        def getRuleIndex(self):
            return edlParser.RULE_motion

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterMotion(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitMotion(self)




    def motion(self):

        localctx = edlParser.MotionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_motion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(edlParser.T__2)
            self.state = 95
            self.motionreel()
            self.state = 96
            self.motionspeed()
            self.state = 97
            self.motionin()
            self.state = 98
            self.match(edlParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Event_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.Event_modifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def motion(self):
            return self.getTypedRuleContext(edlParser.MotionContext,0)


        def comment(self):
            return self.getTypedRuleContext(edlParser.CommentContext,0)


        def getRuleIndex(self):
            return edlParser.RULE_event_modifier

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterEvent_modifier(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitEvent_modifier(self)




    def event_modifier(self):

        localctx = edlParser.Event_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_event_modifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            token = self._input.LA(1)
            if token in [edlParser.T__2]:
                self.state = 100
                self.motion()

            elif token in [edlParser.EVCOMMENTSIGN]:
                self.state = 101
                self.comment()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.EventsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def event(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(edlParser.EventContext)
            else:
                return self.getTypedRuleContext(edlParser.EventContext,i)


        def event_modifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(edlParser.Event_modifierContext)
            else:
                return self.getTypedRuleContext(edlParser.Event_modifierContext,i)


        def getRuleIndex(self):
            return edlParser.RULE_events

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterEvents(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitEvents(self)




    def events(self):

        localctx = edlParser.EventsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_events)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.event()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==edlParser.T__2 or _la==edlParser.EVCOMMENTSIGN:
                    self.state = 105
                    self.event_modifier()
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==edlParser.EVNR):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EdlContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(edlParser.EdlContext, self).__init__(parent, invokingState)
            self.parser = parser

        def title(self):
            return self.getTypedRuleContext(edlParser.TitleContext,0)


        def fcm(self):
            return self.getTypedRuleContext(edlParser.FcmContext,0)


        def events(self):
            return self.getTypedRuleContext(edlParser.EventsContext,0)


        def FOOTER(self):
            return self.getToken(edlParser.FOOTER, 0)

        def getRuleIndex(self):
            return edlParser.RULE_edl

        def enterRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.enterEdl(self)

        def exitRule(self, listener):
            if isinstance( listener, edlListener ):
                listener.exitEdl(self)




    def edl(self):

        localctx = edlParser.EdlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_edl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.title()
            self.state = 116
            self.fcm()
            self.state = 117
            self.events()
            self.state = 119
            _la = self._input.LA(1)
            if _la==edlParser.FOOTER:
                self.state = 118
                self.match(edlParser.FOOTER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




