# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\controls\control.py
# Size of source mod 2**32: 860 bytes
from __future__ import absolute_import, print_function, unicode_literals
from . import EncoderControl, InputControl, SendValueMixin

class SendValueInputControl(InputControl):

    class State(SendValueMixin, InputControl.State):
        pass


class SendValueEncoderControl(EncoderControl):

    class State(SendValueMixin, EncoderControl.State):
        pass

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/controls/control.pyc
