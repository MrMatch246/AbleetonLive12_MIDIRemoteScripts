# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\fixed_length_recording.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1269 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
NUM_LENGTHS = 8

def track_can_record(track):
    return track.can_be_armed and (track.arm or track.implicit_arm)


class FixedLengthRecording(object):

    def __init__(self, song=None, fixed_length_setting=None, *a, **k):
        (super(FixedLengthRecording, self).__init__)(*a, **k)
        self._song = song
        self._fixed_length_setting = fixed_length_setting

    def should_start_recording_in_slot(self, clip_slot):
        return track_can_record(clip_slot.canonical_parent) and not clip_slot.is_recording and not clip_slot.has_clip and self._fixed_length_setting.enabled

    def start_recording_in_slot(self, clip_slot):
        if self.should_start_recording_in_slot(clip_slot):
            clip_slot.fire(record_length=(self._fixed_length_setting.get_selected_length(self._song)))
        else:
            clip_slot.fire()

# okay decompiling ./MIDIRemoteScripts/novation/fixed_length_recording.pyc
