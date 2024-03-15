# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launch_Control_XL\ButtonElement.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 943 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ButtonElement import OFF_VALUE, ON_VALUE
from _Framework.ButtonElement import ButtonElement as ButtonElementBase

class ButtonElement(ButtonElementBase):
    _on_value = None
    _off_value = None

    def reset(self):
        self._on_value = None
        self._off_value = None
        super(ButtonElement, self).reset()

    def set_on_off_values(self, on_value, off_value):
        self._on_value = on_value
        self._off_value = off_value

    def send_value(self, value, **k):
        if value is ON_VALUE and self._on_value is not None:
            self._skin[self._on_value].draw(self)
        else:
            if value is OFF_VALUE and self._off_value is not None:
                self._skin[self._off_value].draw(self)
            else:
                (super(ButtonElement, self).send_value)(value, **k)

# okay decompiling ./MIDIRemoteScripts/Launch_Control_XL/ButtonElement.pyc
