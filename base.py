# -*- coding: utf-8 -*-
"""
.. module:: edl.base
    :synopsis: base classes that make up EDLs and some utilities

copyright 2015 Sebastian Haas
"""

__all__ = ['TimeCode', 'TCFPS', 'Event', 'Clip', 'Comment', 'Motion']

def hhmmss(seconds):
    """ convert seconds into hours, minutes and seconds

    Args:
        seconds: number representing seconds

    Returns:
        dictionary: HH: hours, MM: minutes, SS: seconds
    """
    ret = {}

    ret['HH'] = int(seconds / 3600)
    seconds -= ret['HH'] * 3600

    ret['MM'] = int(seconds / 60)
    seconds -= ret['MM'] * 60

    ret['SS'] = int(seconds)

    return ret

class TCFPS(object):
    """ Time Code aware frames per second, can handle drop frames """
    def __init__(self, fps, drop_frame=False):
        """
        Args:
            fps: frames per second
            drop_frame: whether we're dropping frames cause we don't know how to count
        """

        self._fps = fps
        self._drop_frame = drop_frame
        if not self.drop_frame:
            self._frame_duration = self._fps
        else:
            self._frame_duration = self._fps * (1000.0/1001.0)

    @property
    def fps(self):
        return self._fps

    @property
    def drop_frame(self):
        return self._drop_frame

    @property
    def frame_duration(self):
        return self._frame_duration

    def hhmmssff(self, frames):
        """ returns frames as a time code string

        Args:
            frames: an integer count of frames

        Returns:
            dictionary: :func:`hhmmss` plus FF: subsecond frames
        """
        ret = {}

        if self._drop_frame:
            frames += self.count_dropped_frames(frames)

        ret['FF'] = int(frames % self.fps)
        seconds = int(frames / self.fps)

        ret.update(hhmmss(seconds))

        return ret

    def validate(self, tc_str):
        """ validates a time code string against the fps setting we represent

        Args:
            tc_str: a string representing a timecode of the form HH:MM:SS:FF

        Returns:
            array: list of errors found in the time code string, empty if it's all ok
        """
        errors = []

        (hh, mm , ss, ff) = map(int, tc_str.split(':'))

        if ff > self.fps:
            errors.append('Frames {ff} greater than frames per second {fps}'.format(ff=ff, fps=self.fps))

        if self.drop_frame:
            if ss == 0 and mm and mm % 10: # yup, drop frames are awesome
                if ff in [0, 1]:
                    errors.append('Invalid drop frame timecode {tc}'.format(tc=tc_str))

        return errors

    def count_dropped_frames(self, frames):
        """ count frames we didn't count cause they drank too much when they designed ntsc

        Args:
            frames: integer count of frames

        Returns:
            int: how many frames will be skipped
        """
        fpm = self._fps * 60
        if not self._drop_frame:
            return 0
        # drop frames 0 and 1 each first second every minute, except each 10th minute
        # yeah, seriously...
        minutes = int(frames / fpm)
        if not minutes:
            return 0

        minutes -= int(minutes / 10)
        drop_frames = 2 * (minutes - 1)
        frames -= (minutes - 1) * fpm
        drop_frames += min(2, frames % fpm)

        return drop_frames

    def tc_duration(self, tc_str):
        """ given a timecode string, return how many frames it represents

        Args:
            tc_str: a timecode string of the form HH:MM:SS:FF

        Returns:
            int: how many frames are represented by the timecode, minus drop frames if we're
               representing a timecode with drop frames

        Raises:
            ValueError: if the time code doesn't validate against our settings :func:`.validate`
        """
        (hh, mm , ss, ff) = map(int, tc_str.split(':'))

        errors = self.validate(tc_str)
        if errors:
            raise ValueError('\n'.join(errors))

        frames = ((hh * 3600 * self.fps) +
                  (mm * 60 * self.fps) +
                  (ss * self.fps) +
                  ff)
        drop_frames = self.count_dropped_frames(frames)
        frames -= drop_frames

        return frames

    def frames_to_tc(self, frames):
        """ returns a timecode dictionary representing some number of frames

        Args:
            frames: integer representing some number of frames

        Returns:
            dictionary: :func:`.hhmmssff` plus MS: miliseconds the FF part represents
        """
        ret = self.hhmmssff(frames)

        ret['MS'] = float(ret['FF'] / self.frame_duration)

        return ret

    def __eq__(self, other):
        """ magic method comparing us to another TCFPS instance """
        return (self.fps == other.fps) and (self.drop_frame == other.drop_frame)

    def __str__(self):
        return '{fps}({fd})'.format(fps=self.fps, fd=self.frame_duration)

