# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push\with_priority.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 622 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import DEFAULT_PRIORITY
from ableton.v2.control_surface.elements import WrapperElement

class WithPriority(WrapperElement):

    def __init__(self, wrapped_priority=DEFAULT_PRIORITY, *a, **k):
        (super(WithPriority, self).__init__)(*a, **k)
        self.wrapped_priority = wrapped_priority
        self.register_control_element(self.wrapped_control)

    def get_control_element_priority(self, element, priority):
        return self.wrapped_priority

# okay decompiling ./MIDIRemoteScripts/Push/with_priority.pyc
