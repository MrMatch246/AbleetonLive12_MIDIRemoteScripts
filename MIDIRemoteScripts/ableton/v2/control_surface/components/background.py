# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\components\background.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 2380 bytes
from __future__ import absolute_import, print_function, unicode_literals
from future.utils import itervalues
from functools import partial
from ...base import nop
from ..component import Component

class BackgroundComponent(Component):

    def __init__(self, add_nop_listeners=False, *a, **k):
        (super(BackgroundComponent, self).__init__)(*a, **k)
        self._add_nop_listeners = bool(add_nop_listeners)
        self._control_slots = {}
        self._control_map = {}

    def __getattr__(self, name):
        if len(name) > 4:
            if name[None[:4]] == "set_":
                return partial(self._clear_control, name[4[:None]])
        raise AttributeError(name)

    def _clear_control(self, name, control):
        slot = self._control_slots.get(name, None)
        if slot:
            del self._control_slots[name]
            self.disconnect_disconnectable(slot)
        elif control:
            self._reset_control(control)
            self._control_map[name] = control
            if self._add_nop_listeners:
                self._control_slots[name] = self.register_slot(control, nop, "value")
        elif name in self._control_map:
            del self._control_map[name]

    def _reset_control(self, control):
        control.reset()

    def update(self):
        super(BackgroundComponent, self).update()
        if self.is_enabled():
            for control in itervalues(self._control_map):
                self._reset_control(control)


class ModifierBackgroundComponent(BackgroundComponent):

    def __init__(self, *a, **k):
        (super(ModifierBackgroundComponent, self).__init__)(*a, **k)

    def _reset_control(self, control):
        if len(control.resource.owners) > 1:
            control.set_light(True)
        else:
            control.reset()

# okay decompiling ./MIDIRemoteScripts/ableton/v2/control_surface/components/background.pyc