class TimeCode(object):
    """ Class encapsulating a number of frames and the FPS they should be running at,
        can handle drop frames
    """
    def __init__(self, tc_frames, tc_fps):
        self._frames = int(tc_frames)
        self._tc_fps    = tc_fps

        self._tc = self._tc_fps.frames_to_tc(self._frames)

    @property
    def frames(self):
        return self._frames

    @property
    def fps(self):
        return self._tc_fps

    @property
    def tc(self):
        return self._tc

    def __str__(self):
        return '{HH:02d}:{MM:02d}:{SS:02d}:{FF:02d}'.format(**self._tc)

    def __sub__(self, other):
        """magic method supporting subtraction operator
        Args:
            other: another TimeCode

        Returns:
            TimeCode: a TimeCode object representing the difference between us and the other TimeCode

        Raises:
            TypeError: if the other's fps is different from outs
        """
        if self.fps != other.fps:
            raise TypeError('{fps} != {ofps}'.format(fps=self.fps, ofps=other.fps))

        return TimeCode(self.frames - other.frames, self.fps)

    def __add__(self, other):
        """magic method supporting addition operator
        Args:
            other: another TimeCode

        Returns:
            TimeCode: a TimeCode object representing the addition between us and the other TimeCode

        Raises:
            TypeError: if the other's fps is different from outs
        """
        if self.fps != other.fps:
            raise TypeError('{fps} != {ofps}'.format(fps=self.fps, ofps=other.fps))

        return TimeCode(self.frames + other.frames, self.fps)

    def __abs__(self):
        """magic method returning the absolute of our frames

        Returns:
            TimeCode: Timecode with the same magnitute of frames as us
        """
        return TimeCode(abs(self.frames), self.fps)

# end class TimeCode


class TimeCodeTC(TimeCode):
    """TimeCode subclass which also holds the timecode dictionary of the frames
    """
    def __init__(self, tc_str, tc_fps):
        # SKIP __init__ of base class
        self._tc_str = tc_str
        self._tc_fps = tc_fps

        self._frames = self._tc_fps.tc_duration(self._tc_str)
        self._tc     = self._tc_fps.frames_to_tc(self._frames)

# end class TimeCodeTC


class TimeSpan(object):
    """Class representing a duration between to TimeCodes, OUT inclusive"""
    def __init__(self, ts_in, ts_out):
        self._in  = ts_in
        self._out = ts_out

    @property
    def duration(self):
        return self._out - self._in

    @property
    def IN(self):
        return self._in

    @property
    def OUT(self):
        return self._out

    def __contains__(self, frame):
        """ magic method for the 'in' operation
        Args:
            frame: frame number to check for

        Returns:
            bool: True if frame falls between our IN and OUT point, False else
        """
        return (frame >= self._in) and (frame <= self._out)

# end class TimeSpan

