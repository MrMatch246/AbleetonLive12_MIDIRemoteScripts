# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Akai_Force_MPC\sysex_element.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 355 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import SysexElement

class IdentifyingSysexElement(SysexElement):

    def receive_value(self, _):
        value = self._msg_sysex_identifier[3]
        self.notify_value(value)

# okay decompiling ./MIDIRemoteScripts/Akai_Force_MPC/sysex_element.pyc
