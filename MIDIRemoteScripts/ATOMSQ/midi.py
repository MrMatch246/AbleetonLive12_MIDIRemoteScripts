# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ATOMSQ\midi.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 621 bytes
from __future__ import absolute_import, print_function, unicode_literals
NATIVE_MODE_ON_MESSAGE = (143, 0, 1)
NATIVE_MODE_OFF_MESSAGE = (143, 0, 0)
RED_MIDI_CHANNEL = 1
GREEN_MIDI_CHANNEL = 2
BLUE_MIDI_CHANNEL = 3
USER_MODE_START_CHANNEL = 10
SYSEX_START_BYTE = 240
SYSEX_END_BYTE = 247
PRODUCT_ID_BYTES = (0, 1, 6, 34)
SYSEX_HEADER = (
 SYSEX_START_BYTE,) + PRODUCT_ID_BYTES
DISPLAY_HEADER = SYSEX_HEADER + (18, )
LOWER_FIRMWARE_TOGGLE_HEADER = SYSEX_HEADER + (19, )
UPPER_FIRMWARE_TOGGLE_HEADER = SYSEX_HEADER + (20, )

# okay decompiling ./MIDIRemoteScripts/ATOMSQ/midi.pyc
