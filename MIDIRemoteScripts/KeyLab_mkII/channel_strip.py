# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mkII\channel_strip.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 893 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.control import TextDisplayControl
from KeyLab_Essential.channel_strip import ChannelStripComponent as ChannelStripComponentBase

class ChannelStripComponent(ChannelStripComponentBase):
    track_name_display = TextDisplayControl(" ")

    def set_track_name_display(self, display):
        self.track_name_display.set_control_element(display)
        self._update_track_name_display()

    def set_track(self, track):
        super(ChannelStripComponent, self).set_track(track)
        self._update_track_name_display()

    def _update_track_name_display(self):
        track = self._track
        self.track_name_display[0] = track.name if liveobj_valid(track) else ""

# okay decompiling ./MIDIRemoteScripts/KeyLab_mkII/channel_strip.pyc