class Event(object):
    """Class representing an EDL event"""
    def __init__(self, ev_edl, ev_nr, ev_channel, ev_type):
        """
        Args:
            ev_edl: the EDL we're a part of
            ev_nr: the number we have in the EDL
            ev_channel: the channel we're in in the EDL
            ev_type: the type of EDL event we are
        """
        self._edl       = ev_edl
        self._nr        = int(ev_nr)
        self._channel   = ev_channel
        self._type      = ev_type
        self._comments  = {}
        self._modifiers = []

        self._reel   = ''

        self._src = None
        self._dst = None

        self._srcin  = TimeCode(0, self._edl.fps)
        self._srcout = TimeCode(0, self._edl.fps)
        self._dstin  = TimeCode(0, self._edl.fps)
        self._dstout = TimeCode(0, self._edl.fps)

    def __str__(self):
        output = ['{nr:03d} {reel} {channel} {type} {srcin} {srcout} {dstin} {dstout}'.format(nr=self._nr, reel=self._reel,
                                                                                              channel=self._channel,  type=self._type,
                                                                                              srcin=self._srcin, srcout=self._srcout,
                                                                                              dstin=self._dstin, dstout=self._dstout)]
        for key, value in self._comments.items():
            output.append('* {key}: {value}'.format(key=key, value=value))

        for modifier in self._modifiers:
            output.append(str(modifier))

        return "\n".join(output)

    def process_timecodes(self):
        """ helper method filling src and destination duration attributes """
        self._src  = TimeSpan(self._srcin, self._srcout)
        self._dst  = TimeSpan(self._dstin, self._dstout)

    def set_reel(self, ev_reel):
        self._reel = ev_reel
    def set_srcin(self, tc_str):
        self._srcin = TimeCodeTC(tc_str, self._edl.fps)
    def set_srcout(self, tc_str):
        self._srcout = TimeCodeTC(tc_str, self._edl.fps)
    def set_dstin(self, tc_str):
        self._dstin = TimeCodeTC(tc_str, self._edl.fps)
    def set_dstout(self, tc_str):
        self._dstout = TimeCodeTC(tc_str, self._edl.fps)

    def src_to_dst(self, frame):
        """ returns the edit timecode of a source frame, does not take motion into account

        Args:
            frame: a frame number

        Returns:
            TimeCode: a TimeCode instance representing the edit timecode of the source frame

        Raises:
            KeyError: if the frame is not in our source duration
        """
        if frame not in self._src:
            raise KeyError()

        return TimeCode((frame - self._src.IN) + self._dst.IN, self._src.fps)

    def dst_to_src(self, frame):
        """ returns the source timecode of an edit frame, does not take motion into account

        Args:
            frame: a frame number

        Returns:
            TimeCode: a TimeCode instance representing the source timecode of the edit frame

        Raises:
            KeyError: if the frame is not in our edit duration
        """
        if frame not in self._dst:
            raise KeyError()

        return TimeCode((frame - self._dst.IN) + self._src.IN, self._src.fps)

    def add_comment(self, comment):
        self._comments[comment.key] = comment.value

    def add_modifier(self, modifier):
        self._modifiers.append(modifier)

# end class Event


class Clip(object):
    """ Class representing a clip used in an edl, keeps track of events usage this clip """
    def __init__(self, clip_name, edl):
        """
        Args:
            clip_name: the name of the clip used
            edl: the edl the clip is used in
        """
        self._clip_name = clip_name
        self._edl       = edl

        self._event_nrs = []
        self._dst_duration = TimeCode(0, self._edl.fps)
        self._src_duration = TimeCode(0, self._edl.fps)

    def add_event(self, ev):
        """ add an event that uses this clip, record its duration
        Args:
            ev: an Event instance
        """
        self._event_nrs.append(ev._nr)
        self._dst_duration += abs(ev._dst.duration)
        self._src_duration += abs(ev._src.duration)

# end class Clip


class Comment(object):
    """ EDL Event comment, mostly geared towards FROM/TO CLIP NAME style comments """
    def __init__(self, key=None, value=None):
        self.key   = key
        self.value = value
# end class Comment

class Motion(object):
    """ EDL Event motion (M2), meaning speed up/down/reverse """
    def __init__(self, edl):
        self._edl = edl

        self._reel  = ''
        self._speed = '100.0' # TODO: convert to float here and reformat in __str__
        self._srcin = TimeCode(0, self._edl.fps)

    def set_reel(self, reel):
        self._reel = reel

    def set_speed(self, speed):
        self._speed = speed

    def set_srcin(self, tc_str):
        self._srcin = TimeCodeTC(tc_str, self._edl.fps)

    def __str__(self):
        return 'M2 {reel} {speed} {srcin}'.format(reel=self._reel,
                                                  speed=self._speed,
                                                  srcin=self._srcin)
# end class Motion
