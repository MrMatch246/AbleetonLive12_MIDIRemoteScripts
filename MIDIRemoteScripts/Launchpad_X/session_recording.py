# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_X\session_recording.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1799 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from functools import partial
from ableton.v2.base import task
from ableton.v2.control_surface.control import ButtonControl
BLINK_PERIOD = 0.1

class SessionRecordingMixin(object):
    record_button = ButtonControl(delay_time=0.5)

    def __init__(self, *a, **k):
        (super(SessionRecordingMixin, self).__init__)(*a, **k)
        blink_on = partial(self._set_record_button_color, "Recording.CaptureTriggered")
        blink_off = partial(self._set_record_button_color, "DefaultButton.Off")
        self._blink_task = self._tasks.add(task.sequence(task.run(blink_on), task.wait(BLINK_PERIOD), task.run(blink_off), task.wait(BLINK_PERIOD), task.run(blink_on), task.wait(BLINK_PERIOD), task.run(blink_off)))
        self._blink_task.kill()

    @record_button.released_immediately
    def record_button(self, _):
        self._trigger_recording()

    @record_button.pressed_delayed
    def record_button(self, _):
        try:
            if self.song.can_capture_midi:
                self.song.capture_midi()
                self._blink_task.restart()
        except RuntimeError:
            pass

    @record_button.released
    def record_button(self, _):
        self._update_record_button()

    def _update_record_button(self):
        if not self.record_button.is_pressed:
            self._blink_task.kill()
            super(SessionRecordingMixin, self)._update_record_button()

    def _set_record_button_color(self, color):
        self.record_button.color = color

# okay decompiling ./MIDIRemoteScripts/Launchpad_X/session_recording.pyc
