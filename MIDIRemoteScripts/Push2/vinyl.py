# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\vinyl.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1105 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator

class VinylDistortionDecorator(LiveObjectDecorator, EventObject):

    class ModuleSelect(IntEnum):
        tracing = 0
        pinch = 1

    def __init__(self, *a, **k):
        (super(VinylDistortionDecorator, self).__init__)(*a, **k)
        self._add_enum_parameter(name="Module",
          values=[
         "Tracing", "Pinch"],
          default_value=(self.ModuleSelect.tracing))
        self._add_switch_option(name="Pinch Mode",
          pname="Pinch Soft On",
          labels=["Soft", "Hard"])
        self._add_switch_option(name="Pinch Ch",
          pname="Pinch Mono On",
          labels=["Mono", "Stereo"])
        self._add_on_off_option(name="Tracing", pname="Tracing On")
        self._add_on_off_option(name="Pinch", pname="Pinch On")
        self.register_disconnectables(self.options)

# okay decompiling ./MIDIRemoteScripts/Push2/vinyl.pyc
