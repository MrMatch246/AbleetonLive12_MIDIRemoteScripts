# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MackieControl\MainDisplay.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 3343 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import as_ascii
from .MackieControlComponent import *

class MainDisplay(MackieControlComponent):

    def __init__(self, main_script):
        MackieControlComponent.__init__(self, main_script)
        self._MainDisplay__stack_offset = 0
        self._MainDisplay__last_send_messages = [[], []]

    def destroy(self):
        NUM_CHARS_PER_DISPLAY_LINE = 54
        upper_message = "Ableton Live".center(NUM_CHARS_PER_DISPLAY_LINE)
        self.send_display_string(upper_message, 0, 0)
        lower_message = "Device is offline".center(NUM_CHARS_PER_DISPLAY_LINE)
        self.send_display_string(lower_message, 1, 0)
        MackieControlComponent.destroy(self)

    def stack_offset(self):
        return self._MainDisplay__stack_offset

    def set_stack_offset(self, offset):
        self._MainDisplay__stack_offset = offset

    def send_display_string(self, display_string, display_row, cursor_offset):
        if display_row == 0:
            offset = cursor_offset
        else:
            if display_row == 1:
                offset = NUM_CHARS_PER_DISPLAY_LINE + 2 + cursor_offset
            else:
                message_string = as_ascii(display_string)
                if self._MainDisplay__last_send_messages[display_row] != message_string:
                    self._MainDisplay__last_send_messages[display_row] = message_string
                    if self.main_script().is_extension():
                        device_type = SYSEX_DEVICE_TYPE_XT
                    else:
                        device_type = SYSEX_DEVICE_TYPE
                    display_sysex = (
                     240, 0, 0, 102, device_type, 18, offset) + tuple(message_string) + (247, )
                    self.send_midi(display_sysex)

    def refresh_state(self):
        self._MainDisplay__last_send_messages = [[], []]

    def on_update_display_timer(self):
        pass

# okay decompiling ./MIDIRemoteScripts/MackieControl/MainDisplay.pyc
