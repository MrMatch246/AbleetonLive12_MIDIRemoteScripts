# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\resonator.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1238 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator

class ResonatorDeviceDecorator(LiveObjectDecorator, EventObject):

    class Select(IntEnum):
        pitch = 0
        finetune = 1
        gain = 2

    def __init__(self, *a, **k):
        (super(ResonatorDeviceDecorator, self).__init__)(*a, **k)
        self._add_enum_parameter(name="Select",
          values=[
         "Pitch", "Fine Tune", "Gain"],
          default_value=(self.Select.pitch))
        self._add_on_off_option(name="Filter", pname="Filter On")
        self._add_on_off_option(name="Constant", pname="Const")
        self._add_on_off_option(name="I", pname="I On")
        self._add_on_off_option(name="II", pname="II On")
        self._add_on_off_option(name="III", pname="III On")
        self._add_on_off_option(name="IV", pname="IV On")
        self._add_on_off_option(name="V", pname="V On")
        self._add_switch_option(name="Mode", pname="Mode", labels=["Mode B", "Mode A"])
        self.register_disconnectables(self.options)

# okay decompiling ./MIDIRemoteScripts/Push2/resonator.pyc
