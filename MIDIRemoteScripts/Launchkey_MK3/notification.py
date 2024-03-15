# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK3\notification.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1113 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import task
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import control_list
from .control import DisplayControl
CLEAR_DELAY = 5

class NotificationComponent(Component):
    display_lines = control_list(DisplayControl, control_count=2)

    def __init__(self, *a, **k):
        (super(NotificationComponent, self).__init__)(*a, **k)
        self._clear_notification_task = self._tasks.add(task.sequence(task.wait(CLEAR_DELAY), task.run(self._clear_notification)))
        self._clear_notification_task.kill()

    def show_notification(self, upper_line, lower_line):
        self._clear_notification_task.kill()
        self._clear_notification_task.restart()
        self.display_lines[0].message = upper_line
        self.display_lines[1].message = lower_line

    def _clear_notification(self):
        self.display_lines[0].message = " "
        self.display_lines[1].message = " "

# okay decompiling ./MIDIRemoteScripts/Launchkey_MK3/notification.pyc
