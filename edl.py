# -*- coding: utf-8 -*-
"""
.. module:: edl
    :synopsis: EDL class, can parse CMX 3600 files

copyright 2015 Sebastian Haas
"""

__all__ = ['EDL']

import os
from pprint import pprint, pformat

import antlr4

import base
reload(base)

import edlLexer
reload(edlLexer)
import edlParser
reload(edlParser)
import edlListener
reload(edlListener)

def get_line_from_file(f, linenr):
    """return one line from a file

    Args:
        f: a path to a file
        linenr: the line to return (1 based index)

    Returns:
        string: the line from the file

    Raises:
        IOError: when there's something wrong with f
        IndexError: if there's not enough lines in f
    """
    #: TODO should be replaced by a more clever usage of antlr4
    return open(f).readlines()[linenr-1]

class EDL(edlListener.edlListener):
    """EDL parser/representation, most of the heavy lifting is done by antlr4 through
       a custom grammer constructed from 'edl.g'
    """
    def __init__(self, edl_filename, edl_fps):
        """
        Args:
            edl_filename: The filename to an EDL file
            edl_fps: the fps the edl is in, since EDLs don't carry that information with them
        """
        self._filename = edl_filename
        self._tc_fps   = edl_fps
        self._title    = ''
        self._fcm      = ''

        self._current_comment = None
        self._current_event   = None

        self._from_clips = {}
        self._events = {}
        self._next_ev_number = 1

        if self._filename is not None:
            (_, ext) = os.path.splitext(self._filename)
            if ext.lower() == '.edl':
                self.parse_edl()

    @property
    def fps(self):
        return self._tc_fps

    @property
    def src_duration(self):
        """
        Returns:
            int: the number of source frames used in this EDL overall
        """
        duration = base.TimeCode(0, self.fps)
        for nr, event in self._events.items():
            # the clip might run backwards (through a motion modifier on the Event)
            # so we take the absolute number of frames here
            duration += abs(event._src.duration)

        return duration

    @property
    def dst_duration(self):
        """
        Returns:
            int: the number of edit frames this EDL is long
        """
        duration = base.TimeCode(0, self.fps)
        for nr, event in self._events.items():
            # the clip might run backwards (through a motion modifier on the Event)
            # so we take the absolute number of frames here
            duration += abs(event._dst.duration)

        return duration

    def next_ev_number(self):
        """
        Returns:
           int: the next available number for an EDL event
        """
        return self._next_ev_number

    def add_event(self, ev):
        """ adds an event to the EDL and increments the event number

        Args:
            ev: the event to add
        """
        if ev._nr >= self._next_ev_number:
            self._next_ev_number = ev._nr + 1
        self._events[ev._nr] = ev

    def _process_from_clips(self):
        """ processes all the 'FROM CLIP NAME' comments,
            making a list of all the clips used in the EDL and
            making a lookup table to remember which events used which clips
        """
        for ev in self._events.values():
            if 'FROM CLIP NAME' in ev._comments:
                fcn = ev._comments['FROM CLIP NAME']
            else:
                fcn = ev._reel

            if fcn not in self._from_clips:
                self._from_clips[fcn] = base.Clip(fcn, self)

            self._from_clips[fcn].add_event(ev)

    def parse_edl(self):
        """ main entry point to parse the EDL file we're representing
        """
        input = antlr4.FileStream(self._filename)
        lexer = edlLexer.edlLexer(input)
        stream = antlr4.CommonTokenStream(lexer)
        self.parser = edlParser.edlParser(stream)

        tree = self.parser.edl()

        #print tree.toStringTree()

        walker = antlr4.ParseTreeWalker()
        walker.walk(self, tree)

        self._process_from_clips()

    def write_out(self, f, regen_ev_nrs=True):
        """ writes out the EDL into a file like stream
        Args:
            f: a file like object supporting a 'write' method
            regen_ev_nrs: ignore existing event numbers and replace them with a running count
        """
        if regen_ev_nrs:
            ev_nr = 1
        f.write('TITIE: {title}\n'.format(title=self._title))
        if self._fcm:
            f.write('FCM: {fcm}\n'.format(fcm=self._fcm))
        for event in self._events.values():
            if regen_ev_nrs:
                event._nr = ev_nr
                ev_nr += 1
            f.write(str(event) + "\n")


    def enterEveryRule(self, ctx):
        """ antlr4 overloaded method, called whenever a grammer rule is entered
        Args:
            ctx: antlr4 parsing context
        """
        if   isinstance(ctx, self.parser.EventContext):
            self._current_event = base.Event(self, ctx.EVNR().getText(), ctx.EVCHANNEL().getText(), ctx.EVTYPE().getText())
        elif isinstance(ctx, self.parser.CommentContext):
            self._current_comment = base.Comment()
        elif isinstance(ctx, self.parser.MotionContext):
            self._current_motion = base.Motion(self)

    def exitEveryRule(self, ctx):
        """ antlr4 overloaded method, called whenever a grammer rule is exited
        Args:
            ctx: antlr4 parsing context
        """
        try:
            self._do_exitEveryRule(ctx)
        except Exception as e:
            line = get_line_from_file(self._filename, ctx.start.line)
            raise Exception('Error in line {line_nr}:<pre>{line}</pre>parsing {token}: {e}'.format(line_nr=ctx.start.line, line=line, token=ctx.start.text, e=e))

    def _do_exitEveryRule(self, ctx):
        """ main parsing function
        Args:
            ctx: antlr4 parsing context
        """
        # TITLE
        if   isinstance(ctx, self.parser.TitleContext):
            self._title = ' '.join(map(str, ctx.WORD()))
        # FCM
        elif isinstance(ctx, self.parser.FcmContext):
            self._fcm = ctx.FCMODE().getText()
        # COMMENT
        elif isinstance(ctx, self.parser.CommentkeyContext):
            self._current_comment.key   = ' '.join(map(str, ctx.WORD()))
        elif isinstance(ctx, self.parser.CommentvalueContext):
            self._current_comment.value = ' '.join(map(str, ctx.WORD()))
        elif isinstance(ctx, self.parser.CommentContext):
            self._current_event.add_comment(self._current_comment)
            self._current_comment = None
        # MOTION
        elif isinstance(ctx, self.parser.MotionreelContext):
            self._current_motion.set_reel(ctx.WORD().getText())
        elif isinstance(ctx, self.parser.MotionspeedContext):
            self._current_motion.set_speed(ctx.SPEED().getText())
        elif isinstance(ctx, self.parser.MotioninContext):
            self._current_motion.set_srcin(ctx.getText())
        elif isinstance(ctx, self.parser.MotionContext):
            self._current_event.add_modifier(self._current_motion)
            self._current_motion = None
        # EVENT
        elif isinstance(ctx, self.parser.EventContext):
            self._current_event.process_timecodes()
            self._events[self._current_event._nr] = self._current_event
        # EVENT TIMECODES
        elif isinstance(ctx, self.parser.SrcinContext):
            self._current_event.set_srcin(ctx.getText())
        elif isinstance(ctx, self.parser.SrcoutContext):
            self._current_event.set_srcout(ctx.getText())
        elif isinstance(ctx, self.parser.DstinContext):
            self._current_event.set_dstin(ctx.getText())
        elif isinstance(ctx, self.parser.DstoutContext):
            self._current_event.set_dstout(ctx.getText())
        # EVENT REEL
        elif isinstance(ctx, self.parser.ReelContext):
            self._current_event.set_reel(ctx.WORD().getText())

# end class EDL
