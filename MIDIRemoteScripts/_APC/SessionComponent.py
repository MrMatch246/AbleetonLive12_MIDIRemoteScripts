# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_APC\SessionComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 649 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.SessionComponent import SessionComponent as SessionComponentBase

class SessionComponent(SessionComponentBase):

    def link_with_track_offset(self, track_offset):
        if self._is_linked():
            self._unlink()
        self.set_offsets(track_offset, self.scene_offset())
        self._link()

    def unlink(self):
        if self._is_linked():
            self._unlink()

# okay decompiling ./MIDIRemoteScripts/_APC/SessionComponent.pyc
