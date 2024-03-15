# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MiniLab_3\drum_group.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 592 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.components import DrumGroupComponent as DrumGroupComponentBase
from ableton.v3.control_surface.controls import PlayableControl

class DrumGroupComponent(DrumGroupComponentBase):

    def set_matrix(self, matrix):
        super().set_matrix(matrix)
        for button in self.matrix:
            button.set_mode(PlayableControl.Mode.playable_and_listenable)
            button.pressed_color = "DrumGroup.PadPressed"

# okay decompiling ./MIDIRemoteScripts/MiniLab_3/drum_group.pyc
