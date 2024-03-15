# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\drum_group.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 726 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import DrumGroupComponent as DrumGroupComponentBase
from .util import skin_scroll_buttons

class DrumGroupComponent(DrumGroupComponentBase):

    def __init__(self, *a, **k):
        (super(DrumGroupComponent, self).__init__)(*a, **k)
        skin_scroll_buttons(self._position_scroll, "DrumGroup.Navigation", "DrumGroup.NavigationPressed")
        skin_scroll_buttons(self._page_scroll, "DrumGroup.Navigation", "DrumGroup.NavigationPressed")

    def set_parent_track(self, track):
        pass

# okay decompiling ./MIDIRemoteScripts/novation/drum_group.pyc
