# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_MK2\ComponentUtils.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 399 bytes
from __future__ import absolute_import, print_function, unicode_literals

def skin_scroll_component(component):
    for button in (component.scroll_up_button, component.scroll_down_button):
        button.color = "Scrolling.Enabled"
        button.pressed_color = "Scrolling.Pressed"
        button.disabled_color = "Scrolling.Disabled"

# okay decompiling ./MIDIRemoteScripts/Launchpad_MK2/ComponentUtils.pyc
